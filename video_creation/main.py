"""
Main entry point for video creation system.
FIXED: PIL compatibility for Pillow 10+
"""
import os
import sys

# CRITICAL: Set environment variables BEFORE imports
os.environ['PYTHONUNBUFFERED'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
os.environ['NUMEXPR_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Force stdout unbuffering
sys.stdout.reconfigure(line_buffering=True)

# PIL/Pillow 10+ compatibility fix
try:
    from PIL import Image
    if not hasattr(Image, 'ANTIALIAS'):
        # Pillow 10+ removed ANTIALIAS, add it back for compatibility
        Image.ANTIALIAS = Image.Resampling.LANCZOS
        Image.BILINEAR = Image.Resampling.BILINEAR
        Image.BICUBIC = Image.Resampling.BICUBIC
        Image.NEAREST = Image.Resampling.NEAREST
except Exception as e:
    print(f"Warning: PIL compatibility fix failed: {e}")
    
import os
import sys
import argparse
import traceback
from datetime import datetime
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.core.config_loader import ConfigLoader
from src.core.video_composer import VideoComposer

# ASCII Art Banner
BANNER = """PROFESSIONAL VIDEO CREATOR SYSTEM"""

class VideoCreatorCLI:
    """Command-line interface for video creation."""
    
    def __init__(self):
        self.config_loader = ConfigLoader()
        self.start_time = None
    
    def run(self, args):
        """
        Main execution flow.
        
        Args:
            args: Parsed command-line arguments
        """
        try:
            # Display banner
            print(BANNER)
            
            # Record start time
            self.start_time = datetime.now()
            print(f"🕐 Started at: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            # Handle different commands
            if args.command == 'create':
                self.create_video(args)
            elif args.command == 'validate':
                self.validate_config(args)
            elif args.command == 'sample':
                self.create_sample_config(args)
            else:
                print(f"❌ Unknown command: {args.command}")
                sys.exit(1)
            
            # Report completion time
            self._report_completion()
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Process interrupted by user")
            sys.exit(130)
        
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            if args.debug:
                print("\nDebug traceback:")
                traceback.print_exc()
            sys.exit(1)
    
    def create_video(self, args):
        """
        Create video from configuration.
        
        Args:
            args: Command-line arguments
        """
        # Load configuration
        config = self.config_loader.load(args.config)
        
        # Override output path if specified
        if args.output:
            config['output_path'] = args.output
            print(f"📁 Output overridden to: {args.output}")
        
        # Save processed config if requested
        if args.save_config:
            self.config_loader.save_processed_config()
        
        # Create video composer
        composer = VideoComposer(config)
        
        # Compose video
        output_path = composer.compose()
        
        # Report success
        print(f"\n🎉 Success! Video created: {output_path}")
        
        # Get file size
        file_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
        print(f"   File size: {file_size:.2f} MB")
        
        # Open video if requested
        if args.open:
            self._open_video(output_path)
    
    def validate_config(self, args):
        """
        Validate configuration without creating video.
        
        Args:
            args: Command-line arguments
        """
        print("🔍 Validating configuration...\n")
        
        try:
            config = self.config_loader.load(args.config)
            
            # Report configuration details
            print("\n📊 Configuration Summary:")
            print(f"   Resolution: {config['width']}x{config['height']}")
            print(f"   FPS: {config['fps']}")
            print(f"   Scenes: {len(config.get('scenes', []))}")
            
            if 'audio_path' in config:
                print(f"   Audio: {os.path.basename(config['audio_path'])}")
            
            # Count overlays
            total_overlays = sum(
                len(scene.get('overlays', []))
                for scene in config.get('scenes', [])
            )
            print(f"   Total overlays: {total_overlays}")
            
            print("\n✅ Configuration is valid!")
            
            # Save processed config if requested
            if args.save_config:
                self.config_loader.save_processed_config()
            
        except Exception as e:
            print(f"\n❌ Validation failed: {str(e)}")
            if args.debug:
                traceback.print_exc()
            sys.exit(1)
    
    def create_sample_config(self, args):
        """
        Create a sample configuration file.
        
        Args:
            args: Command-line arguments
        """
        output_path = args.output or 'config_sample.json'
        
        print(f"📝 Creating sample configuration: {output_path}")
        
        try:
            ConfigLoader.create_sample_config(output_path)
            print(f"\n✅ Sample configuration created successfully!")
            print(f"   Edit this file and run:")
            print(f"   python main.py create {output_path}")
        
        except Exception as e:
            print(f"\n❌ Failed to create sample: {str(e)}")
            sys.exit(1)
    
    def _report_completion(self):
        """Report execution time."""
        if self.start_time:
            end_time = datetime.now()
            duration = end_time - self.start_time
            
            minutes, seconds = divmod(duration.total_seconds(), 60)
            
            print(f"\n⏱️  Total time: {int(minutes)}m {seconds:.1f}s")
            print(f"🏁 Completed at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def _open_video(self, path):
        """
        Open video in default player.
        
        Args:
            path: Path to video file
        """
        try:
            import platform
            system = platform.system()
            
            if system == 'Windows':
                os.startfile(path)
            elif system == 'Darwin':  # macOS
                os.system(f'open "{path}"')
            else:  # Linux
                os.system(f'xdg-open "{path}"')
            
            print(f"   🎬 Opening video in default player...")
        
        except Exception as e:
            print(f"   ⚠️  Could not open video: {str(e)}")

def create_parser():
    """Create command-line argument parser."""
    parser = argparse.ArgumentParser(
        description='Professional Video Creator System',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Create video from config:
    python main.py create config.json
    
  Create video with custom output:
    python main.py create config.json -o output/my_video.mp4
    
  Validate configuration:
    python main.py validate config.json
    
  Create sample configuration:
    python main.py sample
    
  Debug mode with full traceback:
    python main.py create config.json --debug
        """
    )
    
    # Add subcommands
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create video from configuration')
    create_parser.add_argument('config', help='Path to configuration JSON file')
    create_parser.add_argument('-o', '--output', help='Override output path')
    create_parser.add_argument('--save-config', action='store_true',
                              help='Save processed configuration for debugging')
    create_parser.add_argument('--open', action='store_true',
                              help='Open video after creation')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate configuration')
    validate_parser.add_argument('config', help='Path to configuration JSON file')
    validate_parser.add_argument('--save-config', action='store_true',
                                help='Save processed configuration')
    
    # Sample command
    sample_parser = subparsers.add_parser('sample', help='Create sample configuration')
    sample_parser.add_argument('-o', '--output', help='Output path for sample config')
    
    # Global arguments
    parser.add_argument('--debug', action='store_true', 
                       help='Enable debug mode with full traceback')
    parser.add_argument('--version', action='version', version='1.0.0')
    
    return parser

def main():
    """Main entry point."""
    # Parse arguments
    parser = create_parser()
    args = parser.parse_args()
    
    # Check if command was provided
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Run CLI
    cli = VideoCreatorCLI()
    cli.run(args)

if __name__ == '__main__':
    main()