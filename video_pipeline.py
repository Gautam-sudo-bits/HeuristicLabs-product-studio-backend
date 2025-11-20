"""
Main pipeline for product demo video generation
Orchestrates: prompt generation → video generation → merging → upload
"""

import os
import sys
from datetime import datetime
import config
from gcs_utils import (
    upload_reference_images,
    download_segment_videos,
    upload_final_video,
    cleanup_temp_files,
    get_gcs_paths
)
from prompt_generator_for_video import generate_and_process_prompts
from video_generator import generate_all_segments
from video_merger import merge_videos_with_crossfade, log_merge_operation


def log_pipeline_start(user_requirements, reference_images):
    """Log pipeline start"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(config.PIPELINE_LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*80}\n")
        f.write(f"PIPELINE STARTED: {timestamp}\n")
        f.write(f"{'='*80}\n")
        f.write(f"User Requirements:\n{user_requirements}\n\n")
        f.write(f"Reference Images: {len(reference_images)}\n")
        for idx, img in enumerate(reference_images, 1):
            f.write(f"  {idx}. {img}\n")
        f.write(f"{'='*80}\n\n")


def log_pipeline_end(success, final_video_uri=None, error=None):
    """Log pipeline completion"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(config.PIPELINE_LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*80}\n")
        f.write(f"PIPELINE {'COMPLETED' if success else 'FAILED'}: {timestamp}\n")
        f.write(f"{'='*80}\n")
        
        if success and final_video_uri:
            f.write(f"Final Video: {final_video_uri}\n")
        
        if error:
            f.write(f"Error: {error}\n")
        
        f.write(f"{'='*80}\n\n")


