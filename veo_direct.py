"""
Veo 3.1 Local Pipeline - Generate videos from local images and prompts
Input: Local images + prompt.txt
Output: Video saved locally AND in GCS bucket
GCS is used transparently for API requirements
"""

import os
import time
from datetime import datetime
from pathlib import Path
from google import genai
from google.genai import types
from google.cloud import storage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===========================
# CONFIGURATION FLAGS
# ===========================
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
GOOGLE_GENAI_USE_VERTEXAI = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "True")
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")

# Set environment variables for SDK
os.environ["GOOGLE_CLOUD_PROJECT"] = GOOGLE_CLOUD_PROJECT
os.environ["GOOGLE_CLOUD_LOCATION"] = GOOGLE_CLOUD_LOCATION
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = GOOGLE_GENAI_USE_VERTEXAI

# Video generation settings
VIDEO_MODEL = "veo-3.1-generate-preview"
VIDEO_RESOLUTION = "720p"
VIDEO_ASPECT_RATIO = "16:9"
DURATION_VIDEO = 6
GENERATE_AUDIO = False
ALLOW_PEOPLE_IN_VIDEO = False
MAX_RETRIES = 3
RETRY_DELAY = 10

# Folder structure
INPUT_IMAGES_FOLDER = "inputs/images/new_idea"
INPUT_PROMPTS_FOLDER = "inputs/prompts"
OUTPUT_VIDEOS_FOLDER = "outputs/videos"
GCS_BASE_FOLDER = "test"  # Root folder in GCS bucket
GCS_TEMP_IMAGES_FOLDER = "temp_images"  # Temporary image storage

# ===========================
# HELPER FUNCTIONS
# ===========================

def validate_setup():
    """Validate configuration and folder structure"""
    print("🔍 Validating setup...")
    
    # Check environment variables
    if not GOOGLE_CLOUD_PROJECT:
        raise ValueError("Missing GOOGLE_CLOUD_PROJECT in .env file")
    if not GCS_BUCKET_NAME:
        raise ValueError("Missing GCS_BUCKET_NAME in .env file")
    
    # Create local folders
    os.makedirs(INPUT_IMAGES_FOLDER, exist_ok=True)
    os.makedirs(INPUT_PROMPTS_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_VIDEOS_FOLDER, exist_ok=True)
    
    print(f"   ✅ Project: {GOOGLE_CLOUD_PROJECT}")
    print(f"   ✅ Location: {GOOGLE_CLOUD_LOCATION}")
    print(f"   ✅ Bucket: {GCS_BUCKET_NAME}")
    print(f"   ✅ Folders created")


def get_next_video_number(storage_client, bucket_name, base_folder):
    """
    Find the next available video_save_N number in GCS bucket
    
    Returns:
        int: Next available number (e.g., if video_save_1 and video_save_2 exist, returns 3)
    """
    print(f"🔢 Finding next video number in gs://{bucket_name}/{base_folder}/...")
    
    try:
        bucket = storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=f"{base_folder}/video_save_")
        
        # Extract existing numbers
        existing_numbers = set()
        for blob in blobs:
            # Parse "test/video_save_1/..." -> extract 1
            path_parts = blob.name.split('/')
            if len(path_parts) >= 2 and path_parts[1].startswith('video_save_'):
                try:
                    num = int(path_parts[1].replace('video_save_', ''))
                    existing_numbers.add(num)
                except ValueError:
                    continue
        
        if existing_numbers:
            next_num = max(existing_numbers) + 1
        else:
            next_num = 1
        
        print(f"   ✅ Next video number: {next_num}")
        return next_num
    
    except Exception as e:
        print(f"   ⚠️ Error checking existing videos: {e}")
        print(f"   ℹ️ Defaulting to video_save_1")
        return 1


def upload_local_images_to_gcs(storage_client, bucket_name, local_images_folder):
    """
    Upload all images from local folder to GCS temporary location
    
    Returns:
        list: GCS URIs of uploaded images
    """
    print(f"\n📤 Uploading local images to GCS...")
    
    # Get all image files
    image_extensions = ['.png', '.jpg', '.jpeg', '.webp']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(Path(local_images_folder).glob(f'*{ext}'))
        image_files.extend(Path(local_images_folder).glob(f'*{ext.upper()}'))
    
    if not image_files:
        raise ValueError(f"No images found in {local_images_folder}")
    
    print(f"   Found {len(image_files)} image(s)")
    
    bucket = storage_client.bucket(bucket_name)
    gcs_uris = []
    
    for img_path in image_files:
        # Upload to temp location: temp_images/image_name.png
        gcs_path = f"{GCS_TEMP_IMAGES_FOLDER}/{img_path.name}"
        blob = bucket.blob(gcs_path)
        
        print(f"   📤 Uploading {img_path.name}...", end=" ")
        blob.upload_from_filename(str(img_path))
        
        gcs_uri = f"gs://{bucket_name}/{gcs_path}"
        gcs_uris.append(gcs_uri)
        print(f"✅")
    
    print(f"   ✅ All images uploaded to gs://{bucket_name}/{GCS_TEMP_IMAGES_FOLDER}/")
    return gcs_uris


