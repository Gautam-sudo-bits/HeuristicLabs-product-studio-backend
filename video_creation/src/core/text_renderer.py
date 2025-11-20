"""
PIL-based text renderer with frame-relative sizing.
FIXED: Text renders at appropriate size for frame resolution.
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from src.utils.helpers import get_font_path, hex_to_rgb

class TextRenderer:
    def __init__(self, width=1184, height=864):
        self.width = width
        self.height = height
    
    def render_text_multicolor(self, text_lines, font, font_size, bold, shadow, outline, outline_width):
        """
        Render text with different colors per line.
        
        Args:
            text_lines: List of dicts [{"text": "Line 1", "color": "#FFFFFF"}, ...]
                        OR single string "Line1\nLine2" with line_colors list
            font: Font name
            font_size: Base font size
            bold: Bold flag
            shadow: Shadow flag
            outline: Outline flag
            outline_width: Outline thickness
        
        Returns:
            PIL Image with multi-colored text
        """
        from src.utils.helpers import hex_to_rgb
        
        # Scale font for resolution
        base_reference = 720
        frame_scale = self.height / base_reference
        actual_font_size = int(font_size * frame_scale * 1.5)
        
        # Load font
        font_name = f"{font}-Bold" if bold and not font.endswith('Bold') else font
        font_path = get_font_path(font_name)
        
        try:
            pil_font = ImageFont.truetype(font_path or "arial.ttf", actual_font_size)
        except:
            pil_font = ImageFont.load_default()
        
        # Process text_lines into structured format
        if isinstance(text_lines, str):
            # Legacy format: split by \n
            lines = text_lines.replace('\\n', '\n').split('\n')
            structured_lines = [{"text": line, "color": "#FFFFFF"} for line in lines]
        else:
            # New format: list of dicts
            structured_lines = text_lines
        
        # Calculate dimensions
        line_spacing = 1.2
        max_width = int(self.width * 0.9)
        line_height = int(actual_font_size * line_spacing)
        
        # Wrap each line and calculate dimensions
        wrapped_lines = []
        for line_data in structured_lines:
            line_text = line_data.get('text', '')
            line_color = line_data.get('color', '#FFFFFF')
            
            if line_text.strip():
                wrapped = self._wrap_text(line_text, pil_font, max_width)
                for wrapped_text in wrapped:
                    wrapped_lines.append({
                        'text': wrapped_text,
                        'color': hex_to_rgb(line_color) if isinstance(line_color, str) else line_color
                    })
            else:
                wrapped_lines.append({'text': '', 'color': (255, 255, 255)})
        
        # Calculate image dimensions
        text_widths = []
        for line_data in wrapped_lines:
            if line_data['text'].strip():
                try:
                    bbox = pil_font.getbbox(line_data['text'])
                    text_widths.append(bbox[2] - bbox[0])
                except:
                    text_widths.append(len(line_data['text']) * actual_font_size // 2)
        
        total_width = max(text_widths) if text_widths else actual_font_size * 10
        total_height = line_height * len(wrapped_lines)
        
        # Create image
        padding = 40
        img_width = int(total_width + padding * 2)
        img_height = int(total_height + padding * 2)
        
        img = Image.new('RGBA', (img_width, img_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Draw each line with its color
        y = padding
        for line_data in wrapped_lines:
            line_text = line_data['text']
            line_color = line_data['color']
            
            if not line_text.strip():
                y += line_height
                continue
            
            try:
                bbox = pil_font.getbbox(line_text)
                line_width = bbox[2] - bbox[0]
            except:
                line_width = len(line_text) * actual_font_size // 2
            
            x = (img_width - line_width) // 2
            
            # Shadow
            if shadow:
                shadow_offset = max(3, actual_font_size // 30)
                for i in range(3, 0, -1):
                    offset = shadow_offset * i
                    alpha = 80 + (3 - i) * 40
                    draw.text((x + offset, y + offset), line_text, font=pil_font, 
                            fill=(0, 0, 0, alpha))
            
            # Outline
            if outline:
                for ox in range(-outline_width, outline_width + 1):
                    for oy in range(-outline_width, outline_width + 1):
                        if abs(ox) == outline_width or abs(oy) == outline_width:
                            draw.text((x + ox, y + oy), line_text, font=pil_font, 
                                    fill=(0, 0, 0, 255))
            
            # Main text with line-specific color
            draw.text((x, y), line_text, font=pil_font, fill=line_color + (255,))
            y += line_height
        
        return img
    
    def _wrap_text(self, text, font, max_width):
        """Wrap text to fit within max_width."""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = font.getbbox(test_line)
            if (bbox[2] - bbox[0]) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines if lines else [text]