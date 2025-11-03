"""
Configuration file for product video generation pipeline
UPDATED: Testing flags and cost controls
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===========================
# Vertex AI Configuration
# ===========================
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
GOOGLE_GENAI_USE_VERTEXAI = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "True")

# Set environment variables for SDK
os.environ["GOOGLE_CLOUD_PROJECT"] = GOOGLE_CLOUD_PROJECT
os.environ["GOOGLE_CLOUD_LOCATION"] = GOOGLE_CLOUD_LOCATION
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = GOOGLE_GENAI_USE_VERTEXAI

# Optional: Service account credentials
if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# ===========================
# UNSPLASH API (for testing)
# ===========================
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "")
UNSPLASH_SECRET_KEY = os.getenv("UNSPLASH_SECRET_KEY", "")

TEST_IMAGES_FOLDER = "test_images_edit_pipeline"
TEST_OUTPUTS_FOLDER = "test_outputs_edit_pipeline"
# Testing configuration
USE_UNSPLASH_FALLBACK = True 

# ===========================
# GCS Configuration
# ===========================
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
GCS_OUTPUT_PREFIX = "veo-product-videos"

# ===========================
# Model Configuration
# ===========================
TEXT_MODEL = "gemini-2.5-pro"
VIDEO_MODEL = "veo-3.1-generate-preview"

# ===========================
# TESTING & COST CONTROL FLAGS for video
# ===========================

# NOTE: Temp files are ALWAYS deleted for deployment (ignoring this flag for cleanup)
TESTING_MODE = True  # Set to False for production deployment

ENABLE_PROMPT_VIEW = True  # Allow frontend to view generated prompts
PROMPT_DISPLAY_FILE = "veo_generated_prompts_vertex.json"  # File to read prompts from

PROMPT_ONLY_MODE = True  # Set to True to skip video generation (just test prompts)
SAVE_PROMPTS_TO_FILE = True  # Save generated prompts to JSON

GENERATE_AUDIO = False  # Disable audio to save credits
USE_LOWER_RESOLUTION = True  # Set to True for "720p" (saves ~30% credits)

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===========================
# Vertex AI Configuration
# ===========================
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
GOOGLE_GENAI_USE_VERTEXAI = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "True")

# Set environment variables for SDK
os.environ["GOOGLE_CLOUD_PROJECT"] = GOOGLE_CLOUD_PROJECT
os.environ["GOOGLE_CLOUD_LOCATION"] = GOOGLE_CLOUD_LOCATION
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = GOOGLE_GENAI_USE_VERTEXAI

# Optional: Service account credentials
if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# ===========================
# UNSPLASH API (for testing)
# ===========================
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "")
UNSPLASH_SECRET_KEY = os.getenv("UNSPLASH_SECRET_KEY", "")

TEST_IMAGES_FOLDER = "test_images_edit_pipeline"
TEST_OUTPUTS_FOLDER = "test_outputs_edit_pipeline"
# Testing configuration
USE_UNSPLASH_FALLBACK = True 

# ===========================
# GCS Configuration
# ===========================
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
GCS_OUTPUT_PREFIX = "veo-product-videos"

# GCS Folder Structure
GCS_SEGMENTS_FOLDER = "segments"
GCS_FINAL_FOLDER = "final"
GCS_INPUTS_FOLDER = "inputs"

# ========================================
# DEBUG SETTINGS
# ========================================

# Show full request payloads in logs
DEBUG_MODE = True  # Set to False in production

# ===========================
# Model Configuration
# ===========================
TEXT_MODEL = "gemini-2.5-pro"  # For prompt generation
VIDEO_MODEL = "veo-3.1-generate-preview"  # Veo 3.1
VIDEO_MODEL_NAME = "veo-3.1-generate-preview" 
VIDEO_MODEL_ENDPOINT = f"projects/{GOOGLE_CLOUD_PROJECT}/locations/{GOOGLE_CLOUD_LOCATION}/publishers/google/models/{VIDEO_MODEL}"

# ===========================
# TESTING & COST CONTROL FLAGS for video
# ===========================

# NOTE: Temp files are ALWAYS deleted for deployment (ignoring this flag for cleanup)
TESTING_MODE = True  # Set to False for production deployment

ENABLE_PROMPT_VIEW = True  # Allow frontend to view generated prompts
PROMPT_DISPLAY_FILE = "veo_generated_prompts_vertex.json"  # File to read prompts from

PROMPT_ONLY_MODE = True  # Set to True to skip video generation (just test prompts)
SAVE_PROMPTS_TO_FILE = True  # Save generated prompts to JSON

#PROMPT_FORMAT_MODE = "inline_timestamps"  # Change to "full_json" to test Option B
PROMPT_FORMAT_MODE = "full_json"

GENERATE_AUDIO = False  # Disable audio to save credits
USE_LOWER_RESOLUTION = True  # Set to True for "720p" (saves ~30% credits)

# ===========================
# Video Configuration
# ===========================
# Cost-optimized durations
DEFAULT_TOTAL_DURATION = 16  # Reduced from 40s (60% cost savings)
DEFAULT_SEGMENT_DURATION = 8  # 2 segments instead of 5

# ===========================
# Video Generation Limits
# ===========================
MAX_IMAGES = 3
MIN_SEGMENT_DURATION = 4
MAX_SEGMENT_DURATION = 8

# ===========================
# Video Quality Settings
# ===========================
VIDEO_ASPECT_RATIO = "16:9"
VIDEO_RESOLUTION = "720p" if USE_LOWER_RESOLUTION else "1080p"
VIDEO_FPS = 24
VIDEO_CODEC = "libx264"
VIDEO_PRESET = "medium"

# Veo Generation Parameters
VEO_SEED = None  # Set to integer for reproducible results, None for random
VEO_SAMPLE_COUNT = 1  # Number of videos to generate per prompt
VEO_PERSON_GENERATION = "disallow"  # "allow_adult" or "disallow"

# ===========================
# Retry Configuration
# ===========================
MAX_RETRIES = 3
RETRY_DELAY = 10  # seconds between retries
OPERATION_POLL_INTERVAL = 30  # seconds between status checks
OPERATION_TIMEOUT = 600  # 10 minutes max per operation

# ===========================
# E-Commerce Video Rules
# ===========================
ALLOW_PEOPLE_IN_VIDEO = False
PRODUCT_OPERATION_MODE = False
COMMERCIAL_STYLE_ONLY = True

# ===========================
# Video Merging Configuration
# ===========================
CROSSFADE_DURATION = 0.5  # seconds for crossfade transition
TEMP_VIDEO_FOLDER = "temp_videos"  # Local temp storage for segments

# ===========================
# Logging Configuration
# ===========================
LOG_FOLDER = "logs"
PROMPT_LOG_FILE = os.path.join(LOG_FOLDER, "generated_prompts_log.txt")
VEO_LOG_FILE = os.path.join(LOG_FOLDER, "veo_generation_log.txt")
PIPELINE_LOG_FILE = os.path.join(LOG_FOLDER, "pipeline_log.txt")

# Create necessary directories
os.makedirs(LOG_FOLDER, exist_ok=True)
os.makedirs(TEMP_VIDEO_FOLDER, exist_ok=True)
os.makedirs(TEST_IMAGES_FOLDER, exist_ok=True)
os.makedirs(TEST_OUTPUTS_FOLDER, exist_ok=True)

# ===========================
# Template Configuration
# ===========================
TEMPLATE_FOLDER = "templates"
VEO_INSTRUCTION_TEMPLATE = os.path.join(TEMPLATE_FOLDER, "veo_instruction_template.txt")

# Create template directory
os.makedirs(TEMPLATE_FOLDER, exist_ok=True)

# ===========================
# Validation
# ===========================
def validate_config():
    """Validate that all required configuration is present"""
    required_vars = [
        ("GOOGLE_CLOUD_PROJECT", GOOGLE_CLOUD_PROJECT),
        ("GCS_BUCKET_NAME", GCS_BUCKET_NAME),
    ]
    
    missing = [var_name for var_name, var_value in required_vars if not var_value]
    
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
    
    print("✅ Configuration validated successfully")
    print(f"   Project: {GOOGLE_CLOUD_PROJECT}")
    print(f"   Location: {GOOGLE_CLOUD_LOCATION}")
    print(f"   Bucket: {GCS_BUCKET_NAME}")
    print(f"   Video Model: {VIDEO_MODEL}")
    print(f"   Resolution: {VIDEO_RESOLUTION}")
    print(f"   Audio: {'Enabled' if GENERATE_AUDIO else 'Disabled'}")
    print(f"   Prompt Only Mode: {'Yes' if PROMPT_ONLY_MODE else 'No'}")

if __name__ == "__main__":
    validate_config()
"""
--------------------------------> version 1 <-----------------------------
# Veo 3.1 Prompt Limits
MAX_PROMPT_LENGTH = 500  # Concise prompts work better
OPTIMAL_PROMPT_LENGTH = 400  # Target length

