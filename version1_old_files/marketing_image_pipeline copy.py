# image_pipeline.py
"""
Image Generation Pipeline - Extracted from app.py for modularity
Handles solid background, lifestyle, and marketing creative image generation
"""
import os
import time
import google.generativeai as genai
from PIL import Image
from io import BytesIO
from datetime import datetime
import cloudinary.uploader
import prompt_instruction_templates


def plan_prompt(instruction_template, user_product_type, unique_id, user_images, user_guidelines=None, user_marketing_copy=None):
    """
    Generates the meta-prompt for the Planner LLM. This is now a multimodal call
    that includes the user's images for an accurate visual analysis.
    """
    print(f"--- Step 1: Planning Prompt (ID: {unique_id}) ---")

    # This is the text portion of our prompt.
    prompt_lines = [
        f"Request-ID: {unique_id}",
        user_product_type,
    ]
    if user_guidelines:
        prompt_lines.append(user_guidelines)
    if user_marketing_copy:
        prompt_lines.append(user_marketing_copy)
    prompt_lines.append("")
    prompt_lines.append(instruction_template)
    text_prompt = "\n".join(prompt_lines)

    # The contents now include both the text instructions AND the images
    contents = [text_prompt] + user_images

    try:
        planner_model = genai.GenerativeModel('gemini-2.5-pro')
        response = planner_model.generate_content(contents)

        cached_tokens = response.usage_metadata.cached_content_token_count
        print(f"Planner ({unique_id}) - Cached Tokens: {cached_tokens}")
        if cached_tokens > 0:
            print(f"WARNING: Planner ({unique_id}) - CACHE HIT DETECTED!")

        planned_prompt_text = response.text.strip()
        print(f"Successfully planned prompt for '{unique_id}'.")
        
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
    import re
    
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
        print(f"  Falling back to single prompt strategy.")
        # Fallback: return the entire text as a single prompt
        return [planned_prompt_text]

def execute_generation(planned_prompt, user_images, unique_id):
    """
    Uses the image generation model with the high-quality, visually-aware prompt.
    """
    print(f"--- Step 2: Executing Image Generation (ID: {unique_id}) ---")
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash-image')
        
        prompt_with_id = f"{planned_prompt}\n\nExecution-ID: {unique_id}"
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
                print("Successfully extracted generated image bytes.")
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

