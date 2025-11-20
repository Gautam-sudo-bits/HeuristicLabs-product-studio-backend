"""
Mixed Video Composer - composes final video from mixed scenes.
Extends existing composer functionality without modifying it.
"""
import moviepy.editor as mp
from moviepy.video.fx.all import fadein, fadeout
import os
from .mixed_scene_builder import MixedSceneBuilder
from src.effects.transitions import apply_transition

class MixedComposer:
    """Composes videos from mixed image/video scenes."""
    
    def __init__(self, config):
        self.config = config
        self.width = config.get('width', 1184)
        self.height = config.get('height', 864)
        self.fps = config.get('fps', 30)
        
        self.scene_builder = MixedSceneBuilder(self.width, self.height)
    
    def compose(self):
        """Compose the complete video."""
        print("\n" + "="*60, flush=True)
        print("🎬 STARTING MIXED VIDEO COMPOSITION", flush=True)
        print("="*60, flush=True)
        
        # Build all scenes
        scene_clips = self._build_all_scenes()
        
        # Concatenate scenes
        final_video = self._concatenate_scenes(scene_clips)
        
        # Add audio
        if 'audio_path' in self.config and self.config['audio_path']:
            final_video = self._add_audio(final_video)
        
        # Final effects
        final_video = self._apply_final_effects(final_video)
        
        # Export
        output_path = self._export_video(final_video)
        
        # NEW: Clean up scene clips first
        for scene_data in scene_clips:
            try:
                scene_data['clip'].close()
            except:
                pass
        
        # Cleanup final video
        self._cleanup(final_video)
        
        # Force garbage collection
        import gc
        gc.collect()
        
        print("\n" + "="*60, flush=True)
        print(f"✅ VIDEO COMPLETE: {output_path}", flush=True)
        print("="*60 + "\n", flush=True)
        
        return output_path
    
    def _build_all_scenes(self):
        """Build all scenes (images and videos)."""
        scenes_config = self.config.get('scenes', [])
        scene_clips = []
        
        print(f"\n📋 Building {len(scenes_config)} scenes...\n", flush=True)
        
        for i, scene_config in enumerate(scenes_config):
            try:
                scene_clip = self.scene_builder.build_scene(scene_config, i)
                scene_clips.append({
                    'clip': scene_clip,
                    'config': scene_config,
                    'index': i
                })
            except Exception as e:
                print(f"\n❌ Error building scene {i+1}: {str(e)}", flush=True)
                raise
        
        return scene_clips
    
    def _concatenate_scenes(self, scene_clips):
        """Concatenate scenes with transitions."""
        if not scene_clips:
            raise ValueError("No scenes to compose!")
        
        if len(scene_clips) == 1:
            return scene_clips[0]['clip']
        
        print(f"\n🎞️  Concatenating {len(scene_clips)} scenes...", flush=True)
        
        # Simple concatenation for now
        clips = [sc['clip'] for sc in scene_clips]
        final_clip = mp.concatenate_videoclips(clips, method="compose")
        
        print(f"   ✅ Total video duration: {final_clip.duration:.2f}s", flush=True)
        
        return final_clip
    
    def _add_audio(self, video_clip):
        """Add background audio."""
        audio_path = self.config['audio_path']
        
        if not os.path.exists(audio_path):
            print(f"\n⚠️  Audio file not found: {audio_path}", flush=True)
            return video_clip
        
        print(f"\n🎵 Adding audio: {os.path.basename(audio_path)}", flush=True)
        
        audio = mp.AudioFileClip(audio_path)
        video_duration = video_clip.duration
        
        if audio.duration > video_duration:
            audio = audio.subclip(0, video_duration)
            audio = audio.audio_fadeout(1.5)
        elif audio.duration < video_duration:
            loops_needed = int(video_duration / audio.duration) + 1
            audio = mp.concatenate_audioclips([audio] * loops_needed)
            audio = audio.subclip(0, video_duration)
        
        video_with_audio = video_clip.set_audio(audio)
        print("   ✅ Audio added", flush=True)
        
        return video_with_audio
    
    def _apply_final_effects(self, video_clip):
        """Apply intro/outro fades."""
        print("\n✨ Applying final effects...", flush=True)
        
        intro_fade = self.config.get('intro_fade', 0.5)
        outro_fade = self.config.get('outro_fade', 1.0)
        
        if intro_fade > 0:
            video_clip = video_clip.fadein(intro_fade)
        if outro_fade > 0:
            video_clip = video_clip.fadeout(outro_fade)
        
        return video_clip
    
    def _export_video(self, video_clip):
        """Export final video."""
        output_path = self.config.get('output_path', 'output/mixed_video.mp4')
        
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        print(f"\n📹 Exporting video...", flush=True)
        print(f"   Output: {output_path}", flush=True)
        print(f"   Resolution: {self.width}x{self.height}", flush=True)
        print(f"   FPS: {self.fps}", flush=True)
        print(f"   Duration: {video_clip.duration:.2f}s", flush=True)
        
        video_clip.write_videofile(
            output_path,
            fps=self.fps,
            codec='libx264',
            audio_codec='aac',
            bitrate='5000k',
            preset='medium',
            threads=4,
            logger='bar',
            ffmpeg_params=["-pix_fmt", "yuv420p"]
        )
        
        return output_path
    
    def _cleanup(self, video_clip):
        """Clean up resources properly to avoid handle errors."""
        print("\n🧹 Cleaning up...", flush=True)
        
        try:
            # Close audio first
            if hasattr(video_clip, 'audio') and video_clip.audio:
                try:
                    video_clip.audio.close()
                except:
                    pass
            
            # Close the video clip
            if hasattr(video_clip, 'close'):
                try:
                    video_clip.close()
                except:
                    pass
            
            # Force garbage collection to clean up FFmpeg readers
            import gc
            gc.collect()
            
        except Exception as e:
            # Silently ignore cleanup errors
            pass
        
    print("   ✅ Cleanup complete", flush=True)