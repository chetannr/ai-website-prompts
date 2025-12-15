# Utilities and Scripts

> **Purpose**: Reusable Python scripts for website content extraction, image processing, and data preparation.

---

## 📦 Available Scripts

### 1. `extract_website_content.py`

**Purpose**: Extract content and images from existing websites for migration or content extraction.

**Features**:
- Downloads images from URLs
- Extracts structured content (mission, about, impact, testimonials, etc.)
- Saves content as JSON
- Organizes images in a structured directory

**Usage**:
```bash
python3 extract_website_content.py
```

**Output**:
- `website_content.json` - Structured content data
- `images/` directory - Downloaded images organized by type

**Dependencies**:
```bash
pip install requests
```

**Configuration**:
- Edit `WEBSITE_CONTENT` dictionary in the script to define content structure
- Edit `IMAGE_URLS` dictionary to specify image URLs to download

---

### 2. `extract_pptx_content.py`

**Purpose**: Extract images and text from PowerPoint presentations for website development.

**Features**:
- Extracts all images from PowerPoint slides
- Extracts text content from each slide
- Generates structured JSON output
- Creates organized image directory
- Handles grouped shapes and nested content

**Usage**:
```bash
python3 extract_pptx_content.py
```

**Requirements**:
- PowerPoint file named `LAW PARK.pptx` in the script directory (or modify path in script)

**Output**:
- `extracted_content/slides_data.json` - Structured slide data
- `extracted_content/images/` - Extracted images with meaningful filenames

**Dependencies**:
```bash
pip install python-pptx
```

**Configuration**:
- Modify `pptx_path` variable to point to your PowerPoint file
- Adjust `output_dir` to change output location

---

### 3. `compress_images.py`

**Purpose**: Compress images for web use while maintaining good quality.

**Features**:
- Compresses JPEG, PNG, and other image formats
- Resizes images to maximum dimensions (default: 1920px)
- Converts PNG to JPEG when beneficial (30%+ size reduction)
- Maintains quality while reducing file size
- Updates JSON references if files are renamed (PNG → JPG)

**Usage**:
```bash
python3 compress_images.py
```

**Configuration**:
- `quality=85` - JPEG quality (1-100, higher is better)
- `max_dimension=1920` - Maximum width/height in pixels
- `images_dir` - Directory containing images to compress
- `json_path` - Optional JSON file to update if images are renamed

**Output**:
- Compressed images (overwrites originals or saves to new location)
- Compression summary with statistics
- Updated JSON file (if provided and files renamed)

**Dependencies**:
```bash
pip install Pillow
```

**Example Output**:
```
Found 50 images to compress...
Settings: Quality=85, Max dimension=1920px

Compressing: image1.jpg (2500.5 KB) -> image1.jpg (450.2 KB, 82.0% reduction)
...

Compression Summary:
  Images processed: 50/50
  Original total size: 125.50 MB
  Compressed total size: 22.50 MB
  Total reduction: 82.1%
  Space saved: 103.00 MB
```

---

## 🚀 Setup

### Install Dependencies

Create a `requirements.txt`:
```txt
requests>=2.31.0
python-pptx>=0.6.23
Pillow>=10.0.0
```

Install:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install requests python-pptx Pillow
```

---

## 📝 Usage Examples

### Extract Content from Website

1. Edit `extract_website_content.py`:
   - Update `WEBSITE_CONTENT` with your content structure
   - Update `IMAGE_URLS` with image URLs to download

2. Run:
   ```bash
   python3 extract_website_content.py
   ```

3. Use the output:
   - Import `website_content.json` into your project
   - Use images from the `images/` directory

### Extract from PowerPoint

1. Place your PowerPoint file in the script directory (or update path)

2. Run:
   ```bash
   python3 extract_pptx_content.py
   ```

3. Review output:
   - Check `extracted_content/slides_data.json` for structured data
   - Use images from `extracted_content/images/`

### Compress Images

1. Place images in `extracted_content/images/` (or update path)

2. Run:
   ```bash
   python3 compress_images.py
   ```

3. Review compression statistics and use optimized images

---

## 🔧 Customization

### Adjusting Image Compression

Edit `compress_images.py`:
```python
# Change quality (1-100)
compress_all_images(images_dir, quality=90, max_dimension=2560)

# Change max dimensions
compress_all_images(images_dir, quality=85, max_dimension=1440)
```

### Changing Output Directories

Edit script paths:
```python
# In extract_pptx_content.py
output_dir = script_dir / "my_custom_output"

# In compress_images.py
images_dir = script_dir / "my_images"
```

### Processing Different File Types

The scripts can be extended to:
- Process Word documents (`.docx`)
- Extract from PDFs
- Process Excel files
- Handle other content sources

---

## 📋 Best Practices

### Image Compression
- **Quality**: 85 is a good balance (80-90 range recommended)
- **Max Dimension**: 1920px for most web use (1440px for mobile-first)
- **Format**: Prefer JPEG for photos, PNG for graphics with transparency
- **WebP**: Consider converting to WebP for even better compression

### Content Extraction
- **Structure**: Define clear content structure before extraction
- **Validation**: Verify extracted content matches source
- **Organization**: Use consistent naming conventions for files

### File Organization
- Keep scripts in a dedicated `scripts/` or `utilities/` directory
- Organize output in project-specific directories
- Use version control for scripts (not for generated content)

---

## 🐛 Troubleshooting

### Images Not Downloading
- Check internet connection
- Verify URLs are accessible
- Check file permissions for output directory

### PowerPoint Extraction Issues
- Ensure `.pptx` file is not corrupted
- Check file path is correct
- Verify `python-pptx` is installed correctly

### Compression Errors
- Ensure images are valid formats (JPEG, PNG)
- Check file permissions
- Verify Pillow is installed correctly

---

## 🔄 Integration with Website Projects

### Typical Workflow

1. **Content Extraction**:
   ```bash
   python3 extract_website_content.py
   # or
   python3 extract_pptx_content.py
   ```

2. **Image Optimization**:
   ```bash
   python3 compress_images.py
   ```

3. **Import to Project**:
   - Copy JSON data to `src/data/` directory
   - Copy optimized images to `public/images/` directory
   - Import and use in React components

### Example Integration

```typescript
// src/data/content.ts
import websiteContent from './website_content.json';

export const mission = websiteContent.mission;
export const about = websiteContent.about;
export const testimonials = websiteContent.testimonials;
```

```tsx
// src/components/sections/About.tsx
import { about } from '../../data/content';

export function About() {
  return (
    <section>
      <h2>{about.title}</h2>
      <p>{about.description}</p>
    </section>
  );
}
```

---

## 📚 Additional Resources

### Python Libraries
- [Requests Documentation](https://requests.readthedocs.io/)
- [python-pptx Documentation](https://python-pptx.readthedocs.io/)
- [Pillow Documentation](https://pillow.readthedocs.io/)

### Image Optimization
- [WebP Conversion](https://developers.google.com/speed/webp)
- [Image Optimization Guide](https://web.dev/fast/#optimize-your-images)

---

## ✅ Checklist

Before using scripts:
- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Script paths configured correctly
- [ ] Output directories exist or will be created
- [ ] Source files accessible (PowerPoint, URLs, etc.)

After running scripts:
- [ ] Verify output files created
- [ ] Check image quality (if compressed)
- [ ] Validate JSON structure
- [ ] Test importing data into project
- [ ] Verify images load correctly

---

*These scripts are reusable utilities for all website projects. Keep them updated and extend as needed for new use cases.*
