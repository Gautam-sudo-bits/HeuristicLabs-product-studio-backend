"""
Main entry point for Mixed Video Creator.
Handles both images and videos as scenes.
"""
import os
import sys
import argparse
import json
from pathlib import Path

# Set environment before imports
os.environ['PYTHONUNBUFFERED'] = '1'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Add project root
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.video_mixer import MixedComposer
from src.core.config_loader import ConfigLoader

def main():
    
    parser = argparse.ArgumentParser(description='Mixed Video Creator')
    parser.add_argument('config', help='Path to config JSON file')
    parser.add_argument('-o', '--output', help='Override output path')
    
    args = parser.parse_args()
    
    # Load config
    print(f"📄 Loading config: {args.config}\n", flush=True)
    
    with open(args.config, 'r') as f:
        config = json.load(f)
    
    # Override output if specified
    if args.output:
        config['output_path'] = args.output
    
    # Compose video
    composer = MixedComposer(config)
    output_path = composer.compose()
    
    # Report
    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\n🎉 Success! Video created: {output_path}", flush=True)
    print(f"   File size: {file_size:.2f} MB\n", flush=True)

if __name__ == '__main__':
    main()