# ===========================
# VIDEO EXTENSION SETTINGS (VEO 3.1)
# ===========================
ENABLE_VIDEO_EXTENSION = True  # Set True to use cumulative video extension

# Extension parameters (only used if ENABLE_VIDEO_EXTENSION = True)
EXTENSION_BASE_DURATION = 8  # Initial video length in seconds
EXTENSION_INCREMENT = 7   # Each extension adds 7 seconds (Veo 3.1 limit)
EXTENSION_COUNT = 1      # Number of times to extend (max 20 per docs = 148s total)

# Model selection for extension
# NOTE: Reddit user tested with "veo-3.1-fast-generate-preview"
# You want to use "veo-3.1-generate-preview" (non-fast)
# If extension fails, try enabling this flag to use fast model
USE_FAST_MODEL_FOR_EXTENSION = False  

def get_extension_model():
    if ENABLE_VIDEO_EXTENSION and USE_FAST_MODEL_FOR_EXTENSION:
        return "veo-3.1-fast-generate-preview"
    return VIDEO_MODEL  # Uses your default veo-3.1-generate-preview

def get_effective_duration():
    if ENABLE_VIDEO_EXTENSION:
        total = EXTENSION_BASE_DURATION + (EXTENSION_INCREMENT * EXTENSION_COUNT)
        print(f"📏 Extension mode: {EXTENSION_BASE_DURATION}s base + {EXTENSION_COUNT} extensions = {total}s total")
        return total
    return DEFAULT_TOTAL_DURATION

