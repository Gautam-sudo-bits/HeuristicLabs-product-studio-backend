"""
Text background/banner system for maximum readability.
"""
from PIL import Image, ImageDraw
import numpy as np

def add_text_background(text_img, style='banner', opacity=0.7, padding=20, color=(0, 0, 0)):
    """
    Add background to text for better readability.
    
    Args:
        text_img: PIL Image with text
        style: 'banner', 'rounded', 'box', 'gradient'
        opacity: Background opacity (0-1)
        padding: Extra padding around text
        color: Background color RGB tuple
    
    Returns:
        PIL Image with background
    """
    width, height = text_img.size
    
    # Create new image with extra space
    new_width = width + padding * 2
    new_height = height + padding * 2
    
    # Create background
    bg = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(bg)
    
    # Calculate alpha from opacity
    alpha = int(255 * opacity)
    bg_color = color + (alpha,)
    
    if style == 'banner':
        # Full width banner
        draw.rectangle([0, 0, new_width, new_height], fill=bg_color)
    
    elif style == 'rounded':
        # Rounded rectangle
        radius = min(30, new_height // 4)
        draw.rounded_rectangle([0, 0, new_width, new_height], radius=radius, fill=bg_color)
    
    elif style == 'box':
        # Simple box
        draw.rectangle([padding//2, padding//2, new_width-padding//2, new_height-padding//2], 
                      fill=bg_color)
    
    elif style == 'gradient':
        # Vertical gradient
        for y in range(new_height):
            gradient_alpha = int(alpha * (1 - abs(y - new_height/2) / (new_height/2)))
            grad_color = color + (gradient_alpha,)
            draw.line([(0, y), (new_width, y)], fill=grad_color)
    
    # Paste text on top
    bg.paste(text_img, (padding, padding), text_img)
    
    return bg