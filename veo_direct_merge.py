"""
Video Merger with Crossfade Transitions
Merges multiple videos with smooth crossfade transitions
Only truncates video duration if necessary for transitions
"""

import os
from pathlib import Path
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
import time

# ===========================
# CONFIGURATION
# ===========================

# Input videos (in order of merging)
INPUT_VIDEOS = [
    r"E:\product-image-backend\outputs\videos\video_20251107_201722_best_pan.mp4",
    r"E:\product-image-backend\outputs\videos\video_20251107_214229_best.mp4",
]

# Output settings
OUTPUT_VIDEO = "merged_output_best.mp4"
OUTPUT_FOLDER = "merged_outputs"

# Transition settings
CROSSFADE_DURATION = 0.5  # seconds (crossfade transition duration)

# Export settings
OUTPUT_FPS = 30
OUTPUT_CODEC = "libx264"
OUTPUT_AUDIO_CODEC = "aac"
PRESET = "medium"  # ultrafast, fast, medium, slow, slower
BITRATE = "5000k"

# ===========================
# HELPER FUNCTIONS
# ===========================

def validate_videos(video_paths):
    """Check if all video files exist"""
    print("🔍 Validating video files...")
    
    missing_videos = []
    for video in video_paths:
        if not os.path.exists(video):
            missing_videos.append(video)
            print(f"   ❌ Not found: {video}")
        else:
            print(f"   ✅ Found: {video}")
    
    if missing_videos:
        raise FileNotFoundError(f"Missing videos: {missing_videos}")
    
    print(f"   ✅ All {len(video_paths)} video(s) found\n")


def get_video_info(video_path):
    """Get video metadata"""
    clip = VideoFileClip(video_path)
    info = {
        'path': video_path,
        'duration': clip.duration,
        'fps': clip.fps,
        'size': clip.size,
        'audio': clip.audio is not None
    }
    clip.close()
    return info


def print_video_info(videos_info):
    """Display video metadata"""
    print("📹 Video Information:")
    print("-" * 70)
    
    for i, info in enumerate(videos_info, 1):
        print(f"Video {i}: {Path(info['path']).name}")
        print(f"   Duration: {info['duration']:.2f}s")
        print(f"   FPS: {info['fps']}")
        print(f"   Resolution: {info['size'][0]}x{info['size'][1]}")
        print(f"   Audio: {'Yes' if info['audio'] else 'No'}")
    
    print("-" * 70 + "\n")


def calculate_final_duration(videos_info, crossfade_duration, num_videos):
    """Calculate final merged video duration"""
    total = sum(info['duration'] for info in videos_info)
    # Subtract overlaps (n-1 transitions)
    total -= crossfade_duration * (num_videos - 1)
    return total


def apply_crossfade(clip, position, total_clips, crossfade_duration):
    """
    Apply crossfade effects based on clip position
    
    Args:
        clip: VideoFileClip
        position: 0=first, -1=last, else=middle
        total_clips: Total number of clips
        crossfade_duration: Duration of crossfade
    
    Returns:
        Modified clip with crossfade applied
    """
    duration = clip.duration
    
    # Safety check: ensure clip is long enough
    if duration < crossfade_duration:
        fade_dur = duration / 2
        print(f"      ⚠️  Clip too short ({duration:.2f}s), using {fade_dur:.2f}s fade")
    else:
        fade_dur = crossfade_duration
    
    # First clip: only fade out at end
    if position == 0:
        return clip.fx(lambda c: c.fadein(0).fadeout(fade_dur))
    
    # Last clip: only fade in at start
    elif position == total_clips - 1:
        return clip.fx(lambda c: c.fadein(fade_dur).fadeout(0))
    
    # Middle clips: fade in and fade out
    else:
        return clip.fx(lambda c: c.fadein(fade_dur).fadeout(fade_dur))


