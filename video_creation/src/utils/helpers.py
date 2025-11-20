"""
Helper utilities for video creation.
"""
import os
from PIL import ImageFont

def ensure_dir(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_font_path(font_name, font_dir='assets/fonts'):
    """
    Get font path. Falls back to system fonts.
    
    Args:
        font_name: Name of the font (e.g., 'Arial', 'Arial-Bold')
        font_dir: Directory containing custom fonts
    
    Returns:
        Path to font file or None for default
    """
    # Custom font directory
    custom_font = os.path.join(font_dir, f"{font_name}.ttf")
    if os.path.exists(custom_font):
        return custom_font
    
    # Common system font locations
    system_fonts = {
        'windows': 'C:/Windows/Fonts',
        'linux': '/usr/share/fonts/truetype',
        'mac': '/Library/Fonts'
    }
    
    # Try to find system font
    for system, path in system_fonts.items():
        if os.path.exists(path):
            # Common font file patterns
            patterns = [
                f"{font_name}.ttf",
                f"{font_name.lower()}.ttf",
                f"{font_name.replace(' ', '')}.ttf",
                f"{font_name.replace(' ', '').lower()}.ttf"
            ]
            
            for pattern in patterns:
                font_path = os.path.join(path, pattern)
                if os.path.exists(font_path):
                    return font_path
    
    # Return None to use PIL default
    return None

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def parse_position(position, frame_size):
    """
    Parse position from config to pixel coordinates.
    
    Args:
        position: 'center', 'top', 'bottom', [x, y], [x%, y%], etc.
        frame_size: (width, height) tuple
    
    Returns:
        (x, y) tuple in pixels
    """
    width, height = frame_size
    
    if position == 'center':
        return (width // 2, height // 2)
    elif position == 'top':
        return (width // 2, height * 0.15)
    elif position == 'bottom':
        return (width // 2, height * 0.85)
    elif isinstance(position, list):
        x, y = position
        
        # Handle percentage positioning
        if isinstance(x, str) and '%' in x:
            x = width * float(x.rstrip('%')) / 100
        elif isinstance(x, float) and x <= 1.0:
            x = width * x
        elif x == 'center':
            x = width // 2
            
        if isinstance(y, str) and '%' in y:
            y = height * float(y.rstrip('%')) / 100
        elif isinstance(y, float) and y <= 1.0:
            y = height * y
        elif y == 'center':
            y = height // 2
            
        return (int(x), int(y))
    
    return (width // 2, height // 2)  # Default to center