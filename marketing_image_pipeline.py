# marketing_image_pipeline.py
"""
Marketing Image Generation Pipeline
Generates 3 different marketing creative variations from a single LLM planning response
"""
import os
import time
import re
import google.generativeai as genai
from PIL import Image
from io import BytesIO
from datetime import datetime
import cloudinary.uploader
import prompt_instruction_templates
import concurrent.futures


def plan_marketing_prompts(user_product_type, user_marketing_copy, user_images, unique_id):
    """
    Generates 3 marketing prompts using the Planner LLM.
    This is a multimodal call that includes the user's images for visual analysis.
    
    Returns:
        str: The full planned prompt text containing all 3 variations
    """
    print(f"--- Step 1: Planning Marketing Prompts (ID: {unique_id}) ---")

    # Build the text portion of the prompt
    prompt_lines = [
        f"Request-ID: {unique_id}",
        user_product_type,
    ]
    
    if user_marketing_copy:
        prompt_lines.append(f"Marketing Image Details:\n{user_marketing_copy}")
    
    prompt_lines.append("")
    prompt_lines.append(prompt_instruction_templates.MARKETING_CREATIVE_INSTRUCTION)
    
    text_prompt = "\n".join(prompt_lines)

    # Combine text and images
    contents = [text_prompt] + user_images

    try:
        planner_model = genai.GenerativeModel('gemini-2.5-pro')
        response = planner_model.generate_content(contents)

        cached_tokens = response.usage_metadata.cached_content_token_count
        print(f"Planner ({unique_id}) - Cached Tokens: {cached_tokens}")
        if cached_tokens > 0:
            print(f"WARNING: Planner ({unique_id}) - CACHE HIT DETECTED!")

        planned_prompt_text = response.text.strip()
        print(f"✓ Successfully planned marketing prompts for '{unique_id}'.")
        
        time.sleep(1)
        return planned_prompt_text
        
    except Exception as e:
        print(f"Error during prompt planning (ID: {unique_id}): {e}")
        raise


def parse_marketing_prompts(planned_prompt_text):
    """
    Parses the LLM response to extract three marketing prompts.
    Expected format: prompt 1: "..." prompt 2: "..." prompt 3: "..."
    
    Returns:
        list: [prompt1_text, prompt2_text, prompt3_text]
    """
    print("--- Parsing Marketing Prompts ---")
    
    # Pattern to match: prompt 1: "..." or prompt 2: "..." (handles multiline)
    pattern = r'prompt\s+(\d+):\s*["\'](.+?)["\'](?=\s*(?:prompt\s+\d+:|$))'
    
    matches = re.findall(pattern, planned_prompt_text, re.DOTALL | re.IGNORECASE)
    
    if len(matches) == 3:
        prompts = [match[1].strip() for match in matches]
        print(f"✓ Successfully parsed {len(prompts)} marketing prompts.")
        for i, prompt in enumerate(prompts, 1):
            print(f"  Prompt {i} length: {len(prompt)} characters")
        return prompts
    else:
        print(f"⚠ WARNING: Expected 3 prompts but found {len(matches)}.")
        print(f"  Raw response excerpt: {planned_prompt_text[:500]}...")
        raise ValueError(f"Failed to parse 3 prompts. Found {len(matches)} prompts instead.")


def execute_image_generation(prompt_text, user_images, unique_id):
    """
    Uses the image generation model to create a single marketing image.
    
    Returns:
        bytes: Generated image bytes
    """
    print(f"--- Executing Image Generation (ID: {unique_id}) ---")
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash-image')
        
        prompt_with_id = f"{prompt_text}\n\nExecution-ID: {unique_id}"
        contents = [prompt_with_id] + user_images
        
        response = model.generate_content(contents)

        cached_tokens = response.usage_metadata.cached_content_token_count
        print(f"Executor ({unique_id}) - Cached Tokens: {cached_tokens}")
        if cached_tokens > 0:
            print(f"WARNING: Executor ({unique_id}) - CACHE HIT DETECTED!")
        
        generated_image_bytes = None
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                image_stream = BytesIO(part.inline_data.data)
                generated_image_bytes = image_stream.getvalue()
                print(f"✓ Successfully extracted generated image bytes for {unique_id}.")
                break

        if generated_image_bytes:
            time.sleep(1)
            return generated_image_bytes
        else:
            print("--- FAILED TO FIND IMAGE DATA IN RESPONSE ---")
            print(f"Full Gemini Response: {response}")
            raise ValueError("No inline_data found in any part of the Gemini response.")

    except Exception as e:
        print(f"Error during image generation (ID: {unique_id}): {e}")
        if 'response' in locals():
            print(f"Full Gemini Response at time of error: {response}")
        raise


