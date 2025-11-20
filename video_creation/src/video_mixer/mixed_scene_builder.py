"""
Mixed Scene Builder - handles both image and video scenes.
Uses existing text animation system without modification.
"""
import moviepy.editor as mp
import os
from src.effects.text_animator_v2 import TextAnimator
from src.effects.motion import apply_motion_effect
from src.utils.timing import calculate_scene_duration
from src.utils.helpers import parse_position
from .video_utils import VideoUtils

class MixedSceneBuilder:
    """Builds scenes from both images and videos."""
    
    def __init__(self, width=1184, height=864):
        self.width = width
        self.height = height
        self.text_animator = TextAnimator(width, height)
        self.video_utils = VideoUtils()
    
    def build_scene(self, scene_config, scene_index=0):
        """
        Build a scene from either image or video source.
        FIXED: Video scenes use natural duration unless specified.
        """
        scene_name = scene_config.get('name', f'Scene {scene_index + 1}')
        scene_type = scene_config.get('type', 'image')
        
        print(f"\n🎬 Building scene: {scene_name} (type: {scene_type})", flush=True)
        
        # Calculate duration differently for videos vs images
        if scene_type == 'video':
            # For videos: use natural duration unless explicitly set
            if 'duration' in scene_config and scene_config['duration'] > 0:
                duration = scene_config['duration']
                print(f"   Duration: {duration:.2f}s (specified)", flush=True)
            else:
                # Will be determined by video length
                duration = None
                print(f"   Duration: Auto (from video)", flush=True)
        else:
            # For images: calculate from text or use config
            duration = calculate_scene_duration(scene_config)
            print(f"   Duration: {duration:.2f}s", flush=True)
        
        # Create background clip (image or video)
        if scene_type == 'video':
            background_clip = self._create_video_background(scene_config, duration)
            # Update duration to actual video duration
            if duration is None:
                duration = background_clip.duration
                print(f"   Actual duration: {duration:.2f}s", flush=True)
        else:
            background_clip = self._create_image_background(scene_config, duration)
        
        # Create text overlays
        overlay_clips = self._create_overlays(scene_config, duration)
        
        # Composite all layers
        all_clips = [background_clip] + overlay_clips
        scene_clip = mp.CompositeVideoClip(all_clips, size=(self.width, self.height))
        scene_clip = scene_clip.set_duration(duration)
        
        print(f"   ✅ Scene complete!", flush=True)
        
        return scene_clip
    
    def _create_image_background(self, scene_config, duration):
        """Create background from image (existing logic)."""
        image_path = scene_config.get('image_path') or scene_config.get('path')
        
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")
        
        print(f"   📷 Loading image: {os.path.basename(image_path)}", flush=True)
        
        # Load image
        bg_clip = mp.ImageClip(image_path)
        bg_clip = self._crop_to_fill(bg_clip, self.width, self.height)
        bg_clip = bg_clip.set_duration(duration)
        
        # Apply motion effect
        effect_config = scene_config.get('background_effect', {'type': 'static'})
        effect_type = effect_config.get('type', 'static')
        
        if effect_type != 'static':
            print(f"   🎥 Applying motion: {effect_type}", flush=True)
            bg_clip = apply_motion_effect(bg_clip, duration, effect_config)
        
        return bg_clip
    
    def _create_video_background(self, scene_config, duration):
        """
        Create background from video.
        FIXED: Only loop if explicitly needed.
        """
        video_path = scene_config.get('video_path') or scene_config.get('path')
        
        # Video processing options
        start_time = scene_config.get('video_start', 0)
        end_time = scene_config.get('video_end', None)
        speed = scene_config.get('video_speed', 1.0)
        resize_method = scene_config.get('resize_method', 'crop')
        
        # Load and process video
        # CRITICAL: Only pass target_duration if explicitly set in config
        bg_clip = self.video_utils.load_video(
            video_path,
            target_duration=duration,  # This will be None if not specified
            start_time=start_time,
            end_time=end_time,
            speed=speed
        )
        
        # Resize to frame dimensions
        bg_clip = self.video_utils.resize_video(
            bg_clip, self.width, self.height, method=resize_method
        )
        
        return bg_clip
    
    def _create_overlays(self, scene_config, scene_duration):
        """Create text overlays (works for both images and videos)."""
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
        
        return overlay_clips
    
    def _create_text_overlay(self, overlay_config, scene_duration):
        """Create animated text overlay (reuses existing system)."""
        text = overlay_config.get('text', '') or (
            '\n'.join([line.get('text', '') for line in overlay_config.get('lines', [])])
        )
        
        print(f"   📝 Adding text overlay: \"{text[:30]}...\"", flush=True)
        
        # Use existing text animator
        text_clip = self.text_animator.create_animated_text(overlay_config, scene_duration)
        
        return text_clip
    
    def _create_image_overlay(self, overlay_config, scene_duration):
        """Create image overlay (logo, watermark, etc.)."""
        image_path = overlay_config.get('path')
        
        if not os.path.exists(image_path):
            print(f"   ⚠️  Overlay image not found: {image_path}", flush=True)
            return None
        
        print(f"   🖼️  Adding image overlay: {os.path.basename(image_path)}", flush=True)
        
        overlay_clip = mp.ImageClip(image_path)
        
        # Resize if specified
        if 'width' in overlay_config:
            target_width = overlay_config['width']
            if isinstance(target_width, float) and target_width <= 1.0:
                target_width = int(self.width * target_width)
            overlay_clip = overlay_clip.resize(width=target_width)
        
        overlay_clip = overlay_clip.set_duration(scene_duration)
        
        # Position
        position = overlay_config.get('position', 'center')
        parsed_position = parse_position(position, (self.width, self.height))
        overlay_clip = overlay_clip.set_position(parsed_position)
        
        # Optional fade
        if overlay_config.get('fade_in'):
            overlay_clip = overlay_clip.fadein(0.5)
        if overlay_config.get('fade_out'):
            overlay_clip = overlay_clip.fadeout(0.5)
        
        return overlay_clip
    
    def _crop_to_fill(self, clip, width, height):
        """Crop image to fill dimensions."""
        clip_width, clip_height = clip.size
        target_ratio = width / height
        clip_ratio = clip_width / clip_height
        
        if clip_ratio > target_ratio:
            resized = clip.resize(height=height)
        else:
            resized = clip.resize(width=width)
        
        return resized.crop(
            x_center=resized.w / 2,
            y_center=resized.h / 2,
            width=width,
            height=height
        )