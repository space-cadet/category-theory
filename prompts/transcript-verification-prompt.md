# Transcript Verification Prompt

## Task: Professional Transcription Verification
Systematically verify a professional transcription against a raw transcript by comparing them paragraph by paragraph to identify missing content.

## Input Files Required
1. **Professional transcription**: Clean, formatted with timestamps and LaTeX
2. **Raw transcript**: Original auto-generated with [MM:SS] timestamps

## Verification Process

### 1. Compare PARAGRAPH BY PARAGRAPH:
- Quote professional transcription paragraph
- Quote corresponding raw transcript section
- List missing content from professional version
- Use format:
```
**PARAGRAPH [N] COMPARISON:**
**MISSING from professional transcription:**
- [specific missing content with timestamps]
- OR "None - content matches exactly"
```

### 2. Critical Rules

**VERIFY:**
- Mathematical sequences and numerical expressions (e.g., "one one one two" vs "1112")
- Timestamp accuracy at topic transitions
- Context-dependent phrases that might seem redundant
- Directional references ("this way", "that way")
- Content that provides mathematical context

**IGNORE:**
- Formatting differences
- Mathematical notation improvements
- Grammar fixes
- Filler word removal

### 3. Examples of Substantive Content in Mathematical Lectures
- Verbal descriptions of diagram elements
- Alternative phrasings of mathematical concepts
- Informal explanations
- References to visual elements
- Step-by-step reasoning
- Connections between concepts

### 4. Professional Improvements (NOT Missing Content)
- Converting verbal math to LaTeX
- Fixing obvious speech errors
- Removing excessive fillers
- Adding proper formatting
- Standardizing notation

### 5. Process Control
- Compare systematically without skipping
- Focus only on missing content
- Do not make assumptions
- Continue until explicitly told to stop
- Report only actual content gaps

After each section, wait for instruction to continue.