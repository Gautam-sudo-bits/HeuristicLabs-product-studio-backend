"""
Video composer - assembles scenes with transitions, audio, and final touches.
"""
import moviepy.editor as mp
from moviepy.video.fx.all import fadein, fadeout
import os
from src.core.scene_builder import SceneBuilder
from src.effects.transitions import apply_transition

class VideoComposer:
    def __init__(self, config):
        """
        Initialize video composer with configuration.
        
        Args:
            config: Full video configuration dictionary
        """
        self.config = config
        self.width = config.get('width', 1184)
        self.height = config.get('height', 864)
        self.fps = config.get('fps', 30)
        
        self.scene_builder = SceneBuilder(self.width, self.height)
    
    def compose(self):
        """
        Compose the complete video from all scenes.
        
        Returns:
            Path to output video file
        """
        print("\n" + "="*60)
        print("🎬 STARTING VIDEO COMPOSITION")
        print("="*60)
        
        # Build all scenes
        scene_clips = self._build_all_scenes()
        
        # Apply transitions and concatenate
        final_video = self._apply_transitions(scene_clips)
        
        # Add audio
        if 'audio_path' in self.config and self.config['audio_path']:
            final_video = self._add_audio(final_video)
        
        # Apply final effects (intro/outro fades)
        final_video = self._apply_final_effects(final_video)
        
        # Export video
        output_path = self._export_video(final_video)
        
        # Cleanup
        self._cleanup(final_video)
        
        print("\n" + "="*60)
        print(f"✅ VIDEO COMPLETE: {output_path}")
        print("="*60 + "\n")
        
        return output_path
    
    def _build_all_scenes(self):
        """
        Build all scene clips from configuration.
        
        Returns:
            List of scene clips
        """
        scenes_config = self.config.get('scenes', [])
        scene_clips = []
        
        print(f"\n📋 Building {len(scenes_config)} scenes...\n")
        
        for i, scene_config in enumerate(scenes_config):
            try:
                scene_clip = self.scene_builder.build_scene(scene_config, i)
                scene_clips.append({
                    'clip': scene_clip,
                    'config': scene_config,
                    'index': i
                })
            except Exception as e:
                print(f"\n❌ Error building scene {i+1}: {str(e)}")
                raise
        
        return scene_clips
    
    def _apply_transitions(self, scene_clips):
        """
        Apply transitions between scenes with proper timeline management.
        """
        if not scene_clips:
            raise ValueError("No scenes to compose!")
        
        if len(scene_clips) == 1:
            return scene_clips[0]['clip']
        
        print(f"\n🎞️  Applying transitions between {len(scene_clips)} scenes...")
        
        # Build timeline with proper transitions
        timeline_clips = []
        current_time = 0
        
        for i, scene_data in enumerate(scene_clips):
            clip = scene_data['clip']
            config = scene_data['config']
            
            # Position clip on timeline
            clip = clip.set_start(current_time)
            
            # Handle transition
            if i > 0 and 'transition' in config:
                trans_config = config['transition']
                trans_type = trans_config.get('type', 'fade')
                trans_duration = min(trans_config.get('duration', 1.0), clip.duration * 0.5)
                
                print(f"   Scene {i} → {i+1}: {trans_type} ({trans_duration}s)")
                
                # Apply transition effects
                if trans_type in ['fade', 'crossfade']:
                    # Fade out previous clip
                    if timeline_clips:
                        prev_clip = timeline_clips[-1]
                        # Adjust previous clip to fade out
                        timeline_clips[-1] = prev_clip.crossfadeout(trans_duration)
                    
                    # Fade in current clip
                    clip = clip.crossfadein(trans_duration)
                    
                    # Overlap clips
                    clip = clip.set_start(current_time - trans_duration)
                    current_time -= trans_duration  # Account for overlap
                
                elif trans_type in ['slide', 'slideIn']:
                    direction = trans_config.get('from_edge', 'left')
                    
                    # Create slide effect
                    w, h = clip.size
                    
                    if direction == 'left':
                        # Slide from left
                        slide_func = lambda t: (max(0, w * (1 - t/trans_duration)), 0)
                    elif direction == 'right':
                        slide_func = lambda t: (min(0, -w * (1 - t/trans_duration)), 0)
                    else:
                        slide_func = lambda t: (0, 0)
                    
                    # Apply slide with overlap
                    clip = clip.set_position(slide_func).set_start(current_time - trans_duration)
                    current_time -= trans_duration
            
            timeline_clips.append(clip)
            
            # Update timeline position
            current_time += clip.duration
            
            # Log progress
            if i == 0:
                print(f"   Scene {i+1}: starts at 0.0s, duration {clip.duration:.2f}s")
            else:
                start_time = clip.start if hasattr(clip, 'start') else current_time - clip.duration
                print(f"   Scene {i+1}: starts at {start_time:.2f}s, duration {clip.duration:.2f}s")
        
        # Composite all clips
        final_clip = mp.CompositeVideoClip(
            timeline_clips,
            size=(self.width, self.height)
        )
        
        print(f"   ✅ Total video duration: {final_clip.duration:.2f}s")
        
        return final_clip
    
    def _add_audio(self, video_clip):
        """
        Add background audio to video.
        
        Args:
            video_clip: Video clip without audio
        
        Returns:
            Video clip with audio
        """
        audio_path = self.config['audio_path']
        
        if not os.path.exists(audio_path):
            print(f"\n⚠️  Warning: Audio file not found: {audio_path}")
            print("   Continuing without audio...")
            return video_clip
        
        print(f"\n🎵 Adding audio: {os.path.basename(audio_path)}")
        
        # Load audio
        audio = mp.AudioFileClip(audio_path)
        video_duration = video_clip.duration
        
        print(f"   Video duration: {video_duration:.2f}s")
        print(f"   Audio duration: {audio.duration:.2f}s")
        
        # Handle audio length
        if audio.duration > video_duration:
            # Trim audio to video length
            print(f"   Trimming audio to {video_duration:.2f}s")
            audio = audio.subclip(0, video_duration)
            # Fade out audio at end
            audio = audio.audio_fadeout(1.5)
        
        elif audio.duration < video_duration:
            # Loop audio to match video length
            print(f"   Looping audio to match video duration")
            loops_needed = int(video_duration / audio.duration) + 1
            audio = mp.concatenate_audioclips([audio] * loops_needed)
            audio = audio.subclip(0, video_duration)
            audio = audio.audio_fadeout(1.5)
        
        # Apply audio to video
        video_with_audio = video_clip.set_audio(audio)
        
        print("   ✅ Audio added")
        
        return video_with_audio
    
    def _apply_final_effects(self, video_clip):
        """
        Apply final video effects (intro/outro fades).
        
        Args:
            video_clip: Video clip
        
        Returns:
            Video clip with final effects
        """
        print("\n✨ Applying final effects...")
        
        # Get fade durations from config
        intro_fade = self.config.get('intro_fade', 0.5)
        outro_fade = self.config.get('outro_fade', 1.0)
        
        # Apply fades
        if intro_fade > 0:
            video_clip = video_clip.fadein(intro_fade)
            print(f"   Intro fade: {intro_fade}s")
        
        if outro_fade > 0:
            video_clip = video_clip.fadeout(outro_fade)
            print(f"   Outro fade: {outro_fade}s")
        
        return video_clip
    
    def _export_video(self, video_clip):
        """Export video to file with proper RGB conversion."""
        output_path = self.config.get('output_path', 'output/video.mp4')
        
        # Ensure output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        print(f"\n📹 Exporting video...")
        print(f"   Output: {output_path}")
        print(f"   Resolution: {self.width}x{self.height}")
        print(f"   FPS: {self.fps}")
        print(f"   Duration: {video_clip.duration:.2f}s")
        
        # Export settings
        codec = self.config.get('codec', 'libx264')
        audio_codec = self.config.get('audio_codec', 'aac')
        bitrate = self.config.get('bitrate', '5000k')
        preset = self.config.get('preset', 'medium')
        
        # Write video file with proper pixel format
        video_clip.write_videofile(
            output_path,
            fps=self.fps,
            codec=codec,
            audio_codec=audio_codec,
            bitrate=bitrate,
            preset=preset,
            threads=4,
            logger='bar',
            ffmpeg_params=["-pix_fmt", "yuv420p"]  # Force standard pixel format
        )
        
        return output_path
        
    def _cleanup(self, video_clip):
        """
        Clean up resources.
        
        Args:
            video_clip: Video clip to close
        """
        print("\n🧹 Cleaning up resources...")
        
        try:
            video_clip.close()
            if video_clip.audio:
                video_clip.audio.close()
        except:
            pass
        
        print("   ✅ Cleanup complete")