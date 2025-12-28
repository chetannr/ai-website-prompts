#!/usr/bin/env python3
"""
Extract all text content from PDF file and convert to markdown.
Preserves structure, topics, and concepts for future reference.
"""

import sys
from pathlib import Path

try:
    import pypdf
except ImportError:
    print("Installing pypdf...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    import pypdf

def extract_pdf_to_markdown(pdf_path, output_path):
    """Extract all content from PDF and save as markdown."""
    print(f"Reading PDF: {pdf_path}")
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        total_pages = len(pdf_reader.pages)
        
        print(f"Total pages: {total_pages}")
        print("Extracting content...")
        
        markdown_content = []
        markdown_content.append("# Refactoring UI - Complete Guide\n\n")
        markdown_content.append(f"*Extracted from: {pdf_path.name}*\n\n")
        markdown_content.append("---\n\n")
        
        for page_num, page in enumerate(pdf_reader.pages, start=1):
            if page_num % 10 == 0:
                print(f"  Processing page {page_num}/{total_pages}...")
            
            text = page.extract_text()
            
            if text.strip():
                # Add page marker
                markdown_content.append(f"## Page {page_num}\n\n")
                
                # Process text to preserve structure
                lines = text.split('\n')
                processed_lines = []
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Detect headings (lines that are short and might be titles)
                    # This is a heuristic - adjust as needed
                    if len(line) < 100 and not line.endswith('.') and not line.endswith(','):
                        # Check if it looks like a heading
                        if line.isupper() or (line[0].isupper() and len(line.split()) <= 10):
                            processed_lines.append(f"### {line}\n")
                        else:
                            processed_lines.append(f"{line}\n")
                    else:
                        processed_lines.append(f"{line}\n")
                
                markdown_content.extend(processed_lines)
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
    
    extract_pdf_to_markdown(pdf_path, output_path)

if __name__ == "__main__":
    main()

