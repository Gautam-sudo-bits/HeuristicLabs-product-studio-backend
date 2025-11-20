"""
Professional motion effects with smooth easing.
"""
import moviepy.editor as mp
from src.utils.easing import get_easing

def create_smooth_ken_burns(clip, duration, zoom=1.2, direction='in', pan=None, easing='motion'):
    """
    Enhanced Ken Burns effect with smooth easing.
    
    Args:
        clip: MoviePy ImageClip
        duration: Duration in seconds
        zoom: Zoom factor (1.0 = no zoom, 1.2 = 20% zoom)
        direction: 'in', 'out', 'in-out'
        pan: Pan direction ('left', 'right', 'up', 'down') or None
        easing: Easing function name
    
    Returns:
        Animated clip
    """
    w, h = clip.size
    ease_func = get_easing(easing)
    
    def get_scale(t):
        """Calculate scale at time t with easing."""
        progress = ease_func(t / duration)
        
        if direction == 'in':
            return 1.0 + (zoom - 1.0) * progress
        elif direction == 'out':
            return zoom - (zoom - 1.0) * progress
        elif direction == 'in-out':
            if progress < 0.5:
                return 1.0 + (zoom - 1.0) * (progress * 2)
            else:
                return zoom - (zoom - 1.0) * ((progress - 0.5) * 2)
        return zoom
    
    def get_position(t):
        """Calculate position at time t with easing."""
        progress = ease_func(t / duration)
        scale = get_scale(t)
        
        # Calculate how much we can pan based on current scale
        available_w = w * scale - w
        available_h = h * scale - h
        
        x, y = 'center', 'center'
        
        if pan == 'right':
            x = -available_w * progress
        elif pan == 'left':
            x = -available_w * (1 - progress)
        elif pan == 'down':
            y = -available_h * progress
        elif pan == 'up':
            y = -available_h * (1 - progress)
        
        return (x, y)
    
    return clip.resize(get_scale).set_position(get_position)

def create_parallax_effect(clip, duration, layers=3, depth=0.05, easing='motion'):
    """
    Create subtle parallax effect for depth.
    Best used with product images on neutral backgrounds.
    
    Args:
        clip: MoviePy ImageClip
        duration: Duration in seconds
        layers: Number of parallax layers
        depth: Movement depth (0.0-0.1 recommended)
        easing: Easing function name
    """
    w, h = clip.size
    ease_func = get_easing(easing)
    
    def get_position(t):
        progress = ease_func(t / duration)
        # Gentle horizontal movement
        x_offset = w * depth * (progress - 0.5) * 2  # -depth to +depth
        return (x_offset, 'center')
    
    # Slight zoom to prevent edge visibility
    zoomed = clip.resize(1.0 + depth * 2)
    return zoomed.set_position(get_position)

def create_zoom_pulse(clip, duration, intensity=0.03, pulses=1, easing='zoom'):
    """
    Subtle zoom pulse effect for emphasis.
    
    Args:
        clip: MoviePy ImageClip
        duration: Duration in seconds
        intensity: Zoom intensity (0.03 = 3% zoom)
        pulses: Number of pulses
        easing: Easing function name
    """
    import math
    ease_func = get_easing(easing)
    
    def get_scale(t):
        progress = (t / duration) * pulses
        # Sine wave for pulse effect
        pulse = math.sin(progress * math.pi * 2)
        return 1.0 + intensity * pulse
    
    return clip.resize(get_scale)

# Motion presets mapping
MOTION_PRESETS = {
    'kenburns_in': lambda clip, dur: create_smooth_ken_burns(clip, dur, zoom=1.15, direction='in'),
    'kenburns_out': lambda clip, dur: create_smooth_ken_burns(clip, dur, zoom=1.15, direction='out'),
    'kenburns_right': lambda clip, dur: create_smooth_ken_burns(clip, dur, zoom=1.1, direction='in', pan='right'),
    'kenburns_left': lambda clip, dur: create_smooth_ken_burns(clip, dur, zoom=1.1, direction='in', pan='left'),
    'kenburns_down': lambda clip, dur: create_smooth_ken_burns(clip, dur, zoom=1.1, direction='in', pan='down'),
    'kenburns_up': lambda clip, dur: create_smooth_ken_burns(clip, dur, zoom=1.1, direction='in', pan='up'),
    'parallax': lambda clip, dur: create_parallax_effect(clip, dur),
    'zoom_pulse': lambda clip, dur: create_zoom_pulse(clip, dur),
    'static': lambda clip, dur: clip,
}

def apply_motion_effect(clip, duration, effect_config):
    """
    Apply motion effect based on config.
    
    Args:
        clip: MoviePy ImageClip
        duration: Scene duration
        effect_config: Effect configuration dict
            Example: {"type": "kenBurns", "zoom": 1.2, "direction": "in"}
    
    Returns:
        Animated clip
    """
    effect_type = effect_config.get('type', 'static')
    
    if effect_type == 'static':
        return clip
    
    elif effect_type == 'kenBurns':
        zoom = effect_config.get('zoom', 1.15)
        direction = effect_config.get('direction', 'in')
        pan = effect_config.get('pan', None)
        
        return create_smooth_ken_burns(clip, duration, zoom=zoom, 
                                      direction=direction, pan=pan)
    
    elif effect_type == 'parallax':
        depth = effect_config.get('depth', 0.05)
        return create_parallax_effect(clip, duration, depth=depth)
    
    elif effect_type == 'pulse':
        intensity = effect_config.get('intensity', 0.03)
        pulses = effect_config.get('pulses', 1)
        return create_zoom_pulse(clip, duration, intensity=intensity, pulses=pulses)
    
    # Fallback to static
    return clip