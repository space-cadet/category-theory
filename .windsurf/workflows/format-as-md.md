---
description: Format a file as markdown with math support, TOC, and semantic analysis
auto_execution_mode: 1
---

# Markdown Formatting Workflow

This workflow formats a given file as markdown with:
- Proper math expression formatting
- Generated table of contents
- Semantic analysis to determine appropriate formatting style

All meaningful content must be preserved (no deletions or modifications of substantive content other than to add or fix formatting)

## Steps

## Conditional Parsing Structure

1. **File Analysis Phase**
   ```pseudo
   if (file_contains_chat_patterns) {
     format_as_chat_session();
   } else if (file_contains_math_expressions) {
     format_as_technical_content();
   } else if (file_contains_long_paragraphs) {
     format_as_long_form();
   } else {
     apply_basic_formatting();
   }
   ```

2. **Chat Session Formatting**
   - Add **Question** and **Answer** labels before each message
   - Preserve all original content exactly
   - Group consecutive messages from same speaker
   - Maintain code blocks, math, and quotes within messages
   - Optional: Add timestamps if present in original

   Pseudocode
   ```pseudo
   lines = read(file)
   messages = []
   current = {speaker: None, time: None, body: []}
   for line in lines:
     if matches_label(line):
       flush(current, messages)
       spk, ts = parse_label_and_time(line)
       current = {speaker: normalize(spk), time: ts, body: []}
     else if looks_like_timestamp_header(line) and current.speaker is not None and is_start_of_message(line):
       # attach timestamp to current message
       current.time = normalize_time(extract_time(line))
     else:
       # content line
       current.body.append(line)
   flush(current, messages)

   # Post-process: infer missing speakers in alternating dialogues
   infer_missing_speakers(messages)
   group_consecutive_same_speaker(messages)

   # Render
   out = []
   ensure_session_heading(out)
   for m in messages:
     out.append(format_heading_line(m.speaker, m.time))
     out.extend(format_body(m.body))
   write(file, out)
   ```

3. **Technical Content Formatting**
   - Standardize math expressions between $...$ and $$...$$
   - Add equation numbering if needed
   - Generate hierarchical TOC
   - Format code blocks with language detection

4. **Long Form Content Formatting**
   - Standardize heading hierarchy
   - Balance paragraph lengths
   - Add section dividers
   - Optimize line breaks

5. **Basic Formatting**
   - Standardize markdown elements
   - Remove extra whitespace
   - Ensure consistent line endings

6. **Verification and Correction Pass**
   - Re-read the edited file
   - Validate formatting requirements:
     - All meaningful content is preserved (no deletions or modifications of substantive content other than formatting changes)
     - TOC exists (or is intentionally omitted for short files) and matches current headings
     - Math delimiters are consistent ($...$ inline, $$...$$ display), no mixed TeX markers
     - Heading hierarchy is normalized (no jumps like H2 -> H4)
     - Lists, code fences, and blockquotes render correctly
     - Line endings and blank-line spacing are consistent
   - If issues found, apply minimal, targeted fixes and re-verify once (max 2 passes total).
   - If issues persist after the second pass, include a brief summary of unresolved items at the top as an HTML comment.

   ```pseudo
   run initial_format(file)
   for pass in [1..2]:
     content = read(file)
     issues = detect_issues(content)
     if issues.empty(): break
     content = fix_issues(content, issues)
     write(file, content)
   if not issues.empty():
     prepend(file, "<!-- format-as-md: unresolved issues: ... -->")
   ```