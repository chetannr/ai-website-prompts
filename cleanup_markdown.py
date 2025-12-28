#!/usr/bin/env python3
"""
Clean up the extracted markdown by removing page numbers and improving structure.
"""

import re
from pathlib import Path

def cleanup_markdown(input_path, output_path):
    """Clean up markdown content."""
    print(f"Reading: {input_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    cleaned_lines = []
    prev_line = ""
    
    for i, line in enumerate(lines):
        original_line = line
        
        # Remove standalone page number lines like "9 Start with a feature, not a layout"
        # Keep the topic, remove the number
        line = re.sub(r'^(\d+)\s+(.+)$', r'\2', line)
        
        # Remove trailing page numbers like "Start with a feature, not a layout 9"
        line = re.sub(r'^(.+?)\s+(\d{1,3})$', r'\1', line)
        
        # Remove lines that are just page numbers
        if re.match(r'^(\d+|Page \d+)$', line.strip()):
            # Skip if it's a page marker we want to keep, otherwise skip
            if not line.strip().startswith('## Page'):
                continue
        
        # Clean up page markers - make them less prominent
        if line.strip().startswith('## Page'):
            # Convert to HTML comment
            page_num = re.search(r'Page (\d+)', line)
            if page_num:
                cleaned_lines.append(f"\n<!-- Page {page_num.group(1)} -->\n")
            continue
        
        # Remove duplicate separators
        if line.strip() == '---' and prev_line.strip() == '---':
            continue
        
        # Clean up excessive blank lines (more than 2 consecutive)
        if line.strip() == '' and prev_line.strip() == '':
            # Check if next line is also blank
            if i + 1 < len(lines) and lines[i + 1].strip() == '':
                continue
        
        cleaned_lines.append(line)
        prev_line = line
    
    # Join and write
    cleaned_content = '\n'.join(cleaned_lines)
    
    # Final cleanup: remove more than 2 consecutive blank lines
    cleaned_content = re.sub(r'\n{4,}', '\n\n\n', cleaned_content)
    
    print(f"Writing cleaned content to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print("✓ Cleanup complete!")

def main():
    script_dir = Path(__file__).parent
    input_path = script_dir / "REFACTORING_UI_COMPLETE_GUIDE.md"
    output_path = script_dir / "REFACTORING_UI_COMPLETE_GUIDE.md"
    
    if not input_path.exists():
        print(f"Error: File not found at {input_path}")
        return
    
    cleanup_markdown(input_path, output_path)

if __name__ == "__main__":
    main()

