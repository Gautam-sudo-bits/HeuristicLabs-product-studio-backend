"""
Generate video prompts using Gemini 2.5 Pro
Creates segment-wise prompts with timestamps for Veo video generation
"""

import json
import os
from datetime import datetime
from google import genai
from google.genai import types
import config


# Initialize Gemini client
client = genai.Client(
    vertexai=True,
    project=config.GOOGLE_CLOUD_PROJECT,
    location=config.GOOGLE_CLOUD_LOCATION
)


def load_instruction_template():
    """
    Load the instruction template for prompt generation
    
    Returns:
        str: Template content
    """
    if not os.path.exists(config.VEO_INSTRUCTION_TEMPLATE):
        raise FileNotFoundError(
            f"Instruction template not found: {config.VEO_INSTRUCTION_TEMPLATE}"
        )
    
    with open(config.VEO_INSTRUCTION_TEMPLATE, 'r', encoding='utf-8') as f:
        return f.read()


def generate_prompts_with_gemini(
    user_requirements,
    reference_image_paths=None,
    total_duration=None,
    segment_duration=None
):
    """
    Generate video prompts using Gemini 2.5 Pro
    
    Args:
        user_requirements: User's description/requirements for the video
        reference_image_paths: List of local paths to reference images (max 3)
        total_duration: Total video duration in seconds
        segment_duration: Duration of each segment in seconds
    
    Returns:
        dict: Generated prompts in structured format
    """
    if total_duration is None:
        total_duration = config.DEFAULT_TOTAL_DURATION
    
    if segment_duration is None:
        segment_duration = config.DEFAULT_SEGMENT_DURATION
    
    # Load instruction template
    instruction_template = load_instruction_template()
    
    # Build the prompt for Gemini
    system_prompt = instruction_template.format(
        total_duration=total_duration,
        segment_duration=segment_duration,
        max_images=config.MAX_IMAGES
    )
    
    user_prompt = f"""User Requirements/Product specification:
{user_requirements}

Total Video Duration: {total_duration} seconds
Segment Duration: {segment_duration} seconds each
Keep the style professional and commercial, suitable for e-commerce.
Please generate detailed Veo prompts for each segment following the instruction template."""
    
    print(f"\n🤖 Generating prompts with {config.TEXT_MODEL}...")
    print(f"   Total duration: {total_duration}s")
    print(f"   Segment duration: {segment_duration}s")
    print(f"   Reference images: {len(reference_image_paths) if reference_image_paths else 0}")
    
    try:
        # Prepare content parts (your original pattern)
        content_parts = [user_prompt]  # String is fine for text
        
        # Add reference images if provided
        if reference_image_paths:
            for img_path in reference_image_paths[:config.MAX_IMAGES]:
                if os.path.exists(img_path):
                    with open(img_path, 'rb') as f:
                        image_data = f.read()
                    
                    # Determine MIME type
                    mime_type = "image/jpeg" if img_path.lower().endswith(('.jpg', '.jpeg')) else "image/png"
                    
                    # Use from_bytes (your original working method)
                    content_parts.append(
                        types.Part.from_bytes(
                            data=image_data,
                            mime_type=mime_type
                        )
                    )
                    print(f"   ✓ Added reference image: {os.path.basename(img_path)}")
        
        # Generate content (your original pattern)
        response = client.models.generate_content(
            model=config.TEXT_MODEL,
            contents=content_parts,  # Pass list directly
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=1,
                response_mime_type="application/json"
            )
        )
        
        # Parse JSON response
        response_text = response.text
        prompts_json = json.loads(response_text)
        
        print(f"✅ Prompts generated successfully")
        
        return prompts_json
        
    except Exception as e:
        print(f"❌ Error generating prompts: {e}")
        raise

def extract_segment_prompts(prompts_json):
    """
    Extract individual segment prompts from the JSON structure
    Supports multiple formatting modes via config.PROMPT_FORMAT_MODE
    
    Args:
        prompts_json: JSON object from Gemini
    
    Returns:
        list: List of tuples (segment_number, formatted_prompt_string)
    """
    segments = []
    
    # Iterate through segments
    for segment_key in sorted(prompts_json.keys()):
        if not segment_key.startswith('segment_'):
            continue
        
        segment_data = prompts_json[segment_key]
        segment_number = int(segment_key.split('_')[1])
        
        # ============================================================
        # MODE SELECTION: Choose formatting based on config
        # ============================================================
        
        if config.PROMPT_FORMAT_MODE == "full_json":
            # OPTION B: Send entire segment JSON as-is
            full_prompt = _format_full_json(segment_data, segment_number)
        
        elif config.PROMPT_FORMAT_MODE == "inline_timestamps":
            # OPTION C: Inline timestamps with temporal connectors
            full_prompt = _format_inline_timestamps(segment_data, segment_number)
        
        else:
            # Fallback to inline if invalid mode
            print(f"⚠️ Unknown PROMPT_FORMAT_MODE: {config.PROMPT_FORMAT_MODE}, using 'inline_timestamps'")
            full_prompt = _format_inline_timestamps(segment_data, segment_number)
        
        segments.append((segment_number, full_prompt))
        
        # Log segment info
        char_count = len(full_prompt)
        timestamp_count = len([k for k in segment_data.keys() if k.startswith('timestamp') and not k.endswith('_prompt')])
        print(f"   Segment {segment_number}: {char_count} chars, {timestamp_count} scene beats, mode={config.PROMPT_FORMAT_MODE}")
    
    return segments


