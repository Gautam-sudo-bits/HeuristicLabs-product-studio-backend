"""
Automatic duration calculation based on text reading speed.
UPDATED: Slower pacing for better comprehension.
"""

def calculate_text_duration(text, words_per_second=1.8, min_duration=4.0, max_duration=10.0):
    """
    Calculate optimal duration for text display.
    
    UPDATED VALUES:
    - words_per_second: Reduced from 2.5 to 1.8 (slower reading)
    - min_duration: Increased from 3.5 to 4.0 (more breathing room)
    - max_duration: Increased from 8.0 to 10.0 (allow longer scenes)
    """
    if not text or not text.strip():
        return min_duration
    
    word_count = len(text.split())
    
    # Base reading time (slower)
    reading_time = word_count / words_per_second
    
    # Animation time (fade in + fade out + pause)
    animation_buffer = 1.5  # 0.8s fade in + 0.7s pause
    
    # Comprehension time (increased)
    comprehension_time = word_count * 0.4  # Increased from 0.3
    
    # Total duration
    calculated_duration = reading_time + animation_buffer + comprehension_time
    
    # Clamp to min/max
    return max(min_duration, min(calculated_duration, max_duration))

def calculate_scene_duration(scene_data):
    """
    Calculate scene duration based on overlays.
    UPDATED: More generous default durations.
    """
    # Check for manual duration
    if 'duration' in scene_data and scene_data['duration'] > 0:
        return scene_data['duration']
    
    # Default duration for scenes without text (increased)
    base_duration = 4.5  # Increased from 3.5
    
    # Find longest text overlay
    max_text_duration = base_duration
    
    for overlay in scene_data.get('overlays', []):
        if overlay['type'] == 'text':
            text_duration = calculate_text_duration(overlay['text'])
            max_text_duration = max(max_text_duration, text_duration)
    
    # Add breathing room for scenes with text
    if scene_data.get('overlays'):
        max_text_duration += 1.0  # Extra second for comprehension
    
    return max_text_duration