# Validation
if ENABLE_VIDEO_EXTENSION:
    if EXTENSION_COUNT < 1 or EXTENSION_COUNT > 20:
        raise ValueError("EXTENSION_COUNT must be 1-20 (Veo limit)")
    
    max_total = EXTENSION_BASE_DURATION + (EXTENSION_INCREMENT * EXTENSION_COUNT)
    if max_total > 148:
        raise ValueError(f"Total duration {max_total}s exceeds Veo 3.1 limit of 148s")

# ===========================
# Cost Tracking (Optional)
# ===========================
# Approximate Veo 3.1 costs
COST_PER_SECOND_1080P = 0.10  # $0.10 per second
COST_PER_SECOND_720P = 0.07   # $0.07 per second

def estimate_generation_cost():
    resolution_cost = COST_PER_SECOND_720P if USE_LOWER_RESOLUTION else COST_PER_SECOND_1080P
    total_cost = DEFAULT_TOTAL_DURATION * resolution_cost
    
    print(f"\n💰 ESTIMATED COST:")
    print(f"   Duration: {DEFAULT_TOTAL_DURATION}s")
    print(f"   Resolution: {VIDEO_RESOLUTION}")
    print(f"   Audio: {'Yes' if GENERATE_AUDIO else 'No (savings!)'}")
    print(f"   Estimated: ${total_cost:.2f} per video")
    print(f"   (Actual cost may vary)\n")
    
    return total_cost"""