"""
Video utilities for processing video clips.
Handles trimming, speed adjustment, looping, etc.
"""
import moviepy.editor as mp
import os

class VideoUtils:
    """Utility functions for video processing."""
    
    @staticmethod
    def load_video(video_path, target_duration=None, start_time=0, end_time=None, speed=1.0):
        """
        Load and process a video clip.
        FIXED: Only loops if target_duration > video duration.
        """
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video not found: {video_path}")
        
        print(f"      Loading video: {os.path.basename(video_path)}", flush=True)
        
        # Load video
        clip = mp.VideoFileClip(video_path)
        
        # Apply trimming
        if end_time:
            clip = clip.subclip(start_time, min(end_time, clip.duration))
        elif start_time > 0:
            clip = clip.subclip(start_time, clip.duration)
        
        # Apply speed adjustment
        if speed != 1.0:
            clip = clip.fx(mp.vfx.speedx, speed)
            print(f"      Applied {speed}x speed", flush=True)
        
        # Adjust to target duration ONLY if specified
        if target_duration is not None:
            current_duration = clip.duration
            
            if current_duration < target_duration:
                # Only loop if explicitly requested via target_duration
                loops_needed = int(target_duration / current_duration) + 1
                clip = mp.concatenate_videoclips([clip] * loops_needed)
                clip = clip.subclip(0, target_duration)
                print(f"      Looped video to {target_duration:.2f}s", flush=True)
            elif current_duration > target_duration:
                # Trim to target duration
                clip = clip.subclip(0, target_duration)
                print(f"      Trimmed video to {target_duration:.2f}s", flush=True)
        else:
            # No target duration - use natural length
            print(f"      Using natural duration: {clip.duration:.2f}s", flush=True)
        
        return clip
    
    @staticmethod
    def resize_video(clip, target_width, target_height, method='crop'):
        """
        Resize video to target dimensions.
        
        Args:
            clip: MoviePy clip
            target_width: Target width
            target_height: Target height
            method: 'crop', 'fit', or 'stretch'
        
        Returns:
            Resized clip
        """
        if method == 'crop':
            # Crop to fill (like images)
            return VideoUtils._crop_to_fill(clip, target_width, target_height)
        elif method == 'fit':
            # Fit inside dimensions (letterbox)
            return clip.resize(height=target_height)
        elif method == 'stretch':
            # Stretch to exact size
            return clip.resize((target_width, target_height))
        else:
            return clip
    
    @staticmethod
    def _crop_to_fill(clip, width, height):
        """Crop video to fill target dimensions without distortion."""
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
    
    @staticmethod
    def add_motion_to_video(clip, effect_config):
        """
        Add motion effects to video (optional enhancement).
        
        Args:
            clip: MoviePy clip
            effect_config: Effect configuration
        
        Returns:
            Clip with motion effect
        """
        effect_type = effect_config.get('type', 'none')
        
        if effect_type == 'zoom':
            # Zoom effect on video
            zoom_factor = effect_config.get('zoom', 1.1)
            direction = effect_config.get('direction', 'in')
            
            def zoom_func(t):
                progress = t / clip.duration
                if direction == 'in':
                    return 1.0 + (zoom_factor - 1.0) * progress
                else:
                    return zoom_factor - (zoom_factor - 1.0) * progress
            
            return clip.resize(zoom_func)
        
        return clip