def cleanup_temp_images(storage_client, bucket_name):
    """Delete temporary images from GCS"""
    print(f"\n🧹 Cleaning up temporary images...")
    
    try:
        bucket = storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=f"{GCS_TEMP_IMAGES_FOLDER}/")
        
        deleted_count = 0
        for blob in blobs:
            blob.delete()
            deleted_count += 1
        
        print(f"   ✅ Deleted {deleted_count} temporary image(s)")
    
    except Exception as e:
        print(f"   ⚠️ Cleanup error: {e}")


def read_prompt_file(prompt_file_path):
    """Read prompt from text file"""
    print(f"\n📝 Reading prompt from {prompt_file_path}...")
    
    if not os.path.exists(prompt_file_path):
        raise FileNotFoundError(f"Prompt file not found: {prompt_file_path}")
    
    with open(prompt_file_path, 'r', encoding='utf-8') as f:
        prompt = f.read().strip()
    
    if not prompt:
        raise ValueError("Prompt file is empty")
    
    print(f"   ✅ Prompt loaded ({len(prompt)} characters)")
    print(f"   Preview: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")
    
    return prompt


def detect_mime_type(gcs_uri):
    """Detect MIME type from GCS URI extension"""
    uri_lower = gcs_uri.lower()
    
    if uri_lower.endswith('.png'):
        return 'image/png'
    elif uri_lower.endswith('.jpg') or uri_lower.endswith('.jpeg'):
        return 'image/jpeg'
    elif uri_lower.endswith('.webp'):
        return 'image/webp'
    else:
        return 'image/png'  # default