def generate_single_marketing_variation(prompt_text, variation_num, user_images, product_type, timestamp_str, pipeline_id):
    """
    Helper function to generate a single marketing variation.
    
    Returns:
        str: Cloudinary URL of the uploaded image
    """
    variation_id = f"{pipeline_id}_var{variation_num}"
    print(f"\n  → Starting Variation {variation_num} (ID: {variation_id})")
    
    try:
        # Generate image
        img_bytes = execute_image_generation(prompt_text, user_images, unique_id=variation_id)
        
        # Upload to Cloudinary
        product_slug = product_type.replace(" ", "-").lower()
        public_id = f"{product_slug}_marketing_var{variation_num}_{timestamp_str}"
        
        upload_result = cloudinary.uploader.upload(
            BytesIO(img_bytes), 
            folder="test_version_2/outputs/marketing", 
            public_id=public_id
        )
        
        url = upload_result['secure_url']
        print(f"  ✓ Variation {variation_num} uploaded successfully")
        print(f"    URL: {url}")
        return url
        
    except Exception as e:
        print(f"  ✗ Variation {variation_num} FAILED: {e}")
        raise


def generate_marketing_images(product_type, marketing_copy, user_images_bytes_list):
    """
    Main entry point for marketing image generation pipeline.
    Generates 3 different marketing creative variations.
    
    Args:
        product_type (str): Product description/type
        marketing_copy (str): Marketing details (brand, headline, CTA, theme, etc.)
        user_images_bytes_list (list): List of image bytes
    
    Returns:
        dict: {
            "success": bool,
            "generated_image_urls": list of 3 URLs,
            "variations": dict with labeled URLs,
            "planned_prompt": str (full planning response),
            "message": str
        }
    """
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    pipeline_id = f"{timestamp_str}_marketing"
    
    print(f"\n{'='*80}")
    print(f"STARTING MARKETING IMAGE GENERATION PIPELINE")
    print(f"Pipeline ID: {pipeline_id}")
    print(f"Product: {product_type}")
    print(f"{'='*80}\n")
    
    try:
        # Convert bytes to PIL Images
        user_images = [Image.open(BytesIO(img_bytes)) for img_bytes in user_images_bytes_list]
        print(f"✓ Loaded {len(user_images)} input image(s)")
        
        # === STEP 1: PLANNING ===
        planned_prompt_text = plan_marketing_prompts(
            user_product_type=product_type,
            user_marketing_copy=marketing_copy,
            user_images=user_images,
            unique_id=pipeline_id
        )
        
        # === STEP 2: PARSING ===
        marketing_prompts = parse_marketing_prompts(planned_prompt_text)
        
        if len(marketing_prompts) != 3:
            raise ValueError(f"Expected 3 prompts, got {len(marketing_prompts)}")
        
        # === STEP 3: CONCURRENT IMAGE GENERATION ===
        print(f"\n--- Generating 3 Marketing Images Concurrently ---")
        
        generated_urls = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = [
                executor.submit(
                    generate_single_marketing_variation,
                    marketing_prompts[i],
                    i + 1,
                    user_images,
                    product_type,
                    timestamp_str,
                    pipeline_id
                )
                for i in range(3)
            ]
            
            for future in concurrent.futures.as_completed(futures):
                url = future.result()
                generated_urls.append(url)
        
        # === STEP 4: SAVE PLANNED PROMPT TO LOG ===
        try:
            with open("generated_prompts_log.txt", "w", encoding="utf-8") as f:
                f.write(f"{'='*80}\n")
                f.write(f"MARKETING IMAGE GENERATION LOG\n")
                f.write(f"Timestamp: {timestamp_str}\n")
                f.write(f"Product: {product_type}\n")
                f.write(f"{'='*80}\n\n")
                f.write(f"FULL PLANNED RESPONSE:\n\n{planned_prompt_text}\n\n")
                f.write(f"{'='*80}\n\n")
                for i, prompt in enumerate(marketing_prompts, 1):
                    f.write(f"--- EXTRACTED PROMPT {i} ---\n{prompt}\n\n")
                    f.write(f"{'-'*80}\n\n")
            print("✓ Successfully wrote prompts to log file.")
        except Exception as e:
            print(f"⚠ Failed to write to log file: {e}")
        
        # === STEP 5: RETURN RESULTS ===
        print(f"\n{'='*80}")
        print(f"✓ PIPELINE COMPLETED SUCCESSFULLY")
        print(f"✓ Generated {len(generated_urls)} marketing images")
        print(f"{'='*80}\n")
        
        return {
            "success": True,
            "generated_image_urls": generated_urls,
            "variations": {
                "geometric_colorful": generated_urls[0] if len(generated_urls) > 0 else None,
                "brand_essence": generated_urls[1] if len(generated_urls) > 1 else None,
                "experimental_dynamic": generated_urls[2] if len(generated_urls) > 2 else None
            },
            "planned_prompt": planned_prompt_text,
            "message": f"Successfully generated 3 marketing image variations."
        }
        
    except Exception as e:
        print(f"\n{'='*80}")
        print(f"✗ PIPELINE FAILED")
        print(f"Error: {e}")
        print(f"{'='*80}\n")
        
        return {
            "success": False,
            "generated_image_urls": [],
            "variations": {},
            "message": f"Failed to generate marketing images: {str(e)}"
        }