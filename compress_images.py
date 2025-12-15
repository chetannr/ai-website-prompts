#!/usr/bin/env python3
"""
Compress images for web use while maintaining good quality.
"""

import os
from pathlib import Path
from PIL import Image
import json

def compress_image(input_path, output_path=None, quality=85, max_width=1920, max_height=1920):
    """
    Compress an image for web use.
    
    Args:
        input_path: Path to input image
        output_path: Path to save compressed image (if None, overwrites input)
        quality: JPEG/PNG quality (1-100, higher is better)
        max_width: Maximum width in pixels
        max_height: Maximum height in pixels
    """
    if output_path is None:
        output_path = input_path
    
    try:
        with Image.open(input_path) as img:
            # Convert RGBA to RGB if needed (for JPEG compatibility)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background for transparent images
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize if image is too large
            original_size = img.size
            if img.width > max_width or img.height > max_height:
                img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
                print(f"  Resized: {original_size} -> {img.size}")
            
            # Get file extension
            ext = Path(input_path).suffix.lower()
            
            # Save with optimization
            if ext in ('.jpg', '.jpeg'):
                img.save(output_path, 'JPEG', quality=quality, optimize=True)
            elif ext == '.png':
                # For PNG, use optimize flag and convert to JPEG if significantly larger
                # Save as PNG first
                img.save(output_path, 'PNG', optimize=True, compress_level=9)
                
                # Check if converting to JPEG would be better
                png_size = os.path.getsize(output_path)
                jpeg_path = output_path.with_suffix('.jpg')
                img.save(jpeg_path, 'JPEG', quality=quality, optimize=True)
                jpeg_size = os.path.getsize(jpeg_path)
                
                # If JPEG is significantly smaller (more than 30% reduction), use it
                if jpeg_size < png_size * 0.7:
                    os.remove(output_path)
                    return jpeg_path
                else:
                    os.remove(jpeg_path)
            else:
                # For other formats, save as JPEG
                output_path = output_path.with_suffix('.jpg')
                img.save(output_path, 'JPEG', quality=quality, optimize=True)
            
            return output_path
            
    except Exception as e:
        print(f"  Error compressing {input_path}: {e}")
        return None

def compress_all_images(images_dir, quality=85, max_dimension=1920):
    """Compress all images in a directory."""
    images_dir = Path(images_dir)
    
    if not images_dir.exists():
        print(f"Error: Directory {images_dir} does not exist")
        return
    
    image_files = list(images_dir.glob('*.png')) + list(images_dir.glob('*.jpg')) + list(images_dir.glob('*.jpeg'))
    
    if not image_files:
        print("No images found to compress")
        return
    
    print(f"Found {len(image_files)} images to compress...")
    print(f"Settings: Quality={quality}, Max dimension={max_dimension}px\n")
    
    total_original_size = 0
    total_compressed_size = 0
    compressed_count = 0
    renamed_files = {}  # Track any file renames (PNG -> JPG)
    
    for img_path in image_files:
        original_size = os.path.getsize(img_path)
        total_original_size += original_size
        
        print(f"Compressing: {img_path.name} ({original_size / 1024:.1f} KB)", end=" -> ")
        
        compressed_path = compress_image(img_path, quality=quality, max_width=max_dimension, max_height=max_dimension)
        
        if compressed_path and compressed_path.exists():
            compressed_size = os.path.getsize(compressed_path)
            total_compressed_size += compressed_size
            compressed_count += 1
            
            reduction = ((original_size - compressed_size) / original_size) * 100
            print(f"{compressed_path.name} ({compressed_size / 1024:.1f} KB, {reduction:.1f}% reduction)")
            
            # Track if filename changed (PNG -> JPG)
            if compressed_path.name != img_path.name:
                renamed_files[img_path.name] = compressed_path.name
        else:
            print("FAILED")
    
    print(f"\n{'='*60}")
    print(f"Compression Summary:")
    print(f"  Images processed: {compressed_count}/{len(image_files)}")
    print(f"  Original total size: {total_original_size / (1024*1024):.2f} MB")
    print(f"  Compressed total size: {total_compressed_size / (1024*1024):.2f} MB")
    print(f"  Total reduction: {((total_original_size - total_compressed_size) / total_original_size) * 100:.1f}%")
    print(f"  Space saved: {(total_original_size - total_compressed_size) / (1024*1024):.2f} MB")
    
    return renamed_files

def update_json_paths(json_path, renamed_files):
    """Update JSON file if any images were renamed (PNG -> JPG)."""
    if not renamed_files:
        return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated = False
    for slide in data:
        for img in slide.get('images', []):
            old_filename = img['filename']
            if old_filename in renamed_files:
                new_filename = renamed_files[old_filename]
                img['filename'] = new_filename
                # Update path
                old_path = img['path']
                img['path'] = old_path.rsplit('.', 1)[0] + '.' + new_filename.split('.')[-1]
                updated = True
    
    if updated:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\nUpdated {json_path} with new image filenames")

def main():
    """Main compression function."""
    script_dir = Path(__file__).parent
    images_dir = script_dir / "extracted_content" / "images"
    json_path = script_dir / "extracted_content" / "slides_data.json"
    
    # Compress images
    renamed_files = compress_all_images(images_dir, quality=85, max_dimension=1920)
    
    # Update JSON if files were renamed
    if renamed_files and json_path.exists():
        update_json_paths(json_path, renamed_files)

if __name__ == "__main__":
    main()