def generate_video(genai_client, prompt, image_gcs_uris, output_gcs_uri):
    """
    Generate video using Veo 3.1
    
    Args:
        genai_client: Google GenAI client
        prompt: Video generation prompt
        image_gcs_uris: List of GCS URIs for reference images
        output_gcs_uri: GCS URI for output video storage
    
    Returns:
        str: GCS URI of generated video, or None if failed
    """
    print(f"\n🎬 Generating video with Veo 3.1...")
    print(f"   Model: {VIDEO_MODEL}")
    print(f"   Resolution: {VIDEO_RESOLUTION}")
    print(f"   Aspect Ratio: {VIDEO_ASPECT_RATIO}")
    print(f"   Duration: 4 seconds")
    print(f"   Audio: {'Enabled' if GENERATE_AUDIO else 'Disabled'}")
    print(f"   Reference Images: {len(image_gcs_uris)}")
    
    # Use primary (first) image as main reference
    primary_image_uri = image_gcs_uris[0]
    mime_type = detect_mime_type(primary_image_uri)
    
    person_gen = "allow_adult" if ALLOW_PEOPLE_IN_VIDEO else "disallow"
    
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"\n   🔄 Attempt {attempt}/{MAX_RETRIES}")
        
        try:
            # Veo API call
            operation = genai_client.models.generate_videos(
                model=VIDEO_MODEL,
                prompt=prompt,
                image=types.Image(
                    gcs_uri=primary_image_uri,
                    mime_type=mime_type,
                ),
                config=types.GenerateVideosConfig(
                    aspect_ratio=VIDEO_ASPECT_RATIO,
                    duration_seconds=DURATION_VIDEO,
                    resolution=VIDEO_RESOLUTION,
                    person_generation=person_gen,
                    generate_audio=GENERATE_AUDIO,
                    output_gcs_uri=output_gcs_uri,
                ),
            )
            
            print(f"      ✅ Operation submitted: {operation.name}")
            
            # Wait for completion
            video_uri = wait_for_completion(genai_client, operation)
            
            if video_uri:
                return video_uri
            
            # Retry logic
            if attempt < MAX_RETRIES:
                print(f"      ⏸️ Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
        
        except Exception as e:
            print(f"      ❌ Error: {e}")
            if attempt < MAX_RETRIES:
                print(f"      ⏸️ Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                import traceback
                traceback.print_exc()
    
    print(f"   ❌ All {MAX_RETRIES} attempts failed")
    return None


def wait_for_completion(genai_client, operation):
    """Poll operation until complete"""
    print(f"      ⏳ Waiting for video generation...")
    
    poll_count = 0
    max_polls = 60  # 15 minutes max (60 * 15s)
    
    while not operation.done and poll_count < max_polls:
        time.sleep(15)
        poll_count += 1
        
        if poll_count % 4 == 0:
            elapsed = poll_count * 15
            print(f"         {elapsed}s elapsed...")
        
        try:
            operation = genai_client.operations.get(operation)
        except Exception as e:
            print(f"         ⚠️ Polling error: {e}")
            time.sleep(5)
            continue
    
    if poll_count >= max_polls:
        print(f"      ⏱️ Timeout after {max_polls * 15}s")
        return None
    
    print(f"      ✅ Generation complete!")
    
    # Check for errors
    if operation.error:
        print(f"      ❌ Veo error: {operation.error}")
        return None
    
    # Extract video URI
    try:
        if operation.response:
            video_uri = operation.result.generated_videos[0].video.uri
            print(f"      📹 Video URI: {video_uri}")
            return video_uri
        else:
            print(f"      ❌ No response in operation")
            return None
    except Exception as e:
        print(f"      ❌ URI extraction error: {e}")
        return None


def download_video_from_gcs(storage_client, video_gcs_uri, local_output_path):
    """
    Download video from GCS to local folder
    
    Args:
        storage_client: GCS storage client
        video_gcs_uri: GCS URI of video (gs://bucket/path/to/video.mp4)
        local_output_path: Local path to save video
    """
    print(f"\n📥 Downloading video to local folder...")
    
    # Parse GCS URI
    if not video_gcs_uri.startswith('gs://'):
        raise ValueError(f"Invalid GCS URI: {video_gcs_uri}")
    
    # Remove 'gs://' and split bucket/path
    uri_parts = video_gcs_uri[5:].split('/', 1)
    bucket_name = uri_parts[0]
    blob_path = uri_parts[1] if len(uri_parts) > 1 else ''
    
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    
    print(f"   Source: {video_gcs_uri}")
    print(f"   Destination: {local_output_path}")
    
    blob.download_to_filename(local_output_path)
    
    file_size_mb = os.path.getsize(local_output_path) / (1024 * 1024)
    print(f"   ✅ Downloaded successfully ({file_size_mb:.2f} MB)")


# ===========================
# MAIN PIPELINE
# ===========================

def run_pipeline():
    """Main pipeline execution"""
    start_time = time.time()
    
    print("=" * 70)
    print("🎬 VEO 3.1 LOCAL VIDEO GENERATION PIPELINE")
    print("=" * 70)
    
    # Step 1: Validate setup
    validate_setup()
    
    # Step 2: Initialize clients
    print(f"\n🔧 Initializing Google Cloud clients...")
    genai_client = genai.Client()
    storage_client = storage.Client(project=GOOGLE_CLOUD_PROJECT)
    print(f"   ✅ Clients initialized")
    
    # Step 3: Read prompt
    prompt_file = os.path.join(INPUT_PROMPTS_FOLDER, "prompt.txt")
    prompt = read_prompt_file(prompt_file)
    
    # Step 4: Upload images to GCS
    image_gcs_uris = upload_local_images_to_gcs(
        storage_client, 
        GCS_BUCKET_NAME, 
        INPUT_IMAGES_FOLDER
    )
    
    # Step 5: Determine output location in GCS
    video_number = get_next_video_number(storage_client, GCS_BUCKET_NAME, GCS_BASE_FOLDER)
    video_folder_name = f"video_save_{video_number}"
    
    # IMPORTANT: Set output to specific file path to avoid nested folders
    output_gcs_uri = f"gs://{GCS_BUCKET_NAME}/{GCS_BASE_FOLDER}/{video_folder_name}/generated_video.mp4"
    
    print(f"\n📂 Video will be saved to:")
    print(f"   GCS: {output_gcs_uri}")
    
    # Step 6: Generate video
    video_uri = generate_video(
        genai_client,
        prompt,
        image_gcs_uris,
        output_gcs_uri
    )
    
    if not video_uri:
        print(f"\n❌ Video generation failed!")
        cleanup_temp_images(storage_client, GCS_BUCKET_NAME)
        return
    
    # Step 7: Download video locally
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    local_filename = f"video_{timestamp}.mp4"
    local_output_path = os.path.join(OUTPUT_VIDEOS_FOLDER, local_filename)
    
    download_video_from_gcs(storage_client, video_uri, local_output_path)
    
    # Step 8: Cleanup temporary images
    cleanup_temp_images(storage_client, GCS_BUCKET_NAME)
    
    # Success summary
    elapsed_time = time.time() - start_time
    print("\n" + "=" * 70)
    print("✅ PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print(f"📹 Local Video: {local_output_path}")
    print(f"☁️  GCS Video: {video_uri}")
    print(f"⏱️  Total Time: {elapsed_time:.1f} seconds")
    print("=" * 70)


if __name__ == "__main__":
    try:
        run_pipeline()
    except KeyboardInterrupt:
        print("\n\n⚠️ Pipeline interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Pipeline failed: {e}")
        import traceback
        traceback.print_exc()