def merge_videos_with_crossfade(video_paths, crossfade_duration):
    """
    Merge videos with crossfade transitions using CompositeVideoClip
    
    Args:
        video_paths: List of video file paths
        crossfade_duration: Duration of crossfade in seconds
    
    Returns:
        Final merged VideoClip
    """
    print("🎬 Loading video clips...")
    
    # Load all clips
    clips = []
    for i, path in enumerate(video_paths, 1):
        print(f"   Loading {i}/{len(video_paths)}: {Path(path).name}")
        clip = VideoFileClip(path)
        clips.append(clip)
    
    print(f"   ✅ All clips loaded\n")
    
    # Apply fade effects
    print("✨ Applying crossfade transitions...")
    
    processed_clips = []
    for i, clip in enumerate(clips):
        print(f"   Processing clip {i+1}/{len(clips)}...")
        processed = apply_crossfade(clip, i, len(clips), crossfade_duration)
        processed_clips.append(processed)
    
    print(f"   ✅ All transitions applied\n")
    
    # Calculate start times for each clip (with overlaps)
    print("🔗 Calculating clip positions...")
    
    clip_start_times = [0]  # First clip starts at 0
    
    for i in range(1, len(processed_clips)):
        # Each clip starts at: previous_start + previous_duration - crossfade_duration
        prev_start = clip_start_times[i-1]
        prev_duration = processed_clips[i-1].duration
        new_start = prev_start + prev_duration - crossfade_duration
        clip_start_times.append(new_start)
    
    # Set start times
    for i, clip in enumerate(processed_clips):
        clip = clip.set_start(clip_start_times[i])
        processed_clips[i] = clip
        print(f"   Clip {i+1}: starts at {clip_start_times[i]:.2f}s")
    
    print()
    
    # Composite all clips together
    print("🎞️  Creating composite video...")
    
    final_clip = CompositeVideoClip(processed_clips)
    
    print(f"   ✅ Composite created\n")
    print(f"   Final duration: {final_clip.duration:.2f}s")
    print(f"   Resolution: {final_clip.size[0]}x{final_clip.size[1]}")
    
    return final_clip


def export_video(clip, output_path, fps, codec, audio_codec, preset, bitrate):
    """Export final video with progress"""
    print(f"\n💾 Exporting to: {output_path}")
    print(f"   Codec: {codec}")
    print(f"   FPS: {fps}")
    print(f"   Preset: {preset}")
    print(f"   Bitrate: {bitrate}\n")
    
    # Create output folder if needed
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    start_time = time.time()
    
    # Export with progress bar
    clip.write_videofile(
        output_path,
        fps=fps,
        codec=codec,
        audio_codec=audio_codec,
        preset=preset,
        bitrate=bitrate,
        verbose=True,
        logger='bar'
    )
    
    elapsed = time.time() - start_time
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    
    print(f"\n   ✅ Export complete!")
    print(f"   File size: {file_size_mb:.2f} MB")
    print(f"   Export time: {elapsed:.1f}s\n")


# ===========================
# MAIN PIPELINE
# ===========================

def run_merger():
    """Main video merging pipeline"""
    start_time = time.time()
    
    print("=" * 70)
    print("🎬 VIDEO MERGER WITH CROSSFADE TRANSITIONS")
    print("=" * 70)
    print()
    
    # Step 1: Validate input videos exist
    validate_videos(INPUT_VIDEOS)
    
    # Step 2: Get video information
    videos_info = [get_video_info(path) for path in INPUT_VIDEOS]
    print_video_info(videos_info)
    
    # Step 3: Show estimated final duration
    estimated_duration = calculate_final_duration(videos_info, CROSSFADE_DURATION, len(INPUT_VIDEOS))
    print(f"📐 Estimated final duration: {estimated_duration:.2f}s")
    print(f"   (Original total: {sum(v['duration'] for v in videos_info):.2f}s)")
    print(f"   (Crossfade overlaps: -{CROSSFADE_DURATION * (len(INPUT_VIDEOS) - 1):.2f}s)\n")
    
    # Step 4: Merge videos
    merged_clip = merge_videos_with_crossfade(INPUT_VIDEOS, CROSSFADE_DURATION)
    
    # Step 5: Export
    output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_VIDEO)
    export_video(
        merged_clip,
        output_path,
        OUTPUT_FPS,
        OUTPUT_CODEC,
        OUTPUT_AUDIO_CODEC,
        PRESET,
        BITRATE
    )
    
    # Cleanup
    print("🧹 Cleaning up...")
    merged_clip.close()
    print("   ✅ Resources released\n")
    
    # Summary
    total_time = time.time() - start_time
    print("=" * 70)
    print("✅ MERGE COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print(f"📹 Output: {output_path}")
    print(f"⏱️  Total time: {total_time:.1f}s")
    print(f"🎞️  Videos merged: {len(INPUT_VIDEOS)}")
    print(f"✨ Transition type: Crossfade ({CROSSFADE_DURATION}s)")
    print("=" * 70)


if __name__ == "__main__":
    try:
        run_merger()
    except KeyboardInterrupt:
        print("\n\n⚠️ Merge interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Merge failed: {e}")
        import traceback
        traceback.print_exc()