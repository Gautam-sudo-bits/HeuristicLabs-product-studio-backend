import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
# --- Configuration ---
# Ensure your Google API key is set as an environment variable.
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    print("ERROR: GEMINI_API_KEY environment variable not set.")
    exit()

print("Listing available models that support video generation (generateContent)...")

# Iterate through all available models and find the one for Veo
found_veo_model = False
for m in genai.list_models():
  # The 'generateContent' method is what we use for video
  if 'generateContent' in m.supported_generation_methods:
    # We are looking for the video model, which will have 'veo' in its name
    if 'veo' in m.name:
        print(f"Found available Veo model: {m.name}")
        found_veo_model = True

if not found_veo_model:
    print("\nCould not find any models with 'veo' in the name.")
    print("This might mean you don't have access yet or the name is different.")
    print("Check all available models below:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)