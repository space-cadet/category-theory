# PDF Chapter Extractor Workflow

Given a PDF file, extract chapters into separate files:

1. Use `pdftotext -f 1 -l 10 [PDF_PATH] -` to extract table of contents
2. Parse chapter titles and logical page numbers from TOC output
3. Find actual PDF page offset by checking where first chapter starts using `pdftotext -f [PAGE] -l [PAGE]`
4. Calculate: PDF_PAGE = LOGICAL_PAGE + OFFSET
5. For each chapter: use `qpdf [PDF_PATH] --pages . [START_PAGE]-[END_PAGE] -- [OUTPUT_PATH]`
6. Name files as: `Chapter_[NUM]_[Title_Words].pdf`
7. If user specifies chapter range, process only those chapters; otherwise extract all
8. For end matter (appendices, index, etc.), extract from final logical page to PDF end
9. Use `pdfinfo [PDF_PATH] | grep Pages` to determine total page count

Input: PDF path, optional chapter range (e.g., "1-5")
Output: Individual chapter PDF files in same directory

## Example Usage (CTFP Book)
- Source: "Category Theory for Programmers" by Bartosz Milewski
- Total pages: 498 PDF pages
- Page offset: 18 (logical page 2 = PDF page 20)
- Extracted: 31 chapters + end matter
- Output: Chapter_01_Category_The_Essence_of_Composition.pdf through Chapter_31_Monads_Monoids_and_Categories.pdf + End_Matter.pdf