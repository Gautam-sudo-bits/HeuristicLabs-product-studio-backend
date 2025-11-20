"""
Veo 3.1 Video Generation using google-genai SDK (AI Studio)
Simpler authentication, no quota project required
"""

import time
from datetime import datetime
from google import genai
from google.genai import types
import config


class VeoVideoGenerator:
    """Generates videos using google-genai SDK"""
    
    def __init__(self):
        self.client = genai.Client()  # ← Simple initialization, no project needed!
        self.model = config.VIDEO_MODEL
    
    def generate_video_segment(
        self,
        prompt,
        reference_image_gcs_uri,
        output_gcs_uri,
        segment_number=1,
        seed=None
    ):
        """
        Generate a single video segment using Veo 3.1
        
        Args:
            prompt: Text prompt for video generation
            reference_image_gcs_uri: GCS URI for the reference image
            output_gcs_uri: GCS URI for output storage
            segment_number: Segment identifier for logging
            seed: Optional seed for reproducibility
        
        Returns:
            str: GCS URI of generated video, or None if failed
        """
        print(f"\n🎬 Generating Segment {segment_number}...")
        print(f"   Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")
        print(f"   Reference Image: {reference_image_gcs_uri}")
        print(f"   Resolution: {config.VIDEO_RESOLUTION}")
        print(f"   Aspect Ratio: {config.VIDEO_ASPECT_RATIO}")
        print(f"   Audio Generation: {config.GENERATE_AUDIO}")
        if seed:
            print(f"   Seed: {seed}")
        
        try:
            person_gen = "disabled" if not config.ALLOW_PEOPLE_IN_VIDEO else "allow_adult"
            
            # Detect MIME type from GCS URI
            mime_type = self._detect_mime_type(reference_image_gcs_uri)
            
            # VEO API CALL (google-genai SDK pattern)
            operation = self.client.models.generate_videos(
                model=self.model,
                prompt=prompt,
                image=types.Image(
                    gcs_uri=reference_image_gcs_uri,
                    mime_type=mime_type,
                ),
                config=types.GenerateVideosConfig(
                    aspect_ratio=config.VIDEO_ASPECT_RATIO,
                    duration_seconds=8,  # Standard 8-second segments
                    resolution=config.VIDEO_RESOLUTION,
                    person_generation=person_gen,
                    generate_audio=config.GENERATE_AUDIO,
                    output_gcs_uri=output_gcs_uri,
                ),
            )
            
            print(f"   ✓ Operation submitted: {operation.name}")
            
            # Wait for completion
            video_uri = self._wait_for_completion(operation, segment_number)
            
            return video_uri
            
        except Exception as e:
            print(f"   ❌ Generation error: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _wait_for_completion(self, operation, segment_number):
        """Poll operation until complete"""
        print(f"   ⏳ Waiting for Veo generation...")
        
        poll_count = 0
        max_polls = 60  # 15 minutes max (60 * 15s)
        
        while not operation.done and poll_count < max_polls:
            time.sleep(15)
            poll_count += 1
            
            if poll_count % 4 == 0:
                elapsed = poll_count * 15
                print(f"      {elapsed}s elapsed...")
            
            try:
                operation = self.client.operations.get(operation)
            except Exception as e:
                print(f"   ⚠️ Polling error: {e}")
                time.sleep(5)
                continue
        
        if poll_count >= max_polls:
            print(f"   ⏱️ Timeout after {max_polls * 15}s")
            return None
        
        print(f"   ✅ Segment {segment_number} complete!")
        
        # Check for errors
        if operation.error:
            print(f"   ❌ Veo error: {operation.error}")
            return None
        
        # Extract video URI
        try:
            if operation.response:
                video_uri = operation.result.generated_videos[0].video.uri
                print(f"   📹 Video URI: {video_uri}")
                return video_uri
            else:
                print(f"   ❌ No response in operation")
                return None
        except Exception as e:
            print(f"   ❌ URI extraction error: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _detect_mime_type(self, gcs_uri):
        """Detect MIME type from GCS URI extension"""
        uri_lower = gcs_uri.lower()
        
        if uri_lower.endswith('.png'):
            return 'image/png'
        elif uri_lower.endswith('.jpg') or uri_lower.endswith('.jpeg'):
            return 'image/jpeg'
        elif uri_lower.endswith('.webp'):
            return 'image/webp'
        else:
            print(f"   ⚠️ Unknown image format, defaulting to image/png")
            return 'image/png'


def generate_segment_with_retry(
    prompt,
    reference_image_gcs_uris,
    output_storage_uri,
    segment_number,
    seed=None,
    max_retries=None
):
    """
    Generate video segment with automatic retry logic
    
    Args:
        prompt: Video prompt
        reference_image_gcs_uris: List of reference image GCS URIs
        output_storage_uri: Output GCS base path
        segment_number: Segment identifier
        seed: Optional seed
        max_retries: Maximum retry attempts
    
    Returns:
        str: GCS URI of generated video, or None if all retries failed
    """
    if max_retries is None:
        max_retries = config.MAX_RETRIES
    
    # ============================================================
    # CRITICAL: Use PRIMARY (first) image for ALL segments
    # This ensures product consistency across the entire video
    # ============================================================
    primary_image_uri = reference_image_gcs_uris[0]
    
    generator = VeoVideoGenerator()
    
    for attempt in range(1, max_retries + 1):
        print(f"\n{'='*70}")
        print(f"SEGMENT {segment_number} - Attempt {attempt}/{max_retries}")
        print(f"{'='*70}")
        
        # Log generation start
        log_generation_start(segment_number, prompt, f"attempt_{attempt}")
        
        # Generate video
        video_uri = generator.generate_video_segment(
            prompt=prompt,
            reference_image_gcs_uri=primary_image_uri,  # ← SAME image for all segments
            output_gcs_uri=output_storage_uri,
            segment_number=segment_number,
            seed=seed
        )
        
        if video_uri:
            print(f"\n   ✅ Segment {segment_number} generated successfully!")
            log_generation_success(segment_number, video_uri, attempt)
            return video_uri
        
        # Retry logic
        if attempt < max_retries:
            print(f"   ⏸️ Retrying in {config.RETRY_DELAY} seconds...")
            time.sleep(config.RETRY_DELAY)
        else:
            print(f"   ❌ All {max_retries} attempts failed")
            log_generation_failure(segment_number, "Max retries exceeded")
    
    return None


def log_generation_start(segment_number, prompt, operation_id):
    """Log video generation start"""
    import os
    os.makedirs(os.path.dirname(config.VEO_LOG_FILE), exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(config.VEO_LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*80}\n")
        f.write(f"[{timestamp}] SEGMENT {segment_number} - STARTED\n")
        f.write(f"Operation ID: {operation_id}\n")
        f.write(f"Prompt: {prompt[:200]}{'...' if len(prompt) > 200 else ''}\n")
        f.write(f"{'='*80}\n")


def log_generation_success(segment_number, video_uri, attempt):
    """Log successful video generation"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(config.VEO_LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] SEGMENT {segment_number} - SUCCESS (Attempt {attempt})\n")
        f.write(f"Video URI: {video_uri}\n\n")


def log_generation_failure(segment_number, error_message):
    """Log failed video generation"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(config.VEO_LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] SEGMENT {segment_number} - FAILED\n")
        f.write(f"Error: {error_message}\n\n")


def generate_all_segments(
    segment_prompts,
    reference_image_gcs_uris,
    project_id=None,
    seed=None
):
    """
    Generate all video segments sequentially
    
    Args:
        segment_prompts: List of (segment_number, prompt) tuples
        reference_image_gcs_uris: List of reference image GCS URIs
        project_id: Optional project ID for GCS organization
        seed: Optional seed for consistency
    
    Returns:
        list: List of GCS URIs for generated videos (in order)
    """
    from gcs_utils import get_gcs_paths
    
    gcs_paths = get_gcs_paths(project_id)
    output_base_uri = f"gs://{config.GCS_BUCKET_NAME}/{gcs_paths['segments']}/"
    
    generated_videos = []
    
    print(f"\n{'='*70}")
    print(f"GENERATING {len(segment_prompts)} VIDEO SEGMENT(S)")
    print(f"{'='*70}")
    print(f"SDK: google-genai (AI Studio) ✅")
    print(f"Model: {config.VIDEO_MODEL}")
    print(f"Output location: {output_base_uri}")
    print(f"Reference images: {len(reference_image_gcs_uris)}")
    for idx, img_uri in enumerate(reference_image_gcs_uris):
        print(f"  Image {idx+1}: {img_uri}")
    print(f"Using PRIMARY image (Image 1) for ALL segments (ensures consistency)")
    
    for seg_num, prompt in segment_prompts:
        video_uri = generate_segment_with_retry(
            prompt=prompt,
            reference_image_gcs_uris=reference_image_gcs_uris,
            output_storage_uri=output_base_uri,
            segment_number=seg_num,
            seed=seed
        )
        
        if video_uri:
            generated_videos.append(video_uri)
        else:
            # Critical failure - cannot continue
            print(f"\n❌ CRITICAL: Segment {seg_num} generation failed after {config.MAX_RETRIES} attempts")
            print(f"❌ Cannot continue without all segments in sequence")
            raise Exception(f"Failed to generate segment {seg_num}")
    
    print(f"\n{'='*70}")
    print(f"✅ ALL {len(generated_videos)} SEGMENTS GENERATED SUCCESSFULLY")
    print(f"{'='*70}\n")
    
    return generated_videos


if __name__ == "__main__":
    # Test video generation
    print("Testing video generation with google-genai SDK...")
    config.validate_config()
    
    print("\n⚠️ This is a test stub. In production, use generate_all_segments()")
    print("✅ SDK: google-genai (no quota project required)")