def run_generation_pipeline(job_type, user_product_type, user_guidelines, user_marketing_copy, user_images_bytes, timestamp_str):
    """
    Orchestrates a single, isolated generation pipeline from planning to execution.
    For 'marketing_creative', generates THREE images from three different prompts.
    For other job types, generates a single image.
    """
    pipeline_unique_id = f"{timestamp_str}_{job_type}"
    print(f"\n--- Starting Generation Pipeline for Job: {job_type.upper()} (ID: {pipeline_unique_id}) ---")
    
    planned_prompt = None
    try:
        user_images = [Image.open(BytesIO(img_bytes)) for img_bytes in user_images_bytes]

        common_args = {
            "user_product_type": user_product_type,
            "unique_id": pipeline_unique_id,
            "user_images": user_images
        }

        # === PLANNING PHASE ===
        if job_type == 'solid_background':
            instruction = prompt_instruction_templates.SOLID_BACKGROUND_INSTRUCTION
            planned_prompt = plan_prompt(instruction, **common_args)
            
        elif job_type == 'lifestyle':
            instruction = prompt_instruction_templates.LIFESTYLE_INSTRUCTION
            planned_prompt = plan_prompt(instruction, user_guidelines=user_guidelines, **common_args)
            
        elif job_type == 'marketing_creative':
            instruction = prompt_instruction_templates.MARKETING_CREATIVE_INSTRUCTION
            planned_prompt = plan_prompt(instruction, user_marketing_copy=user_marketing_copy, **common_args)
        
        
        # === EXECUTION PHASE ===
        if job_type == 'marketing_creative':
            # Parse the 3 prompts
            marketing_prompts = parse_marketing_prompts(planned_prompt)
            
            if len(marketing_prompts) == 3:
                print(f"--- Generating 3 Marketing Images Concurrently (ID: {pipeline_unique_id}) ---")
                
                # Execute 3 image generations concurrently
                import concurrent.futures
                
                generated_urls = []
                
                def generate_single_marketing_image(prompt_text, variation_num):
                    """Helper function to generate a single marketing variation"""
                    variation_id = f"{pipeline_unique_id}_var{variation_num}"
                    print(f"  → Starting variation {variation_num} (ID: {variation_id})")
                    
                    img_bytes = execute_generation(prompt_text, user_images, unique_id=variation_id)
                    
                    # Upload to Cloudinary
                    product_slug = user_product_type.replace(" ", "-").lower()
                    public_id = f"{product_slug}_marketing_var{variation_num}_{timestamp_str}"
                    
                    upload_result = cloudinary.uploader.upload(
                        BytesIO(img_bytes), 
                        folder="test_version_2/outputs", 
                        public_id=public_id
                    )
                    
                    url = upload_result['secure_url']
                    print(f"  ✓ Variation {variation_num} uploaded: {url}")
                    return url
                
                # Generate all 3 images concurrently
                with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                    futures = [
                        executor.submit(generate_single_marketing_image, marketing_prompts[i], i+1)
                        for i in range(3)
                    ]
                    
                    for future in concurrent.futures.as_completed(futures):
                        url = future.result()
                        generated_urls.append(url)
                
                print(f"✓ Successfully generated {len(generated_urls)} marketing images.")
                
                # Return all 3 URLs and the planned prompt
                return (generated_urls, planned_prompt)
            
            else:
                # Fallback: single image generation
                print("⚠ Falling back to single marketing image generation.")
                generated_image_bytes = execute_generation(planned_prompt, user_images, unique_id=pipeline_unique_id)
                
                product_slug = user_product_type.replace(" ", "-").lower()
                public_id = f"{product_slug}_{job_type}_{timestamp_str}"
                
                upload_result = cloudinary.uploader.upload(
                    BytesIO(generated_image_bytes), 
                    folder="test_version_2/outputs", 
                    public_id=public_id
                )
                final_url = upload_result['secure_url']
                print(f"Successfully uploaded. Final URL: {final_url}")
                
                return ([final_url], planned_prompt)
        
        else:
            # === STANDARD SINGLE IMAGE GENERATION (for solid_background & lifestyle) ===
            generated_image_bytes = execute_generation(planned_prompt, user_images, unique_id=pipeline_unique_id)
            
            print(f"Uploading final '{job_type}' image to Cloudinary...")
            product_slug = user_product_type.replace(" ", "-").lower()
            public_id = f"{product_slug}_{job_type}_{timestamp_str}"
            
            upload_result = cloudinary.uploader.upload(
                BytesIO(generated_image_bytes), 
                folder="test_version_2/outputs", 
                public_id=public_id
            )
            final_url = upload_result['secure_url']
            print(f"Successfully uploaded. Final URL: {final_url}")
            
            return ([final_url], planned_prompt)

    except Exception as e:
        print(f"--- Pipeline for Job '{job_type.upper()}' FAILED (ID: {pipeline_unique_id}) ---")
        print(f"REASON: {e}") 
        return ([], planned_prompt)

def generate_images(product_type, guidelines, marketing_copy, user_images_bytes_list):
    """
    Main entry point for image generation pipeline.
    Runs three generation pipelines in parallel.
    
    Returns:
        dict: {
            "success": bool,
            "generated_image_urls": list,
            "prompts": list (optional)
        }
    """
    import concurrent.futures
    
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    job_types = ['solid_background', 'lifestyle', 'marketing_creative']
    job_args = [
        (job_type, product_type, guidelines, marketing_copy, user_images_bytes_list, timestamp_str)
        for job_type in job_types
    ]
        
    print(f"--- Preparing to run {len(job_types)} pipelines in parallel (Request ID: {timestamp_str}) ---")
    
    generated_urls, logged_prompts = [], []
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_generation_pipeline, *args) for args in job_args]
        
        for future in concurrent.futures.as_completed(futures):
            result_urls, planned_prompt = future.result()
            
            # result_urls is now a LIST (can be 1 URL or 3 URLs)
            if result_urls:
                generated_urls.extend(result_urls)  # Use extend instead of append
            
            if planned_prompt: 
                logged_prompts.append(planned_prompt)
    
    # Save prompts to log file
    if logged_prompts:
        try:
            with open("generated_prompts_log.txt", "w", encoding="utf-8") as f:
                f.write(f"--- LOG FOR GENERATION REQUEST {timestamp_str} ---\n\n")
                for i, prompt_text in enumerate(logged_prompts):
                    f.write(f"--- PROMPT {i+1} ---\n{prompt_text}\n\n---------------------------------------\n\n")
            print("Successfully wrote generated prompts to log file.")
        except Exception as e:
            print(f"Failed to write to log file: {e}")
    
    print(f"--- All pipelines finished. Successfully generated {len(generated_urls)} images. ---")
    
    return {
        "success": len(generated_urls) > 0,
        "generated_image_urls": generated_urls,
        "message": f"Successfully generated {len(generated_urls)} images."
    }