def run_pipeline(
    user_requirements,
    reference_image_paths,
    project_id=None,
    total_duration=None,
    segment_duration=None,
    seed=None
):
    """
    Main pipeline function
    
    Args:
        user_requirements: User's video requirements/description
        reference_image_paths: List of local paths to reference images (max 3)
        project_id: Optional custom project ID for organization
        total_duration: Total video duration in seconds
        segment_duration: Duration per segment in seconds
        seed: Optional seed for reproducibility
    
    Returns:
        str: GCS URI of final merged video
    """
    print("\n" + "="*80)
    print("🎬 PRODUCT DEMO VIDEO GENERATION PIPELINE")
    print("="*80)
    
    # Validate configuration
    config.validate_config()
    
    # Log pipeline start
    log_pipeline_start(user_requirements, reference_image_paths)
    
    try:
        # ========================================
        # STEP 1: Upload Reference Images to GCS
        # ========================================
        print("\n" + "="*80)
        print("STEP 1: Uploading Reference Images")
        print("="*80)
        
        reference_image_gcs_uris = upload_reference_images(
            reference_image_paths,
            project_id=project_id
        )
        
        if not reference_image_gcs_uris:
            raise Exception("No reference images uploaded successfully")
        
        print(f"✅ {len(reference_image_gcs_uris)} reference image(s) uploaded")
        
        # ========================================
        # STEP 2: Generate Prompts with Gemini
        # ========================================
        print("\n" + "="*80)
        print("STEP 2: Generating Video Prompts with Gemini")
        print("="*80)
        
        prompts_json, segment_prompts = generate_and_process_prompts(
            user_requirements=user_requirements,
            reference_image_paths=reference_image_paths,
            total_duration=total_duration,
            segment_duration=segment_duration
        )
        
        print(f"✅ Generated {len(segment_prompts)} segment prompt(s)")
        
        # Print prompts for review
        print("\n📋 Generated Prompts:")
        print("-" * 80)
        for seg_num, prompt in segment_prompts:
            print(f"\nSegment {seg_num}:")
            print(f"  {prompt[:200]}{'...' if len(prompt) > 200 else ''}")
        print("-" * 80)
        
        # Check if in prompt-only mode
        if config.PROMPT_ONLY_MODE:
            print("\n⚠️  PROMPT_ONLY_MODE is enabled")
            print("Prompts have been generated and saved.")
            print("Video generation is skipped.")
            print(f"Check prompts in: {config.PROMPT_DISPLAY_FILE}")
            return None
        
        # ========================================
        # STEP 3: Generate Video Segments with Veo
        # ========================================
        print("\n" + "="*80)
        print("STEP 3: Generating Video Segments with Veo 3.1")
        print("="*80)
        
        segment_video_uris = generate_all_segments(
            segment_prompts=segment_prompts,
            reference_image_gcs_uris=reference_image_gcs_uris,
            project_id=project_id,
            seed=seed
        )
        
        print(f"✅ All {len(segment_video_uris)} segment(s) generated")
        
        # ========================================
        # STEP 4: Download Segments for Merging
        # ========================================
        print("\n" + "="*80)
        print("STEP 4: Downloading Segments for Merging")
        print("="*80)
        
        local_segment_paths = download_segment_videos(segment_video_uris)
        
        print(f"✅ Downloaded {len(local_segment_paths)} segment(s)")
        
        # ========================================
        # STEP 5: Merge Videos with Crossfade
        # ========================================
        print("\n" + "="*80)
        print("STEP 5: Merging Video Segments")
        print("="*80)
        
        # Create output filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        merged_filename = f"merged_video_{timestamp}.mp4"
        local_merged_path = os.path.join(config.TEMP_VIDEO_FOLDER, merged_filename)
        
        # Merge videos
        merge_videos_with_crossfade(
            video_paths=local_segment_paths,
            output_path=local_merged_path,
            crossfade_duration=config.CROSSFADE_DURATION
        )
        
        # Log merge operation
        log_merge_operation(local_segment_paths, local_merged_path, "crossfade")
        
        print(f"✅ Video merged successfully")
        
        # ========================================
        # STEP 6: Upload Final Video to GCS
        # ========================================
        print("\n" + "="*80)
        print("STEP 6: Uploading Final Video to GCS")
        print("="*80)
        
        final_video_uri = upload_final_video(
            local_video_path=local_merged_path,
            project_id=project_id,
            filename=f"final_product_video_{timestamp}.mp4"
        )
        
        print(f"✅ Final video uploaded")
        
        # ========================================
        # STEP 7: Cleanup Temporary Files
        # ========================================
        print("\n" + "="*80)
        print("STEP 7: Cleaning Up Temporary Files")
        print("="*80)
        
        cleanup_temp_files()
        
        print(f"✅ Cleanup completed")
        
        # ========================================
        # PIPELINE COMPLETE
        # ========================================
        print("\n" + "="*80)
        print("🎉 PIPELINE COMPLETED SUCCESSFULLY")
        print("="*80)
        print(f"\n📹 Final Video: {final_video_uri}")
        print(f"\n📊 Summary:")
        print(f"  - Reference Images: {len(reference_image_gcs_uris)}")
        print(f"  - Segments Generated: {len(segment_video_uris)}")
        print(f"  - Transition Style: Crossfade ({config.CROSSFADE_DURATION}s)")
        print(f"  - Resolution: {config.VIDEO_RESOLUTION}")
        print(f"  - Audio: {'Enabled' if config.GENERATE_AUDIO else 'Disabled'}")
        
        # Print GCS folder structure
        gcs_paths = get_gcs_paths(project_id)
        print(f"\n📁 GCS Project Folder:")
        print(f"  gs://{config.GCS_BUCKET_NAME}/{gcs_paths['base']}/")
        print(f"    ├── inputs/       (reference images)")
        print(f"    ├── segments/     ({len(segment_video_uris)} video segments)")
        print(f"    └── final/        (merged video)")
        
        print("\n" + "="*80)
        
        # Log success
        log_pipeline_end(True, final_video_uri)
        
        return final_video_uri
        
    except Exception as e:
        print(f"\n❌ PIPELINE FAILED: {e}")
        log_pipeline_end(False, error=str(e))
        
        # Cleanup on failure
        try:
            cleanup_temp_files()
        except:
            pass
        
        raise


def main():
    """
    Example usage of the pipeline
    """
    print("Product Demo Video Generation Pipeline")
    print("="*80)
    
    # Example configuration
    user_requirements = """
    Brand theme: Blue, white. ABstract, with organic key elements, professionally created video of the shoe pair.
    """
    
    # Reference images (update these paths)
    reference_image_paths = [
        r"E:\product-image-backend\test_images\shoe_pair.jpg",
    ]
    
    # Check if images exist
    for img_path in reference_image_paths[:]:
        if not os.path.exists(img_path):
            print(f"⚠️ Warning: Image not found: {img_path}")
            reference_image_paths.remove(img_path)
    
    if not reference_image_paths:
        print("❌ No valid reference images found")
        print("Please update the reference_image_paths in main()")
        sys.exit(1)
    
    # Run pipeline
    try:
        final_video_uri = run_pipeline(
            user_requirements=user_requirements,
            reference_image_paths=reference_image_paths,
            project_id=None,  # Auto-generate project ID
            total_duration=config.DEFAULT_TOTAL_DURATION,
            segment_duration=config.DEFAULT_SEGMENT_DURATION,
            seed=config.VEO_SEED
        )
        
        print(f"\n✅ Success! Final video: {final_video_uri}")
        
    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()