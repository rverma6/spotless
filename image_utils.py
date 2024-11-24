from PIL import Image
import io

def optimize_image(image, max_size=(800, 800), quality=85):
    """Optimize image size and quality before sending to API"""
    img = Image.open(image)
    
    # Convert to RGB if needed
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    
    # Resize if larger than max_size
    if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
    
    # Save optimized image
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=quality, optimize=True)
    return buffer.getvalue()