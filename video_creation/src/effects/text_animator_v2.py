"""
Definitive text animation system using pre-rendered frames.
FIXED: Proper transparency handling
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import moviepy.editor as mp
from src.utils.helpers import get_font_path, hex_to_rgb
import math

class TextAnimator:
    """
    Professional text animator that pre-renders all frames.
    FIXED: Returns RGBA frames with transparency.
    """
    
    def __init__(self, width=1184, height=864, fps=30):
        self.width = width
        self.height = height
        self.fps = fps
    
    def create_animated_text(self, config, duration):
        """
        Create fully animated text clip from config.
        FIXED: Extracts and passes background parameters.
        """
        animation = config.get('animation', 'fade_in')
        start_time = config.get('start_time', 0)
        position = config.get('position', 'center')
        
        # Text styling
        font = config.get('font', 'Arial')
        font_size = config.get('font_size', 25)
        bold = config.get('bold', True)
        shadow = config.get('shadow', True)
        outline = config.get('outline', False)
        outline_width = config.get('outline_width', 3)
        
        # ✅ EXTRACT BACKGROUND PARAMETERS
        background = config.get('background', None)
        bg_opacity = config.get('bg_opacity', 0.7)
        bg_padding = config.get('bg_padding', 20)
        
        # Determine if multi-color or single-color text
        text_img = None
        
        if 'lines' in config:
            print(f"   📝 Rendering multi-color text ({len(config['lines'])} lines)", flush=True)
            text_img = self.render_text_multicolor(
                config['lines'], font, font_size, bold, shadow, outline, outline_width,
                background, bg_opacity, bg_padding  # ✅ PASS BACKGROUND PARAMS
            )
            text_string = '\n'.join([line.get('text', '') for line in config['lines']])
        
        elif 'line_colors' in config:
            text = config.get('text', '')
            lines_text = text.replace('\\n', '\n').split('\n')
            line_colors = config.get('line_colors', [])
            default_color = config.get('color', '#FFFFFF')
            
            structured_lines = []
            for i, line_text in enumerate(lines_text):
                color = line_colors[i] if i < len(line_colors) else default_color
                structured_lines.append({'text': line_text, 'color': color})
            
            print(f"   📝 Rendering text with {len(structured_lines)} colored lines", flush=True)
            text_img = self.render_text_multicolor(
                structured_lines, font, font_size, bold, shadow, outline, outline_width,
                background, bg_opacity, bg_padding  # ✅ PASS BACKGROUND PARAMS
            )
            text_string = text
        
        else:
            text = config.get('text', '')
            color = config.get('color', '#FFFFFF')
            
            print(f"   📝 Rendering single-color text: \"{text[:40]}...\"", flush=True)
            text_img = self.render_text(
                text, font, font_size, color, bold, shadow, outline, outline_width,
                background, bg_opacity, bg_padding  # ✅ PASS BACKGROUND PARAMS
            )
            text_string = text
        
        # Rest stays the same...
        pos_x, pos_y = self._parse_position(position)
        frames = self.generate_animation_frames(
            text_img, animation, duration, start_time, pos_x, pos_y
        )
        clip = mp.ImageSequenceClip(frames, fps=self.fps)
        clip = clip.set_duration(duration)
        
        return clip
    
    # ... (render_text and _wrap_text methods stay the same) ...
    
    def render_text(self, text, font, font_size, color, bold, shadow, outline, outline_width,
                background=None, bg_opacity=0.7, bg_padding=20):
        """
        Render text with optional background for readability.
        FIXED: Proper variable initialization.
        """
        # Convert color
        if isinstance(color, str):
            color = hex_to_rgb(color)
        
        # Scale font for resolution
        base_reference = 720
        frame_scale = self.height / base_reference
        actual_font_size = int(font_size * frame_scale * 1.5)
        
        # Load font - simple direct loading
        font_name = font  # Use font name as-is from config

        try:
            pil_font = ImageFont.truetype(font_name, actual_font_size)
            print(f"      ✅ Loaded font: {font_name}", flush=True)
        except Exception as e:
            # Fallback to Arial
            try:
                pil_font = ImageFont.truetype("arial.ttf", actual_font_size)
                print(f"      ⚠️  Font '{font_name}' not found, using Arial", flush=True)
            except:
                pil_font = ImageFont.load_default()
                print(f"      ⚠️  Using default font", flush=True)
        # Handle newlines
        text = text.replace('\\n', '\n')
        lines = text.split('\n')
        
        # Calculate text dimensions
        line_spacing = 1.2
        max_width = int(self.width * 0.9)
        
        # Wrap text
        wrapped_lines = []
        for line in lines:
            if line.strip():
                wrapped = self._wrap_text(line, pil_font, max_width)
                wrapped_lines.extend(wrapped)
            else:
                wrapped_lines.append('')
        
        # Get line dimensions
        line_height = int(actual_font_size * line_spacing)
        text_heights = []
        text_widths = []
        
        for line in wrapped_lines:
            if line.strip():
                try:
                    bbox = pil_font.getbbox(line)
                    text_widths.append(bbox[2] - bbox[0])
                    text_heights.append(bbox[3] - bbox[1])
                except:
                    # Fallback if getbbox fails
                    text_widths.append(len(line) * actual_font_size // 2)
                    text_heights.append(actual_font_size)
        
        # CRITICAL FIX: Ensure we always have values
        total_width = max(text_widths) if text_widths else actual_font_size * 5
        total_height = line_height * len(wrapped_lines) if wrapped_lines else line_height
        
        # Create image
        padding = 40
        img_width = int(total_width + padding * 2)
        img_height = int(total_height + padding * 2)
        
        # Create transparent canvas
        img = Image.new('RGBA', (img_width, img_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Draw text lines
        y = padding
        for line in wrapped_lines:
            if not line.strip():
                y += line_height
                continue
            
            try:
                bbox = pil_font.getbbox(line)
                line_width = bbox[2] - bbox[0]
            except:
                line_width = len(line) * actual_font_size // 2
            
            x = (img_width - line_width) // 2
            
            # Shadow
            if shadow:
                shadow_offset = max(3, actual_font_size // 30)
                for i in range(3, 0, -1):
                    offset = shadow_offset * i
                    alpha = 80 + (3 - i) * 40
                    draw.text((x + offset, y + offset), line, font=pil_font, 
                            fill=(0, 0, 0, alpha))
            
            # Outline
            if outline:
                outline_color = (0, 0, 0, 255)
                for ox in range(-outline_width, outline_width + 1):
                    for oy in range(-outline_width, outline_width + 1):
                        if abs(ox) == outline_width or abs(oy) == outline_width:
                            draw.text((x + ox, y + oy), line, font=pil_font, 
                                    fill=outline_color)
            
            # Main text
            draw.text((x, y), line, font=pil_font, fill=color + (255,))
            y += line_height
        
        if background and background != 'none':
            try:
                from src.effects.text_background import add_text_background
                # Determine background color (dark bg for light text, light bg for dark text)
                bg_brightness = sum(color) / 3
                if bg_brightness > 128:  # Light text
                    bg_color = (0, 0, 0)  # Dark background
                else:  # Dark text
                    bg_color = (255, 255, 255)  # Light background
                
                img = add_text_background(
                    img, 
                    style=background, 
                    opacity=bg_opacity, 
                    padding=bg_padding, 
                    color=bg_color
                )
                print(f"      Applied {background} background (opacity: {bg_opacity})", flush=True)
            except Exception as e:
                print(f"      ⚠️ Background failed: {e}", flush=True)
        
        return img
    
    def render_text_multicolor(self, text_lines, font, font_size, bold, shadow, outline, outline_width,
                           background=None, bg_opacity=0.7, bg_padding=20):
        """
        Render text with different colors per line.
        FIXED: Proper line spacing and background application.
        """
        from src.utils.helpers import hex_to_rgb
        
        # Scale font for resolution
        base_reference = 720
        frame_scale = self.height / base_reference
        actual_font_size = int(font_size * frame_scale * 1.5)
        
        # Load font
        font_name = font
        
        try:
            pil_font = ImageFont.truetype(font_name, actual_font_size)
        except:
            pil_font = ImageFont.truetype("arial.ttf", actual_font_size)
        
        # Ensure text_lines is a list
        if not isinstance(text_lines, list):
            text_lines = [{"text": str(text_lines), "color": "#FFFFFF"}]
        
        # Calculate dimensions
        line_spacing = 1.2
        max_width = int(self.width * 0.9)
        line_height = int(actual_font_size * line_spacing)
        
        # Wrap each line and calculate dimensions
        wrapped_lines = []
        for line_data in text_lines:
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
        
        # Ensure we have lines
        if not wrapped_lines:
            wrapped_lines = [{'text': 'ERROR', 'color': (255, 255, 255)}]
        
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
        
        # Create image with proper dimensions
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
            
            # ✅ CRITICAL: Move to next line position
            y += line_height
        
        # Apply background if specified
        if background and background != 'none':
            try:
                from src.effects.text_background import add_text_background
                bg_color = (0, 0, 0)  # Dark background for multi-color text
                
                img = add_text_background(
                    img, 
                    style=background, 
                    opacity=bg_opacity, 
                    padding=bg_padding, 
                    color=bg_color
                )
                print(f"      Applied {background} background (opacity: {bg_opacity})", flush=True)
            except Exception as e:
                print(f"      ⚠️ Background failed: {e}", flush=True)
        
        return img
        
    def _wrap_text(self, text, font, max_width):
        """Wrap text to fit max width."""
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

    def _parse_position(self, position):
        """
        Parse position config to pixel coordinates.
        Returns (x, y) where text should be centered.
        """
        if position == 'center':
            return (self.width // 2, self.height // 2)
        elif position == 'top':
            return (self.width // 2, int(self.height * 0.15))
        elif position == 'bottom':
            return (self.width // 2, int(self.height * 0.85))
        elif isinstance(position, list):
            x, y = position
            
            # Parse x
            if x == 'center':
                x = self.width // 2
            elif isinstance(x, float) and x <= 1.0:
                x = int(self.width * x)
            elif isinstance(x, int):
                x = x
            else:
                x = self.width // 2
            
            # Parse y
            if y == 'center':
                y = self.height // 2
            elif isinstance(y, float) and y <= 1.0:
                y = int(self.height * y)
            elif isinstance(y, int):
                y = y
            else:
                y = self.height // 2
            
            return (x, y)
        
        # Default to center
        return (self.width // 2, self.height // 2)
    
    def generate_animation_frames(self, text_img, animation, duration, start_time, pos_x, pos_y):
        """
        Generate all animation frames.
        NOW ACCEPTS pos_x, pos_y for positioning.
        """
        total_frames = int(duration * self.fps)
        frames = []
        
        # Choose animation generator - PASS POSITION
        if 'fade' in animation.lower():
            frames = self._animate_fade(text_img, total_frames, start_time, pos_x, pos_y)
        
        elif 'slide' in animation.lower() and 'left' in animation.lower():
            frames = self._animate_slide(text_img, total_frames, start_time, 'left', pos_x, pos_y)
        
        elif 'slide' in animation.lower() and 'right' in animation.lower():
            frames = self._animate_slide(text_img, total_frames, start_time, 'right', pos_x, pos_y)
        
        elif 'slide' in animation.lower() and 'bottom' in animation.lower():
            frames = self._animate_slide(text_img, total_frames, start_time, 'bottom', pos_x, pos_y)
        
        elif 'slide' in animation.lower() and 'top' in animation.lower():
            frames = self._animate_slide(text_img, total_frames, start_time, 'top', pos_x, pos_y)
        
        elif 'scale' in animation.lower() or 'zoom' in animation.lower() or 'grow' in animation.lower():
            frames = self._animate_scale(text_img, total_frames, start_time, pos_x, pos_y)
        
        elif 'pop' in animation.lower() or 'bounce' in animation.lower():
            frames = self._animate_pop(text_img, total_frames, start_time, pos_x, pos_y)
        
        else:
            frames = self._animate_fade(text_img, total_frames, start_time, pos_x, pos_y)
        
        return frames
    
    def _animate_fade(self, text_img, total_frames, start_time, pos_x, pos_y):
        """
        Generate fade-in animation frames.
        FIXED: Uses pos_x, pos_y instead of auto-centering.
        """
        frames = []
        anim_frames = int(0.8 * self.fps)
        start_frame = int(start_time * self.fps)
        
        for i in range(total_frames):
            canvas = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
            
            if i < start_frame:
                pass
            elif i < start_frame + anim_frames:
                progress = (i - start_frame) / anim_frames
                alpha_img = text_img.copy()
                alpha_img.putalpha(ImageEnhance.Brightness(text_img.split()[3]).enhance(progress))
                
                # FIXED: Use provided position (centered on pos_x, pos_y)
                x = pos_x - text_img.width // 2
                y = pos_y - text_img.height // 2
                canvas.paste(alpha_img, (x, y), alpha_img)
            else:
                # FIXED: Use provided position
                x = pos_x - text_img.width // 2
                y = pos_y - text_img.height // 2
                canvas.paste(text_img, (x, y), text_img)
            
            frames.append(np.array(canvas))
        
        return frames

    def _animate_slide(self, text_img, total_frames, start_time, direction, pos_x, pos_y):
        """FIXED: Uses pos_x, pos_y for final position."""
        frames = []
        anim_frames = int(0.8 * self.fps)
        start_frame = int(start_time * self.fps)
        
        for i in range(total_frames):
            canvas = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
            
            if i < start_frame:
                pass
            elif i < start_frame + anim_frames:
                progress = (i - start_frame) / anim_frames
                progress = 1 - pow(1 - progress, 3)
                
                # Calculate final position (centered on pos_x, pos_y)
                final_x = pos_x - text_img.width // 2
                final_y = pos_y - text_img.height // 2
                
                # Calculate slide start positions
                if direction == 'left':
                    x = int(-text_img.width + (text_img.width + final_x) * progress)
                    y = final_y
                elif direction == 'right':
                    x = int(self.width + (final_x - self.width) * progress)
                    y = final_y
                elif direction == 'bottom':
                    x = final_x
                    y = int(self.height + (final_y - self.height) * progress)
                elif direction == 'top':
                    x = final_x
                    y = int(-text_img.height + (text_img.height + final_y) * progress)
                
                # Fade during slide
                if progress < 0.3:
                    alpha_mult = progress / 0.3
                    img_copy = text_img.copy()
                    img_copy.putalpha(ImageEnhance.Brightness(text_img.split()[3]).enhance(alpha_mult))
                    canvas.paste(img_copy, (x, y), img_copy)
                else:
                    canvas.paste(text_img, (x, y), text_img)
            else:
                # Final position
                x = pos_x - text_img.width // 2
                y = pos_y - text_img.height // 2
                canvas.paste(text_img, (x, y), text_img)
            
            frames.append(np.array(canvas))
        
        return frames

    def _animate_scale(self, text_img, total_frames, start_time, pos_x, pos_y):
        """FIXED: Uses pos_x, pos_y."""
        frames = []
        anim_frames = int(0.7 * self.fps)
        start_frame = int(start_time * self.fps)
        
        for i in range(total_frames):
            canvas = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
            
            if i < start_frame:
                pass
            elif i < start_frame + anim_frames:
                progress = (i - start_frame) / anim_frames
                progress = 1 - pow(1 - progress, 3)
                scale = 0.3 + 0.7 * progress
                
                new_size = (int(text_img.width * scale), int(text_img.height * scale))
                if new_size[0] > 0 and new_size[1] > 0:
                    scaled = text_img.resize(new_size, Image.Resampling.LANCZOS)
                    
                    # FIXED: Center on pos_x, pos_y
                    x = pos_x - scaled.width // 2
                    y = pos_y - scaled.height // 2
                    
                    if progress < 0.4:
                        alpha_mult = progress / 0.4
                        scaled_copy = scaled.copy()
                        scaled_copy.putalpha(ImageEnhance.Brightness(scaled.split()[3]).enhance(alpha_mult))
                        canvas.paste(scaled_copy, (x, y), scaled_copy)
                    else:
                        canvas.paste(scaled, (x, y), scaled)
            else:
                x = pos_x - text_img.width // 2
                y = pos_y - text_img.height // 2
                canvas.paste(text_img, (x, y), text_img)
            
            frames.append(np.array(canvas))
        
        return frames

    def _animate_pop(self, text_img, total_frames, start_time, pos_x, pos_y):
        """FIXED: Uses pos_x, pos_y."""
        frames = []
        anim_frames = int(0.5 * self.fps)
        start_frame = int(start_time * self.fps)
        
        for i in range(total_frames):
            canvas = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
            
            if i < start_frame:
                pass
            elif i < start_frame + anim_frames:
                progress = (i - start_frame) / anim_frames
                
                if progress < 0.5:
                    scale = 0.3 + 0.9 * (progress * 2)
                else:
                    scale = 1.2 - 0.2 * ((progress - 0.5) * 2)
                
                new_size = (int(text_img.width * scale), int(text_img.height * scale))
                if new_size[0] > 0 and new_size[1] > 0:
                    scaled = text_img.resize(new_size, Image.Resampling.LANCZOS)
                    
                    # FIXED: Center on pos_x, pos_y
                    x = pos_x - scaled.width // 2
                    y = pos_y - scaled.height // 2
                    
                    if progress < 0.2:
                        alpha_mult = progress / 0.2
                        scaled_copy = scaled.copy()
                        scaled_copy.putalpha(ImageEnhance.Brightness(scaled.split()[3]).enhance(alpha_mult))
                        canvas.paste(scaled_copy, (x, y), scaled_copy)
                    else:
                        canvas.paste(scaled, (x, y), scaled)
            else:
                x = pos_x - text_img.width // 2
                y = pos_y - text_img.height // 2
                canvas.paste(text_img, (x, y), text_img)
            
            frames.append(np.array(canvas))
        
        return frames