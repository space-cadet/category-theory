# PDF CLI Content Extraction
*Created: 2025-09-22 12:57:00 IST*
*Last Updated: 2025-09-22 12:57:00 IST*

## Overview
Documentation for extracting structured content from PDF files using CLI tools, specifically for academic documents with mathematical expressions and complex layouts.

## Problem Statement
Need to extract text content from "Milewski_Category Theory for Programmers_2014.pdf" (17 MB) while preserving:
- Document structure (headings, sections)
- Mathematical expressions in LaTeX format  
- Tables and figures
- Text formatting

## Tool Evaluation

### Traditional Text Extraction Issues
- **pdftotext**: Fast but loses word boundaries, joins text together
- **pdfplumber**: Better structure preservation but still has formatting issues
- Both struggle with mathematical expressions

### Advanced Solutions

#### Commercial Tools
1. **Mathpix Snip** - Industry leader
   - CLI: `npm install -g @mathpix/mpx-cli`
   - Excellent math formula recognition
   - Preserves document structure
   - Outputs LaTeX, Markdown, DOCX

2. **Underleaf PDF to LaTeX**
   - AI-powered conversion
   - 5-page processing limit
   - Handles complex academic documents

#### Open Source Solutions
1. **Pix2Text** - Free Mathpix alternative
   - Install: `pip install pix2text`
   - Supports 80+ languages
   - Layout analysis and table recognition
   - Outputs structured Markdown with LaTeX math

2. **LaTeX-OCR** 
   - Install: `pip install pix2tex`
   - Specialized for mathematical formulas
   - CLI: `pix2tex /path/to/image`

3. **Surya** (successor to Texify)
   - Install: `pip install surya-ocr`
   - Command: `surya_latex_ocr`

## Implementation: Pix2Text Setup

### Installation with UV
```bash
# Create isolated environment
uv venv pix2text-env
source pix2text-env/bin/activate
uv pip install pix2text
```

### Usage Commands

#### Full Document Extraction
```bash
./pix2text-env/bin/p2t predict "docs/Milewski_Category Theory for Programmers_2014.pdf" -o category_theory_extracted.md
```

#### Page Range Extraction (First 20 pages)
```bash
./pix2text-env/bin/p2t predict "docs/Milewski_Category Theory for Programmers_2014.pdf" --page-numbers "1-20" -o category_theory_first20.md
```

#### Specific Pages
```bash
./pix2text-env/bin/p2t predict "docs/Milewski_Category Theory for Programmers_2014.pdf" --page-numbers "1,3,5-10,15-20" -o category_theory_selected.md
```

### PATH Resolution Issues
- Conda/miniconda installations can conflict with uv environments
- Solution: Use full path to uv environment binary
- Alternative: `conda deactivate` before activating uv environment

## Technical Notes

### Output Format
- Structured Markdown with preserved layouts
- Mathematical expressions in LaTeX format
- Tables converted to Markdown tables
- Figures referenced with proper captions

### Performance Considerations  
- Tool downloads models on first run
- Page range extraction significantly reduces processing time
- Memory usage scales with document size

### Quality Factors
- Higher DPI images improve OCR accuracy
- Academic documents with complex layouts work well
- Mathematical formulas recognition is highly accurate

## Next Steps
1. Test extraction on first 20 pages for quality assessment
2. Compare output quality with pdftotext baseline
3. Evaluate mathematical formula accuracy
4. Consider batch processing for multiple documents

## File References
- Source: `docs/Milewski_Category Theory for Programmers_2014.pdf` (17 MB)
- Extracted text: `docs/Milewski_Category Theory for Programmers_2014.txt` (590 KB, poor formatting)
- Target output: Structured Markdown with LaTeX math expressions
