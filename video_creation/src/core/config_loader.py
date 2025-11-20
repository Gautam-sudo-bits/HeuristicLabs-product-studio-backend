"""
Configuration loader with validation and defaults.
"""
import json
import os
from typing import Dict, Any, List, Optional

class ConfigLoader:
    """Handles configuration loading, validation, and preprocessing."""
    
    # Default configuration values
    DEFAULTS = {
        'width': 1184,
        'height': 864,
        'fps': 30,
        'output_path': 'output/video.mp4',
        'codec': 'libx264',
        'audio_codec': 'aac',
        'bitrate': '5000k',
        'preset': 'medium',
        'intro_fade': 0.5,
        'outro_fade': 1.0,
        'reading_speed': 2.5,  # words per second
        'min_scene_duration': 2.0,
        'max_scene_duration': 6.0,
        'default_font': 'Arial',
        'default_font_size': 80,
        'default_text_color': '#FFFFFF',
        'enable_text_shadow': True,
        'enable_text_bold': True,
    }
    
    # Required fields
    REQUIRED_FIELDS = ['scenes']
    
    # Valid animation types
    VALID_ANIMATIONS = [
        'fade_in', 'slide_bottom', 'slide_top', 'slide_left', 'slide_right',
        'scale_in', 'grow', 'typewriter', 'word_by_word',
        # Legacy Manim names (will be mapped)
        'AnimateTextFromLeft', 'AnimateTextGrowFromCenter', 'AnimateTextFadeInWordByWord'
    ]
    
    # Valid transition types
    VALID_TRANSITIONS = ['fade', 'crossfade', 'slide', 'slideIn', 'zoom']
    
    # Valid motion effects
    VALID_MOTIONS = ['static', 'kenBurns', 'parallax', 'pulse', 'zoom_pulse']
    
    def __init__(self, config_path: str = None):
        """
        Initialize config loader.
        
        Args:
            config_path: Path to configuration JSON file
        """
        self.config_path = config_path
        self.config = {}
        self.warnings = []
        self.errors = []
    
    def load(self, config_path: str = None) -> Dict[str, Any]:
        """
        Load and validate configuration.
        
        Args:
            config_path: Path to config file (overrides init path)
        
        Returns:
            Validated configuration dictionary
        
        Raises:
            FileNotFoundError: If config file not found
            JSONDecodeError: If config is invalid JSON
            ValueError: If validation fails
        """
        path = config_path or self.config_path
        
        if not path:
            raise ValueError("No configuration file specified")
        
        if not os.path.exists(path):
            raise FileNotFoundError(f"Configuration file not found: {path}")
        
        print(f"\n📄 Loading configuration from: {path}")
        
        # Load JSON
        with open(path, 'r', encoding='utf-8') as f:
            raw_config = json.load(f)
        
        # Merge with defaults
        self.config = self._merge_with_defaults(raw_config)
        
        # Validate configuration
        self._validate()
        
        # Preprocess scenes
        self._preprocess_scenes()
        
        # Report warnings
        if self.warnings:
            print("\n⚠️  Configuration warnings:")
            for warning in self.warnings:
                print(f"   - {warning}")
        
        # Check for errors
        if self.errors:
            print("\n❌ Configuration errors:")
            for error in self.errors:
                print(f"   - {error}")
            raise ValueError(f"Configuration validation failed with {len(self.errors)} errors")
        
        print("   ✅ Configuration loaded successfully")
        
        return self.config
    
    def _merge_with_defaults(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Merge user configuration with defaults.
        
        Args:
            config: User configuration
        
        Returns:
            Merged configuration
        """
        merged = self.DEFAULTS.copy()
        merged.update(config)
        return merged
    
    def _validate(self):
        """Validate configuration structure and values."""
        
        # Check required fields
        for field in self.REQUIRED_FIELDS:
            if field not in self.config:
                self.errors.append(f"Required field '{field}' is missing")
        
        # Validate scenes
        if 'scenes' in self.config:
            self._validate_scenes()
        
        # Validate output path
        if 'output_path' in self.config:
            output_dir = os.path.dirname(self.config['output_path'])
            if output_dir and not os.path.exists(output_dir):
                try:
                    os.makedirs(output_dir)
                    print(f"   Created output directory: {output_dir}")
                except:
                    self.errors.append(f"Cannot create output directory: {output_dir}")
        
        # Validate audio
        if 'audio_path' in self.config:
            if not os.path.exists(self.config['audio_path']):
                self.warnings.append(f"Audio file not found: {self.config['audio_path']}")
        
        # Validate dimensions
        if self.config['width'] <= 0 or self.config['height'] <= 0:
            self.errors.append("Video dimensions must be positive")
        
        # Validate FPS
        if self.config['fps'] <= 0:
            self.errors.append("FPS must be positive")
    
    def _validate_scenes(self):
        """Validate individual scene configurations."""
        scenes = self.config.get('scenes', [])
        
        if not scenes:
            self.errors.append("At least one scene is required")
            return
        
        for i, scene in enumerate(scenes):
            scene_name = scene.get('name', f'Scene {i+1}')
            
            # Check required scene fields
            if 'image_path' not in scene:
                self.errors.append(f"{scene_name}: Missing 'image_path'")
            elif not os.path.exists(scene['image_path']):
                self.errors.append(f"{scene_name}: Image not found: {scene['image_path']}")
            
            # Validate background effect
            if 'background_effect' in scene:
                effect = scene['background_effect']
                if 'type' in effect:
                    effect_type = effect['type']
                    if effect_type not in self.VALID_MOTIONS:
                        self.warnings.append(
                            f"{scene_name}: Unknown motion effect '{effect_type}', using 'static'"
                        )
                        effect['type'] = 'static'
            
            # Validate transition
            if 'transition' in scene:
                transition = scene['transition']
                if 'type' in transition:
                    trans_type = transition['type']
                    if trans_type not in self.VALID_TRANSITIONS:
                        self.warnings.append(
                            f"{scene_name}: Unknown transition '{trans_type}', using 'fade'"
                        )
                        transition['type'] = 'fade'
            
            # Validate overlays
            if 'overlays' in scene:
                self._validate_overlays(scene['overlays'], scene_name)
    
    def _validate_overlays(self, overlays: List[Dict], scene_name: str):
        """
        Validate overlay configurations.
        UPDATED: Support both 'text' and 'lines' formats.
        """
        for j, overlay in enumerate(overlays):
            overlay_name = f"{scene_name} - Overlay {j+1}"
            
            # Check overlay type
            if 'type' not in overlay:
                self.errors.append(f"{overlay_name}: Missing overlay 'type'")
                continue
            
            overlay_type = overlay['type']
            
            if overlay_type == 'text':
                # Validate text overlay - ACCEPT EITHER 'text' OR 'lines'
                has_text = 'text' in overlay
                has_lines = 'lines' in overlay
                
                if not has_text and not has_lines:
                    self.errors.append(f"{overlay_name}: Text overlay missing 'text' or 'lines' field")
                
                # Validate lines format if present
                if has_lines:
                    lines = overlay['lines']
                    if not isinstance(lines, list):
                        self.errors.append(f"{overlay_name}: 'lines' must be an array")
                    else:
                        for i, line in enumerate(lines):
                            if not isinstance(line, dict):
                                self.errors.append(f"{overlay_name}: lines[{i}] must be an object")
                            elif 'text' not in line:
                                self.errors.append(f"{overlay_name}: lines[{i}] missing 'text' field")
                
                # Validate animation
                if 'animation' in overlay:
                    anim = overlay['animation']
                    if anim not in self.VALID_ANIMATIONS:
                        self.warnings.append(
                            f"{overlay_name}: Unknown animation '{anim}', using 'fade_in'"
                        )
                        overlay['animation'] = 'fade_in'
            
            elif overlay_type == 'image':
                # Validate image overlay
                if 'path' not in overlay:
                    self.errors.append(f"{overlay_name}: Image overlay missing 'path' field")
                elif not os.path.exists(overlay['path']):
                    self.warnings.append(f"{overlay_name}: Image not found: {overlay['path']}")
    
    def _preprocess_scenes(self):
        """Preprocess scenes with defaults and calculated values."""
        scenes = self.config.get('scenes', [])
        
        for i, scene in enumerate(scenes):
            # Set default name if not present
            if 'name' not in scene:
                scene['name'] = f'Scene {i+1}'
            
            # Apply default background effect if not present
            if 'background_effect' not in scene:
                scene['background_effect'] = {'type': 'static'}
            
            # Process overlays
            if 'overlays' in scene:
                for overlay in scene['overlays']:
                    self._preprocess_overlay(overlay)
    
    def _preprocess_overlay(self, overlay: Dict):
        """Apply defaults to overlay configuration."""
        if overlay['type'] == 'text':
            # Apply text defaults
            if 'font' not in overlay:
                overlay['font'] = self.config['default_font']
            
            if 'font_size' not in overlay:
                overlay['font_size'] = self.config['default_font_size']
            
            if 'color' not in overlay:
                overlay['color'] = self.config['default_text_color']
            
            if 'bold' not in overlay:
                overlay['bold'] = self.config['enable_text_bold']
            
            if 'shadow' not in overlay:
                overlay['shadow'] = self.config['enable_text_shadow']
            
            if 'animation' not in overlay:
                overlay['animation'] = 'fade_in'
            
            if 'position' not in overlay:
                overlay['position'] = 'center'
            
            if 'start_time' not in overlay:
                overlay['start_time'] = 0
    
    def save_processed_config(self, output_path: str = None):
        """
        Save the processed configuration for debugging.
        
        Args:
            output_path: Path to save processed config
        """
        if not output_path:
            output_path = 'output/processed_config.json'
        
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2)
        
        print(f"   💾 Processed config saved to: {output_path}")
    
    @staticmethod
    def create_sample_config(output_path: str = 'config_sample.json'):
        """
        Create a sample configuration file.
        
        Args:
            output_path: Where to save the sample config
        """
        sample = {
            "output_path": "output/sample_video.mp4",
            "audio_path": "soundtrack/background_music.mp3",
            "width": 1184,
            "height": 864,
            "fps": 30,
            "scenes": [
                {
                    "name": "Introduction",
                    "image_path": "scenes/scene1.png",
                    "duration": 0,  # Auto-calculate from text
                    "background_effect": {
                        "type": "kenBurns",
                        "zoom": 1.1,
                        "direction": "in"
                    },
                    "overlays": [
                        {
                            "type": "text",
                            "text": "Welcome to Our Product",
                            "animation": "fade_in",
                            "font": "Arial",
                            "font_size": 100,
                            "color": "#FFFFFF",
                            "bold": True,
                            "position": "center",
                            "start_time": 0.5
                        }
                    ]
                },
                {
                    "name": "Feature 1",
                    "image_path": "scenes/scene2.png",
                    "transition": {
                        "type": "fade",
                        "duration": 1.0
                    },
                    "background_effect": {
                        "type": "kenBurns",
                        "direction": "right"
                    },
                    "overlays": [
                        {
                            "type": "text",
                            "text": "Premium Quality Materials",
                            "animation": "slide_bottom",
                            "font_size": 80,
                            "position": ["center", 0.8]
                        }
                    ]
                }
            ]
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(sample, f, indent=2)
        
        print(f"Sample configuration created: {output_path}")