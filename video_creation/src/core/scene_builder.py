"""
Scene builder - constructs individual scenes with motion, text, and overlays.
"""
import moviepy.editor as mp
from PIL import Image
import os
from src.core.text_renderer import TextRenderer
from src.effects.motion import apply_motion_effect
#from src.effects.text_animations import apply_text_animation
from src.utils.timing import calculate_scene_duration
from src.utils.helpers import parse_position

class SceneBuilder:
    def __init__(self, width=1184, height=864):
        """
        Initialize scene builder.
        
        Args:
            width: Video frame width
            height: Video frame height
        """
        self.width = width
        self.height = height
        self.text_renderer = TextRenderer(width, height)
    
    def build_scene(self, scene_config, scene_index=0):
        """
        Build a complete scene from configuration.
        
        Args:
            scene_config: Scene configuration dictionary
            scene_index: Scene number (for logging)
        
        Returns:
            MoviePy CompositeVideoClip with all elements
        """
        scene_name = scene_config.get('name', f'Scene {scene_index + 1}')
        print(f"\n🎬 Building scene: {scene_name}")
        
        # Calculate duration (auto or manual)
        duration = calculate_scene_duration(scene_config)
        print(f"   Duration: {duration:.2f}s")
        
        # Load and prepare background
        background_clip = self._create_background(scene_config, duration)
        
        # Create overlay clips (text, images, etc.)
        overlay_clips = self._create_overlays(scene_config, duration)
        
        # Composite all layers
        all_clips = [background_clip] + overlay_clips
        scene_clip = mp.CompositeVideoClip(all_clips, size=(self.width, self.height))
        scene_clip = scene_clip.set_duration(duration)
        
        print(f"   ✅ Scene complete!")
        
        return scene_clip
    
    def _create_background(self, scene_config, duration):
        """
        Create background clip with motion effects.
        
        Args:
            scene_config: Scene configuration
            duration: Scene duration
        
        Returns:
            MoviePy clip with motion applied
        """
        image_path = scene_config['image_path']
        
        # Validate image exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Scene image not found: {image_path}")
        
        print(f"   📷 Loading image: {os.path.basename(image_path)}")
        
        # Load image as clip
        bg_clip = mp.ImageClip(image_path)
        
        # Crop/resize to fill frame (handles aspect ratio)
        bg_clip = self._crop_to_fill(bg_clip, self.width, self.height)
        bg_clip = bg_clip.set_duration(duration)
        
        # Apply background motion effect
        effect_config = scene_config.get('background_effect', {'type': 'static'})
        effect_type = effect_config.get('type', 'static')
        
        if effect_type != 'static':
            print(f"   🎥 Applying motion: {effect_type}")
            bg_clip = apply_motion_effect(bg_clip, duration, effect_config)
        
        return bg_clip
    
    def _create_overlays(self, scene_config, scene_duration):
        """
        Create all overlay clips (text, images, etc.).
        
        Args:
            scene_config: Scene configuration
            scene_duration: Total scene duration
        
        Returns:
            List of overlay clips
        """
        overlay_clips = []
        overlays = scene_config.get('overlays', [])
        
        for i, overlay_config in enumerate(overlays):
            overlay_type = overlay_config.get('type')
            
            if overlay_type == 'text':
                clip = self._create_text_overlay(overlay_config, scene_duration)
                overlay_clips.append(clip)
            
            elif overlay_type == 'image':
                clip = self._create_image_overlay(overlay_config, scene_duration)
                overlay_clips.append(clip)
            
            # Future: Add support for video overlays, shapes, etc.
        
        return overlay_clips
    
    def _create_text_overlay(self, overlay_config, scene_duration):
        """
        Create animated text overlay using frame-based animation system.
        Position is handled internally by the animator.
        """
        from src.effects.text_animator_v2 import TextAnimator
        
        text = overlay_config.get('text', '')
        print(f"   📝 Rendering animated text: \"{text[:40]}{'...' if len(text) > 40 else ''}\"")
        
        # Create animator
        animator = TextAnimator(self.width, self.height, fps=30)
        
        # Generate animated clip (position handled internally)
        text_clip = animator.create_animated_text(overlay_config, scene_duration)
        
        # DO NOT call set_position - frames are already full-frame with text positioned
        
        return text_clip
    
    def _create_image_overlay(self, overlay_config, scene_duration):
        """
        Create image overlay (logos, icons, etc.).
        
        Args:
            overlay_config: Image overlay configuration
            scene_duration: Total scene duration
        
        Returns:
            MoviePy image clip
        """
        image_path = overlay_config.get('path')
        
        if not os.path.exists(image_path):
            print(f"   ⚠️  Warning: Overlay image not found: {image_path}")
            return None
        
        print(f"   🖼️  Adding image overlay: {os.path.basename(image_path)}")
        
        # Load image
        overlay_clip = mp.ImageClip(image_path)
        
        # Resize if width specified (as percentage or pixels)
        if 'width' in overlay_config:
            target_width = overlay_config['width']
            if isinstance(target_width, float) and target_width <= 1.0:
                # Percentage of frame width
                target_width = int(self.width * target_width)
            overlay_clip = overlay_clip.resize(width=target_width)
        
        # Set duration
        overlay_clip = overlay_clip.set_duration(scene_duration)
        
        # Position
        position = overlay_config.get('position', 'center')
        parsed_position = parse_position(position, (self.width, self.height))
        overlay_clip = overlay_clip.set_position(parsed_position)
        
        # Optional: fade in/out
        if overlay_config.get('fade_in'):
            overlay_clip = overlay_clip.fadein(0.5)
        if overlay_config.get('fade_out'):
            overlay_clip = overlay_clip.fadeout(0.5)
        
        return overlay_clip
    
    def _crop_to_fill(self, clip, width, height):
        """
        Resize and crop clip to fill target dimensions without distortion.
        
        Args:
            clip: MoviePy clip
            width: Target width
            height: Target height
        
        Returns:
            Cropped clip
        """
        clip_width, clip_height = clip.size
        target_ratio = width / height
        clip_ratio = clip_width / clip_height
        
        if clip_ratio > target_ratio:
            # Clip is wider - fit to height, crop width
            resized = clip.resize(height=height)
        else:
            # Clip is taller - fit to width, crop height
            resized = clip.resize(width=width)
        
        # Crop to exact size from center
        return resized.crop(
            x_center=resized.w / 2,
            y_center=resized.h / 2,
            width=width,
            height=height
        )