"""
Professional scene transitions.
"""
import moviepy.editor as mp
from moviepy.video.fx.all import fadein, fadeout
from src.utils.easing import get_easing
import numpy as np

def crossfade_transition(clip1, clip2, duration=1.0):
    """
    Smooth crossfade between clips.
    
    Args:
        clip1: Outgoing clip
        clip2: Incoming clip
        duration: Transition duration
    
    Returns:
        Concatenated clip with crossfade
    """
    # Apply fadeout to clip1
    clip1_faded = clip1.crossfadeout(duration)
    
    # Apply fadein to clip2
    clip2_faded = clip2.crossfadein(duration)
    
    # Overlap them
    clip2_faded = clip2_faded.set_start(clip1.duration - duration)
    
    return mp.CompositeVideoClip([clip1_faded, clip2_faded])

def slide_transition(clip1, clip2, duration=0.8, direction='left'):
    """
    Slide transition between clips.
    
    Args:
        clip1: Outgoing clip
        clip2: Incoming clip
        duration: Transition duration
        direction: 'left', 'right', 'up', 'down'
    
    Returns:
        Concatenated clip with slide
    """
    w, h = clip1.size
    ease_func = get_easing('transition')
    
    # Clip2 slides in over clip1
    if direction == 'left':
        def pos_func(t):
            if t < clip1.duration - duration:
                return (0, 0)
            progress = ease_func((t - (clip1.duration - duration)) / duration)
            return (w * (1 - progress), 0)
    elif direction == 'right':
        def pos_func(t):
            if t < clip1.duration - duration:
                return (0, 0)
            progress = ease_func((t - (clip1.duration - duration)) / duration)
            return (-w * (1 - progress), 0)
    elif direction == 'up':
        def pos_func(t):
            if t < clip1.duration - duration:
                return (0, 0)
            progress = ease_func((t - (clip1.duration - duration)) / duration)
            return (0, h * (1 - progress))
    elif direction == 'down':
        def pos_func(t):
            if t < clip1.duration - duration:
                return (0, 0)
            progress = ease_func((t - (clip1.duration - duration)) / duration)
            return (0, -h * (1 - progress))
    else:
        return crossfade_transition(clip1, clip2, duration)
    
    clip2_sliding = clip2.set_position(pos_func).set_start(clip1.duration - duration)
    
    return mp.CompositeVideoClip([clip1, clip2_sliding], size=(w, h))

def zoom_transition(clip1, clip2, duration=1.0, direction='in'):
    """
    Zoom transition between clips.
    
    Args:
        clip1: Outgoing clip
        clip2: Incoming clip
        duration: Transition duration
        direction: 'in' (clip2 zooms in) or 'out' (clip1 zooms out)
    
    Returns:
        Concatenated clip with zoom transition
    """
    ease_func = get_easing('transition')
    
    if direction == 'in':
        # Clip2 starts small and zooms in
        def scale_func(t):
            if t < clip1.duration - duration:
                return 1.0
            progress = ease_func((t - (clip1.duration - duration)) / duration)
            return 0.5 + 0.5 * progress
        
        clip2_zooming = clip2.resize(scale_func).set_start(clip1.duration - duration)
        clip1_fading = clip1.fadeout(duration)
        
    else:  # direction == 'out'
        # Clip1 zooms out
        def scale_func(t):
            if t < clip1.duration - duration:
                return 1.0
            progress = ease_func((t - (clip1.duration - duration)) / duration)
            return 1.0 + 0.5 * progress
        
        clip1_fading = clip1.resize(scale_func).fadeout(duration)
        clip2_zooming = clip2.fadein(duration).set_start(clip1.duration - duration)
    
    return mp.CompositeVideoClip([clip1_fading, clip2_zooming])

def apply_transition(clip1, clip2, transition_config):
    """
    Apply transition between two clips based on config.
    
    Args:
        clip1: Outgoing clip
        clip2: Incoming clip
        transition_config: Transition configuration dict
            Example: {"type": "fade", "duration": 1.0}
                    {"type": "slideIn", "duration": 0.8, "from_edge": "left"}
    
    Returns:
        Transition clip
    """
    if not transition_config:
        return clip2
    
    trans_type = transition_config.get('type', 'fade')
    duration = transition_config.get('duration', 1.0)
    
    if trans_type == 'fade' or trans_type == 'crossfade':
        return crossfade_transition(clip1, clip2, duration)
    
    elif trans_type == 'slideIn' or trans_type == 'slide':
        direction = transition_config.get('from_edge', 'left')
        return slide_transition(clip1, clip2, duration, direction)
    
    elif trans_type == 'zoom':
        direction = transition_config.get('direction', 'in')
        return zoom_transition(clip1, clip2, duration, direction)
    
    # Default to crossfade
    return crossfade_transition(clip1, clip2, duration)