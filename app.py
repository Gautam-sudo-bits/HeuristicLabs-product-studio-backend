# app.py (Clean endpoint architecture)
import os
import json
from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import google.generativeai as genai
import cloudinary
from pathlib import Path
import tempfile

# Import pipelines
#from marketing_image_pipeline import generate_images
#from video_pipeline import generate_product_video
from marketing_image_pipeline import generate_marketing_images
from config import ENABLE_PROMPT_VIEW, PROMPT_DISPLAY_FILE

load_dotenv()
app = Flask(__name__)
CORS(app)

# --- Configuration ---
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#Port = os.getenv("PORT")
@app.route('/api/generate', methods=['POST'])
def generate_marketing_images_endpoint():
    """
    Endpoint to generate 3 marketing creative image variations
    """
    try:
        # Extract form data
        product_type = request.form.get('product_type')
        marketing_copy = request.form.get('marketing_copy')
        
        # Extract uploaded images
        uploaded_files = request.files.getlist('images')
        
        if not uploaded_files:
            return jsonify({"error": "No images provided"}), 400
        
        if not product_type:
            return jsonify({"error": "Product type is required"}), 400
        
        # Convert uploaded files to bytes
        user_images_bytes = []
        for file in uploaded_files:
            img_bytes = file.read()
            user_images_bytes.append(img_bytes)
        
        print(f"Received request: Product={product_type}, Images={len(user_images_bytes)}")
        
        # Generate marketing images
        result = generate_marketing_images(
            product_type=product_type,
            marketing_copy=marketing_copy,
            user_images_bytes_list=user_images_bytes
        )
        
        return jsonify(result), 200 if result["success"] else 500
        
    except Exception as e:
        print(f"Error in endpoint: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/generate-video', methods=['POST'])
def generate_video_endpoint():
    """
    Video generation endpoint - calls ad_pipeline module
    """
    temp_dir = None
    try:
        # Get uploaded images
        image_files = request.files.getlist('images')
        if not image_files:
            return jsonify({"error": "At least one product image is required."}), 400
        
        # Get text inputs
        product_overview = request.form.get('product_overview', '')
        brand_guidelines = request.form.get('brand_guidelines', '')
        
        if not product_overview:
            return jsonify({"error": "Product overview is required."}), 400
        
        # Save uploaded images temporarily
        import tempfile
        temp_dir = tempfile.mkdtemp(prefix='product_images_')
        image_paths = []
        
        for i, img_file in enumerate(image_files):
            temp_path = os.path.join(temp_dir, f"product_image_{i}.png")
            img_file.save(temp_path)
            image_paths.append(temp_path)
        
        print(f"Saved {len(image_paths)} images to temporary directory: {temp_dir}")
        
        # Call video generation pipeline
        result = generate_product_video(
            image_paths=image_paths,
            product_overview=product_overview,
            brand_guidelines=brand_guidelines
        )
        
        if result["success"]:
            response_data = {
                "status": "success",
                "video_url": result.get("final_video_url"),
                "request_id": result.get("request_id"),
                "duration": result.get("duration"),
                "segment_count": result.get("segment_count")
            }
            
            # Include prompt data if available
            if ENABLE_PROMPT_VIEW and result.get("mode") != "prompt_only":
                response_data["prompt_available"] = True
            
            return jsonify(response_data)
        else:
            return jsonify({"error": result.get("error", "Video generation failed")}), 500
            
    except Exception as e:
        print(f"Error in video generation endpoint: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    
    finally:
        # CRITICAL: Always cleanup temp directory
        if temp_dir and os.path.exists(temp_dir):
            import shutil
            shutil.rmtree(temp_dir, ignore_errors=True)
            print(f"🗑️ Cleaned up temp directory: {temp_dir}")

@app.route('/api/edit-image', methods=['POST'])
def edit_image_endpoint():
    """
    Image edit endpoint - accepts operation_id instead of free text
    UPDATED: Now supports multiple images
    """
    try:
        # Get uploaded images (can be single or multiple)
        image_files = request.files.getlist('images')
        
        # Fallback to single 'image' for backward compatibility
        if not image_files:
            single_image = request.files.get('image')
            if single_image:
                image_files = [single_image]
        
        # Validate at least one image
        if not image_files or len(image_files) == 0:
            return jsonify({"error": "At least one image file is required"}), 400
        
        # Validate files are not empty
        valid_images = [img for img in image_files if img.filename != '']
        if len(valid_images) == 0:
            return jsonify({"error": "No valid images selected"}), 400
        
        # Get operation_id (required)
        operation_id = request.form.get('operation_id', '').strip()
        if not operation_id:
            return jsonify({
                "error": "operation_id is required. Select an operation from the dropdown."
            }), 400
        
        # Validate operation_id
        try:
            operation_id = int(operation_id)
            if operation_id < 1 or operation_id > 39:
                raise ValueError("Invalid range")
        except ValueError:
            return jsonify({
                "error": f"Invalid operation_id: {operation_id}. Must be 1-38."
            }), 400
        
        # Get optional operation details
        operation_details = request.form.get('operation_details', '').strip()
        
        print(f"\n{'='*70}")
        print(f"📥 EDIT IMAGE REQUEST")
        print(f"{'='*70}")
        print(f"🆔 Operation ID: {operation_id}")
        print(f"📸 Images: {len(valid_images)}")
        if operation_details:
            print(f"📝 User Details: {operation_details[:100]}...")
        print(f"{'='*70}\n")
        
        # Import edit pipeline
        from image_edit_pipeline import edit_product_image
        
        # Process images
        edited_urls = []
        operation_name = None
        
        for idx, image_file in enumerate(valid_images):
            print(f"\n🖼️ Processing image {idx + 1}/{len(valid_images)}: {image_file.filename}")
            
            # Read image bytes
            image_bytes = image_file.read()
            
            # Process single image
            result = edit_product_image(
                image_bytes=image_bytes,
                operation_id=operation_id,
                operation_details=operation_details if operation_details else None
            )
            
            if result["success"]:
                edited_urls.append(result["edited_image_url"])
                if operation_name is None:
                    operation_name = result["operation_name"]
                print(f"   ✅ Edited: {result['edited_image_url']}")
            else:
                print(f"   ❌ Failed: {result.get('error', 'Unknown error')}")
                # Continue with other images even if one fails
        
        # Check if at least one succeeded
        if len(edited_urls) > 0:
            response_data = {
                "status": "success",
                "operation_name": operation_name,
                "total_images": len(valid_images),
                "successful_edits": len(edited_urls)
            }
            
            # Return single URL or array based on count
            if len(edited_urls) == 1:
                response_data["edited_image_url"] = edited_urls[0]
            else:
                response_data["edited_image_urls"] = edited_urls
                response_data["edited_image_url"] = edited_urls[0]  # First one for backward compatibility
            
            print(f"\n✅ Edit successful!")
            print(f"   Operation: {operation_name}")
            print(f"   Images processed: {len(edited_urls)}/{len(valid_images)}\n")
            
            return jsonify(response_data)
        else:
            return jsonify({
                "error": "All image edits failed",
                "total_attempted": len(valid_images)
            }), 500
    
    except Exception as e:
        print(f"\n❌ Error in edit endpoint: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for deployment monitoring"""
    return jsonify({
        "status": "healthy",
        "service": "Product Creative Generator",
        "features": {
            "image_generation": True,
            "image_editing": True,
            "video_generation": True,
            "prompt_view": ENABLE_PROMPT_VIEW
        }
    })


if __name__ == '__main__':
    app.run(debug=True, port=5001)