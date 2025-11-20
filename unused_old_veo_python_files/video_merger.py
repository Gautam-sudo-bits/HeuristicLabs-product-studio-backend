"""
Video merging utilities using MoviePy
Merges video segments with crossfade transitions
"""

import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
from datetime import datetime
import config


def merge_videos_with_crossfade(video_paths, output_path, crossfade_duration=None):
    """
    Merge multiple video segments with crossfade transitions
    
    Args:
        video_paths: List of paths to video files (in order)
        output_path: Path for output merged video
        crossfade_duration: Duration of crossfade in seconds
    
    Returns:
        str: Path to merged video file
    """
    if crossfade_duration is None:
        crossfade_duration = config.CROSSFADE_DURATION
    
    print(f"\n🎞️  Merging {len(video_paths)} video segment(s)...")
    print(f"   Crossfade duration: {crossfade_duration}s")
    
    try:
        # Load all video clips
        clips = []
        for idx, video_path in enumerate(video_paths, 1):
            if not os.path.exists(video_path):
                raise FileNotFoundError(f"Video file not found: {video_path}")
            
            print(f"   Loading segment {idx}: {os.path.basename(video_path)}")
            clip = VideoFileClip(video_path)
            clips.append(clip)
        
        if not clips:
            raise ValueError("No video clips to merge")
        
        # If only one clip, no need to merge
        if len(clips) == 1:
            print("   Only one segment, copying directly...")
            clips[0].write_videofile(
                output_path,
                codec=config.VIDEO_CODEC,
                fps=config.VIDEO_FPS,
                preset=config.VIDEO_PRESET,
                logger=None  # Suppress moviepy logs
            )
            clips[0].close()
            return output_path
        
        # Apply crossfade transitions
        print(f"   Applying crossfade transitions...")
        final_clips = []
        
        for i, clip in enumerate(clips):
            if i == 0:
                # First clip: fade out at end
                final_clips.append(clip.crossfadeout(crossfade_duration))
            elif i == len(clips) - 1:
                # Last clip: fade in at start
                final_clips.append(clip.crossfadein(crossfade_duration))
            else:
                # Middle clips: fade in and out
                final_clips.append(
                    clip.crossfadein(crossfade_duration).crossfadeout(crossfade_duration)
                )
        
        # Concatenate with method='compose' to handle overlapping fades
        print(f"   Concatenating clips...")
        final_video = concatenate_videoclips(final_clips, method="compose")
        
        # Calculate expected duration
        total_duration = sum(clip.duration for clip in clips)
        overlap = crossfade_duration * (len(clips) - 1)
        expected_duration = total_duration - overlap
        
        print(f"   Original total: {total_duration:.1f}s")
        print(f"   Crossfade overlap: {overlap:.1f}s")
        print(f"   Final duration: {expected_duration:.1f}s")
        
        # Write final video
        print(f"   Writing final video to: {output_path}")
        final_video.write_videofile(
            output_path,
            codec=config.VIDEO_CODEC,
            fps=config.VIDEO_FPS,
            preset=config.VIDEO_PRESET,
            logger=None  # Suppress moviepy verbose output
        )
        
        # Clean up
        for clip in clips:
            clip.close()
        final_video.close()
        
        print(f"   ✅ Video merged successfully!")
        print(f"   Output: {output_path}")
        
        return output_path
        
    except Exception as e:
        print(f"   ❌ Error merging videos: {e}")
        # Clean up clips on error
        for clip in clips:
            try:
                clip.close()
            except:
                pass
        raise


def merge_videos_hard_cut(video_paths, output_path):
    """
    Merge multiple video segments with hard cuts (no transitions)
    Faster alternative to crossfade
    
    Args:
        video_paths: List of paths to video files (in order)
        output_path: Path for output merged video
    
    Returns:
        str: Path to merged video file
    """
    print(f"\n🎞️  Merging {len(video_paths)} video segment(s) with hard cuts...")
    
    try:
        # Load all video clips
        clips = []
        for idx, video_path in enumerate(video_paths, 1):
            if not os.path.exists(video_path):
                raise FileNotFoundError(f"Video file not found: {video_path}")
            
            print(f"   Loading segment {idx}: {os.path.basename(video_path)}")
            clip = VideoFileClip(video_path)
            clips.append(clip)
        
        if not clips:
            raise ValueError("No video clips to merge")
        
        # Concatenate directly
        print(f"   Concatenating clips...")
        final_video = concatenate_videoclips(clips, method="compose")
        
        total_duration = sum(clip.duration for clip in clips)
        print(f"   Total duration: {total_duration:.1f}s")
        
        # Write final video
        print(f"   Writing final video to: {output_path}")
        final_video.write_videofile(
            output_path,
            codec=config.VIDEO_CODEC,
            fps=config.VIDEO_FPS,
            preset=config.VIDEO_PRESET,
            logger=None
        )
        
        # Clean up
        for clip in clips:
            clip.close()
        final_video.close()
        
        print(f"   ✅ Video merged successfully!")
        print(f"   Output: {output_path}")
        
        return output_path
        
    except Exception as e:
        print(f"   ❌ Error merging videos: {e}")
        # Clean up clips on error
        for clip in clips:
            try:
                clip.close()
            except:
                pass
        raise


def get_video_info(video_path):
    """
    Get information about a video file
    
    Args:
        video_path: Path to video file
    
    Returns:
        dict: Video information (duration, fps, size, etc.)
    """
    try:
        clip = VideoFileClip(video_path)
        
        info = {
            "duration": clip.duration,
            "fps": clip.fps,
            "size": clip.size,
            "width": clip.w,
            "height": clip.h,
            "aspect_ratio": f"{clip.w}:{clip.h}"
        }
        
        clip.close()
        return info
        
    except Exception as e:
        print(f"Error getting video info: {e}")
        return None


def log_merge_operation(video_paths, output_path, merge_type="crossfade"):
    """
    Log video merge operation details
    
    Args:
        video_paths: List of input video paths
        output_path: Output video path
        merge_type: Type of merge (crossfade or hard_cut)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_file = os.path.join(config.LOG_FOLDER, "video_merge_log.txt")
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*80}\n")
        f.write(f"[{timestamp}] VIDEO MERGE OPERATION\n")
        f.write(f"{'='*80}\n")
        f.write(f"Merge Type: {merge_type}\n")
        f.write(f"Input Segments: {len(video_paths)}\n")
        
        for idx, path in enumerate(video_paths, 1):
            f.write(f"  Segment {idx}: {path}\n")
        
        f.write(f"Output: {output_path}\n")
        
        # Get output video info if file exists
        if os.path.exists(output_path):
            info = get_video_info(output_path)
            if info:
                f.write(f"Final Duration: {info['duration']:.2f}s\n")
                f.write(f"Resolution: {info['width']}x{info['height']}\n")
                f.write(f"FPS: {info['fps']}\n")
        
        f.write(f"{'='*80}\n\n")


if __name__ == "__main__":
    # Test video merger
    print("Testing video merger...")
    print("\n⚠️ This module requires actual video files to test.")
    print("Use from ad_pipeline.py in production.")
    
    # Example usage
    print("\nExample usage:")
    print("""
    from video_merger import merge_videos_with_crossfade
    
    video_paths = ["segment_1.mp4", "segment_2.mp4", "segment_3.mp4"]
    output = "final_video.mp4"
    
    merged_video = merge_videos_with_crossfade(video_paths, output)
    """)