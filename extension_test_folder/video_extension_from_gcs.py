"""
Quick script to extend your already-generated video
No need for operation ID - just the GCS path!
"""

import time
import requests
from google.auth import default
from google.auth.transport.requests import Request

# Your configuration
PROJECT_ID = "gen-lang-client-0825799617"
LOCATION = "us-central1"
GCS_BUCKET = "vertex-ai-veo-outputs"
GCS_PREFIX = "veo-product-videos"
MODEL_ID = "veo-3.1-generate-preview"
BASE_URL = f"https://{LOCATION}-aiplatform.googleapis.com/v1"

# YOUR GENERATED VIDEO PATH (update this!)
EXISTING_VIDEO = "gs://vertex-ai-veo-outputs/veo-product-videos/10439118813818453868/sample_0.mp4"

# YOUR EXTENSION PROMPT
EXTENSION_PROMPT = """The earbud continues rotating, camera slowly zooms in to show the touch controls,
a finger reaches in and taps the surface activating blue LED lights, maintain the same 
minimalist background and studio lighting"""

# Optional: Use same seed for visual consistency
SEED = 12345


def get_access_token():
    credentials, project = default()
    credentials.refresh(Request())
    return credentials.token


def extend_video(video_gcs_path, extension_prompt, seed=None):
    """Extend an existing video"""
    url = f"{BASE_URL}/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/{MODEL_ID}:predictLongRunning"
    
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json"
    }
    
    parameters = {
        "storageUri": f"gs://{GCS_BUCKET}/{GCS_PREFIX}/extended/",
        "sampleCount": 1,
        "aspectRatio": "16:9",
        "resolution": "720p",
        "personGeneration": "allow_adult"
    }
    
    if seed is not None:
        parameters["seed"] = seed
    
    payload = {
        "instances": [
            {
                "prompt": extension_prompt,
                "video": {
                    "gcsUri": video_gcs_path,
                    "mimeType": "video/mp4"
                }
            }
        ],
        "parameters": parameters
    }
    
    print("=" * 70)
    print("🎬 EXTENDING YOUR VIDEO")
    print("=" * 70)
    print(f"Source: {video_gcs_path}")
    print(f"Prompt: {extension_prompt}")
    print(f"Output: gs://{GCS_BUCKET}/{GCS_PREFIX}/extended/")
    print()
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        operation_name = data.get("name")
        print(f"✅ Extension started!")
        print(f"Operation: {operation_name.split('/')[-1]}")
        return operation_name
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
        return None


def check_status(operation_name):
    url = f"{BASE_URL}/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/{MODEL_ID}:fetchPredictOperation"
    
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json"
    }
    
    payload = {"operationName": operation_name}
    response = requests.post(url, headers=headers, json=payload)
    
    return response.json() if response.status_code == 200 else None


def wait_for_completion(operation_name):
    print("\n⏳ Waiting for extension to complete...\n")
    start_time = time.time()
    
    while True:
        result = check_status(operation_name)
        
        if not result:
            return None
        
        elapsed = int(time.time() - start_time)
        
        if result.get("done"):
            print(f"\n✅ Completed! (Total time: {elapsed}s)")
            
            if "error" in result:
                print(f"❌ Error: {result['error']}")
                return None
            
            # Extract video path
            videos = result.get("response", {}).get("videos", [])
            if videos:
                video_path = videos[0].get("gcsUri")
                print(f"\n📹 Extended video: {video_path}")
                return video_path
            
            return None
        
        print(f"⏳ Processing... ({elapsed}s elapsed)")
        time.sleep(30)


if __name__ == "__main__":
    print("\n🚀 Extending your existing video...")
    print(f"This will add ~7 seconds to your video.\n")
    
    # Extend the video
    operation = extend_video(EXISTING_VIDEO, EXTENSION_PROMPT, SEED)
    
    if operation:
        extended_path = wait_for_completion(operation)
        
        if extended_path:
            print("\n" + "=" * 70)
            print("✅ SUCCESS!")
            print("=" * 70)
            print(f"Original:  {EXISTING_VIDEO}")
            print(f"Extended:  {extended_path}")
            print(f"\nYou can extend this new video again up to 20 times!")
            print("=" * 70)
        else:
            print("\n❌ Extension failed")
    else:
        print("\n❌ Could not start extension")