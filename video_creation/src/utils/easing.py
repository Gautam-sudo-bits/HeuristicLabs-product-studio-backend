"""
Easing functions for smooth, professional animations.
Based on https://easings.net/
"""
import math

def linear(t):
    """No easing, linear interpolation."""
    return t

def ease_in_out_cubic(t):
    """Smooth acceleration and deceleration."""
    return 4 * t * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 3) / 2

def ease_in_out_quad(t):
    """Gentler acceleration/deceleration."""
    return 2 * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 2) / 2

def ease_out_cubic(t):
    """Fast start, slow end."""
    return 1 - pow(1 - t, 3)

def ease_in_cubic(t):
    """Slow start, fast end."""
    return t * t * t

def ease_out_expo(t):
    """Exponential ease out - very smooth."""
    return 1 if t == 1 else 1 - pow(2, -10 * t)

def ease_in_out_sine(t):
    """Sinusoidal easing - very natural."""
    return -(math.cos(math.pi * t) - 1) / 2

def ease_out_back(t):
    """Slight overshoot for dynamic effect."""
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * pow(t - 1, 3) + c1 * pow(t - 1, 2)

# Default easing for different effects
EASING_PRESETS = {
    'motion': ease_in_out_cubic,      # Smooth camera motion
    'zoom': ease_in_out_sine,          # Natural zoom
    'text': ease_out_cubic,            # Text appearance
    'transition': ease_in_out_quad,    # Scene transitions
    'dynamic': ease_out_back           # Attention-grabbing
}

def get_easing(name='motion'):
    """Get easing function by name."""
    return EASING_PRESETS.get(name, ease_in_out_cubic)