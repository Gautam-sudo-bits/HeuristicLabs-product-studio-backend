"""
Google Cloud Storage utilities for video generation pipeline
Handles upload, download, and organization of files in GCS
"""

import os
import time
from datetime import datetime
from google.cloud import storage
from pathlib import Path
import config

# Initialize GCS client
storage_client = storage.Client(project=config.GOOGLE_CLOUD_PROJECT)


def get_project_folder_name(project_id=None):
    """
    Generate a unique project folder name
    
    Args:
        project_id: Optional custom project ID, otherwise uses timestamp
    
    Returns:
        str: Folder name like "project_20250102_143022" or custom project_id
    """
    if project_id:
        return f"project_{project_id}"
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"project_{timestamp}"


def get_gcs_paths(project_id=None):
    """
    Get organized GCS paths for a project
    
    Args:
        project_id: Optional custom project ID
    
    Returns:
        dict: Dictionary with paths for segments, final, and inputs
    """
    project_folder = get_project_folder_name(project_id)
    base_path = f"{config.GCS_OUTPUT_PREFIX}/projects/{project_folder}"
    
    return {
        "base": base_path,
        "segments": f"{base_path}/{config.GCS_SEGMENTS_FOLDER}",
        "final": f"{base_path}/{config.GCS_FINAL_FOLDER}",
        "inputs": f"{base_path}/{config.GCS_INPUTS_FOLDER}",
        "project_folder": project_folder
    }


def upload_to_gcs(local_file_path, gcs_path, content_type=None):
    """
    Upload a file to Google Cloud Storage
    
    Args:
        local_file_path: Path to local file
        gcs_path: Destination path in GCS (without gs:// prefix)
        content_type: Optional MIME type
    
    Returns:
        str: Full GCS URI (gs://bucket/path)
    """
    try:
        bucket = storage_client.bucket(config.GCS_BUCKET_NAME)
        blob = bucket.blob(gcs_path)
        
        # Auto-detect content type if not provided
        if not content_type:
            if local_file_path.endswith('.mp4'):
                content_type = 'video/mp4'
            elif local_file_path.endswith(('.jpg', '.jpeg')):
                content_type = 'image/jpeg'
            elif local_file_path.endswith('.png'):
                content_type = 'image/png'
        
        blob.upload_from_filename(local_file_path, content_type=content_type)
        
        gcs_uri = f"gs://{config.GCS_BUCKET_NAME}/{gcs_path}"
        print(f"✅ Uploaded: {local_file_path} -> {gcs_uri}")
        
        return gcs_uri
        
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        raise


def download_from_gcs(gcs_uri, local_file_path):
    """
    Download a file from Google Cloud Storage
    
    Args:
        gcs_uri: Full GCS URI (gs://bucket/path) or just path
        local_file_path: Destination path for downloaded file
    
    Returns:
        str: Path to downloaded file
    """
    try:
        # Extract bucket and path from URI
        if gcs_uri.startswith("gs://"):
            gcs_uri = gcs_uri[5:]  # Remove gs://
        
        parts = gcs_uri.split("/", 1)
        bucket_name = parts[0]
        blob_path = parts[1] if len(parts) > 1 else ""
        
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        
        blob.download_to_filename(local_file_path)
        
        print(f"✅ Downloaded: gs://{bucket_name}/{blob_path} -> {local_file_path}")
        
        return local_file_path
        
    except Exception as e:
        print(f"❌ Download failed: {e}")
        raise


def upload_reference_images(image_paths, project_id=None):
    """
    Upload reference images to GCS inputs folder
    
    Args:
        image_paths: List of local image file paths
        project_id: Optional custom project ID
    
    Returns:
        list: List of GCS URIs for uploaded images
    """
    gcs_paths = get_gcs_paths(project_id)
    uploaded_uris = []
    
    print(f"\n📤 Uploading {len(image_paths)} reference image(s)...")
    
    for idx, image_path in enumerate(image_paths, 1):
        if not os.path.exists(image_path):
            print(f"⚠️ Image not found: {image_path}")
            continue
        
        filename = os.path.basename(image_path)
        gcs_path = f"{gcs_paths['inputs']}/reference_{idx}_{filename}"
        
        gcs_uri = upload_to_gcs(image_path, gcs_path)
        uploaded_uris.append(gcs_uri)
    
    print(f"✅ Uploaded {len(uploaded_uris)} reference image(s)")
    
    return uploaded_uris


def download_segment_videos(segment_gcs_uris, local_folder=None):
    """
    Download all segment videos from GCS to local temp folder
    
    Args:
        segment_gcs_uris: List of GCS URIs for video segments
        local_folder: Optional local folder path, defaults to config.TEMP_VIDEO_FOLDER
    
    Returns:
        list: List of local file paths for downloaded segments
    """
    if not local_folder:
        local_folder = config.TEMP_VIDEO_FOLDER
    
    os.makedirs(local_folder, exist_ok=True)
    
    local_paths = []
    
    print(f"\n📥 Downloading {len(segment_gcs_uris)} video segment(s)...")
    
    for idx, gcs_uri in enumerate(segment_gcs_uris, 1):
        local_path = os.path.join(local_folder, f"segment_{idx}.mp4")
        download_from_gcs(gcs_uri, local_path)
        local_paths.append(local_path)
    
    print(f"✅ Downloaded {len(local_paths)} segment(s) to {local_folder}")
    
    return local_paths


def upload_final_video(local_video_path, project_id=None, filename="final_video.mp4"):
    """
    Upload final merged video to GCS
    
    Args:
        local_video_path: Path to local merged video
        project_id: Optional custom project ID
        filename: Name for the final video file
    
    Returns:
        str: GCS URI of uploaded final video
    """
    gcs_paths = get_gcs_paths(project_id)
    gcs_path = f"{gcs_paths['final']}/{filename}"
    
    print(f"\n📤 Uploading final video...")
    gcs_uri = upload_to_gcs(local_video_path, gcs_path, content_type='video/mp4')
    
    print(f"✅ Final video uploaded: {gcs_uri}")
    
    return gcs_uri


def cleanup_temp_files(local_folder=None):
    """
    Clean up temporary video files
    
    Args:
        local_folder: Folder to clean, defaults to config.TEMP_VIDEO_FOLDER
    """
    if not local_folder:
        local_folder = config.TEMP_VIDEO_FOLDER
    
    if not os.path.exists(local_folder):
        return
    
    print(f"\n🧹 Cleaning up temporary files in {local_folder}...")
    
    deleted_count = 0
    for file in os.listdir(local_folder):
        file_path = os.path.join(local_folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                deleted_count += 1
        except Exception as e:
            print(f"⚠️ Could not delete {file_path}: {e}")
    
    print(f"✅ Cleaned up {deleted_count} temporary file(s)")


def list_gcs_files(gcs_folder_path):
    """
    List all files in a GCS folder
    
    Args:
        gcs_folder_path: GCS folder path (without gs:// prefix)
    
    Returns:
        list: List of blob names
    """
    try:
        bucket = storage_client.bucket(config.GCS_BUCKET_NAME)
        blobs = bucket.list_blobs(prefix=gcs_folder_path)
        
        files = [blob.name for blob in blobs if not blob.name.endswith('/')]
        
        return files
        
    except Exception as e:
        print(f"❌ Error listing files: {e}")
        return []


if __name__ == "__main__":
    # Test GCS utilities
    print("Testing GCS utilities...")
    config.validate_config()
    
    # Test path generation
    paths = get_gcs_paths("test_project")
    print("\n📁 Generated GCS paths:")
    for key, path in paths.items():
        print(f"  {key}: {path}")