def _format_full_json(segment_data, segment_number):
    """
    OPTION B: Format segment as complete JSON structure
    Preserves all nested objects, arrays, and formatting
    Veo receives the raw JSON structure as a string
    
    Args:
        segment_data: The segment dictionary from LLM
        segment_number: Segment number for logging
    
    Returns:
        str: JSON string of the entire segment
    """
    # Convert entire segment dict to pretty-printed JSON string
    json_string = json.dumps(segment_data, indent=2, ensure_ascii=False)
    
    print(f"   → Mode B: Sending full JSON structure to Veo")
    
    return json_string


def _format_inline_timestamps(segment_data, segment_number):
    """
    OPTION C: Format with inline timestamp markers
    Creates a temporal narrative: [00:00-00:03] action, followed by [00:03-00:06] action
    
    Args:
        segment_data: The segment dictionary from LLM
        segment_number: Segment number for logging
    
    Returns:
        str: Temporally-structured prompt string
    """
    # Extract timestamps and prompts in order
    timestamp_entries = []
    
    # Get all timestamp keys (timestamp1, timestamp2, etc.)
    timestamp_keys = sorted([k for k in segment_data.keys() if k.startswith('timestamp') and not k.endswith('_prompt')])
    
    for ts_key in timestamp_keys:
        time_range = segment_data.get(ts_key, "")
        prompt_key = f"{ts_key}_prompt"
        prompt_text = segment_data.get(prompt_key, "")
        
        if prompt_text:
            # Format: [00:00-00:03] Prompt text
            timestamp_entries.append(f"[{time_range}] {prompt_text}")
    
    # Join with natural temporal connectors
    if len(timestamp_entries) > 1:
        full_prompt = ", followed by ".join(timestamp_entries)
    elif len(timestamp_entries) == 1:
        full_prompt = timestamp_entries[0]
    else:
        # Fallback: concatenate all prompt values
        full_prompt = ". ".join([v for k, v in segment_data.items() if 'prompt' in k.lower() and isinstance(v, str)])
    
    print(f"   → Mode C: Inline timestamps with {len(timestamp_entries)} beats")
    
    return full_prompt

def save_prompts_to_file(prompts_json, filepath=None):
    """
    Save generated prompts to JSON file for review
    
    Args:
        prompts_json: Prompts JSON object
        filepath: Optional custom filepath
    """
    if filepath is None:
        filepath = config.PROMPT_DISPLAY_FILE
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    output = {
        "generated_at": timestamp,
        "model": config.TEXT_MODEL,
        "prompts": prompts_json
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Prompts saved to: {filepath}")


def log_prompts_to_text(prompts_json, user_requirements):
    """
    Log prompts to text file for audit trail
    
    Args:
        prompts_json: Prompts JSON object
        user_requirements: Original user requirements
    """
    os.makedirs(config.LOG_FOLDER, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(config.PROMPT_LOG_FILE, 'a', encoding='utf-8') as f:
        f.write("\n" + "=" * 80 + "\n")
        f.write(f"Generated at: {timestamp}\n")
        f.write(f"Model: {config.TEXT_MODEL}\n")
        f.write(f"Prompt Format Mode: {config.PROMPT_FORMAT_MODE}\n")  # ← NEW
        f.write("=" * 80 + "\n\n")
        
        f.write("USER REQUIREMENTS:\n")
        f.write(f"{user_requirements}\n\n")
        
        f.write("GENERATED PROMPTS (Raw JSON from LLM):\n")
        f.write(json.dumps(prompts_json, indent=2, ensure_ascii=False))
        f.write("\n\n")
        
        # Extract and format segment prompts
        segments = extract_segment_prompts(prompts_json)
        f.write("SEGMENT PROMPTS (Formatted for Veo):\n")
        f.write(f"Mode: {config.PROMPT_FORMAT_MODE}\n")  # ← NEW
        f.write("-" * 80 + "\n")
        for seg_num, prompt in segments:
            f.write(f"\nSegment {seg_num}:\n")
            f.write(f"{prompt}\n")
            f.write("-" * 80 + "\n")
    
    print(f"✅ Prompts logged to: {config.PROMPT_LOG_FILE}")

def generate_and_process_prompts(
    user_requirements,
    reference_image_paths=None,
    total_duration=None,
    segment_duration=None
):
    """
    Main function to generate prompts and handle all processing
    
    Args:
        user_requirements: User's video requirements
        reference_image_paths: List of reference image paths
        total_duration: Total video duration
        segment_duration: Segment duration
    
    Returns:
        tuple: (prompts_json, segment_prompts_list)
    """
    # Generate prompts
    prompts_json = generate_prompts_with_gemini(
        user_requirements=user_requirements,
        reference_image_paths=reference_image_paths,
        total_duration=total_duration,
        segment_duration=segment_duration
    )
    
    # Extract segment prompts
    segment_prompts = extract_segment_prompts(prompts_json)
    
    print(f"\n📋 Extracted {len(segment_prompts)} segment prompt(s)")
    
    # Save to file if enabled
    if config.SAVE_PROMPTS_TO_FILE:
        save_prompts_to_file(prompts_json)
    
    # Log to text file
    log_prompts_to_text(prompts_json, user_requirements)
    
    return prompts_json, segment_prompts


if __name__ == "__main__":
    # Test prompt generation
    print("Testing prompt generation...")
    config.validate_config()
    
    # Sample user requirements
    test_requirements = """
    Create a premium product video for a sleek wireless earbud.
    Show the product rotating on a minimalist platform with studio lighting.
    Highlight the metallic finish, LED indicators, and touch controls.
    Keep the style professional and commercial, suitable for e-commerce.
    """
    
    try:
        prompts_json, segment_prompts = generate_and_process_prompts(
            user_requirements=test_requirements,
            total_duration=16,
            segment_duration=8
        )
        
        print("\n✅ Test successful!")
        print(f"Generated {len(segment_prompts)} segments")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")