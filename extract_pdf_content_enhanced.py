#!/usr/bin/env python3
"""
Enhanced PDF extraction with better structure, page number removal, and topic organization.
"""

import sys
import re
from pathlib import Path

try:
    import pypdf
except ImportError:
    print("Installing pypdf...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    import pypdf

def clean_text(text):
    """Clean extracted text by removing page numbers and formatting issues."""
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Remove standalone page numbers (e.g., "9 Start with a feature" -> "Start with a feature")
        # Pattern: number at start or end of line followed by topic name
        line = re.sub(r'^\d+\s+(.+)$', r'\1', line)
        line = re.sub(r'^(.+?)\s+\d+$', r'\1', line)
        
        # Remove page number references like "Page 9" when standalone
        if re.match(r'^Page \d+$', line):
            continue
        
        # Remove trailing page numbers in format "topic name 9"
        line = re.sub(r'^(.+?)\s+\d{1,3}$', r'\1', line)
        
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def detect_heading(line, prev_line=""):
    """Detect if a line is likely a heading."""
    line = line.strip()
    
    # Skip empty lines
    if not line:
        return False
    
    # Lines that are all uppercase and short are likely headings
    if line.isupper() and len(line) < 80:
        return True
    
    # Lines that start with capital and are short (likely section titles)
    if line[0].isupper() and len(line) < 100 and not line.endswith('.') and not line.endswith(','):
        # Check if it's a question (likely not a heading in this context)
        if line.endswith('?'):
            return False
        # If previous line was empty or a heading, this might be a heading
        if not prev_line.strip() or detect_heading(prev_line):
            return True
    
    return False

def extract_pdf_to_markdown_enhanced(pdf_path, output_path):
    """Extract all content from PDF with enhanced structure."""
    print(f"Reading PDF: {pdf_path}")
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        total_pages = len(pdf_reader.pages)
        
        print(f"Total pages: {total_pages}")
        print("Extracting and processing content...")
        
        markdown_content = []
        markdown_content.append("# Refactoring UI - Complete Guide\n\n")
        markdown_content.append("*Extracted from: refactoring-ui_compress 2.pdf*\n\n")
        markdown_content.append("---\n\n")
        markdown_content.append("## Table of Contents\n\n")
        
        # First pass: extract all content
        all_pages_content = []
        for page_num, page in enumerate(pdf_reader.pages, start=1):
            if page_num % 50 == 0:
                print(f"  Processing page {page_num}/{total_pages}...")
            
            text = page.extract_text()
            if text.strip():
                all_pages_content.append((page_num, text))
        
        # Build table of contents from first few pages
        toc_section = False
        toc_lines = []
        for page_num, text in all_pages_content[:10]:
            if "Contents" in text or "Table of Contents" in text:
                toc_section = True
            if toc_section:
                lines = text.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith("Page") and len(line) > 5:
                        # Extract topic names (usually before page numbers)
                        match = re.match(r'^(.+?)\s+\.+\s*\d+$', line)
                        if match:
                            topic = match.group(1).strip()
                            if topic and len(topic) > 3:
                                toc_lines.append(f"- {topic}\n")
                if page_num > 5 and not any("Contents" in t for t in [all_pages_content[i][1] for i in range(max(0, page_num-2), min(len(all_pages_content), page_num+1))]):
                    toc_section = False
        
        if toc_lines:
            markdown_content.extend(toc_lines)
        markdown_content.append("\n---\n\n")
        
        # Second pass: process and write content
        print("Organizing content...")
        prev_line = ""
        current_section = ""
        
        for page_num, text in all_pages_content:
            if page_num % 50 == 0:
                print(f"  Organizing page {page_num}/{total_pages}...")
            
            # Clean the text
            cleaned_text = clean_text(text)
            
            if not cleaned_text.strip():
                continue
            
            lines = cleaned_text.split('\n')
            
            # Add page marker (less prominent)
            markdown_content.append(f"<!-- Page {page_num} -->\n\n")
            
            for line in lines:
                line = line.strip()
                if not line:
                    markdown_content.append("\n")
                    prev_line = ""
                    continue
                
                # Skip page number only lines
                if re.match(r'^Page \d+$', line) or re.match(r'^\d+$', line):
                    continue
                
                # Detect and format headings
                if detect_heading(line, prev_line):
                    # Check if it's a major section (all caps or very prominent)
                    if line.isupper() and len(line) < 60:
                        markdown_content.append(f"## {line}\n\n")
                        current_section = line
                    else:
                        markdown_content.append(f"### {line}\n\n")
                else:
                    # Regular content
                    markdown_content.append(f"{line}\n\n")
                
                prev_line = line
            
            markdown_content.append("\n---\n\n")
        
        # Write to markdown file
        print(f"\nWriting markdown to: {output_path}")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(markdown_content))
        
        print(f"✓ Extraction complete!")
        print(f"  - Pages processed: {total_pages}")
        print(f"  - Output saved to: {output_path}")

def main():
    """Main extraction function."""
    script_dir = Path(__file__).parent
    pdf_path = script_dir / "refactoring-ui_compress 2.pdf"
    output_path = script_dir / "REFACTORING_UI_COMPLETE_GUIDE.md"
    
    if not pdf_path.exists():
        print(f"Error: PDF file not found at {pdf_path}")
        return
    
    extract_pdf_to_markdown_enhanced(pdf_path, output_path)

if __name__ == "__main__":
    main()

