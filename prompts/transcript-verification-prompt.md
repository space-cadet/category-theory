# Transcript Verification Prompt

## Task: Professional Transcription Verification

You will systematically verify a professional transcription against a raw transcript by comparing them paragraph by paragraph to identify any missing content.

## Input Files Required
1. **Professional transcription file**: The cleaned, formatted transcription with timestamps and LaTeX notation
2. **Raw transcript file**: The original auto-generated transcript with precise timestamps in [MM:SS] format

## Instructions

### 1. Confirmation Phase
Before starting, confirm your understanding:
- State "YES, I UNDERSTAND" or "NO, I DO NOT UNDERSTAND"  
- If NO, ask for clarification
- If YES, proceed immediately to comparison

### 2. Comparison Method
Compare the files **PARAGRAPH BY PARAGRAPH** in exact sequence:

For each paragraph:
1. **Quote the professional transcription paragraph exactly**
2. **Quote the corresponding raw transcript section exactly**  
3. **Identify any missing content** from the professional transcription
4. **Report findings** using the format below

### 3. Reporting Format
```
**PARAGRAPH [N] COMPARISON:**

**MISSING from professional transcription:**
- [specific missing content with timestamps if applicable]
- OR "None - content matches exactly"
```

### 4. Critical Rules

**DO:**
- Compare every paragraph systematically without skipping
- Note any missing words, phrases, or filler content
- Continue until explicitly told to stop
- Focus only on what is missing, not on improvements

**DO NOT:**
- Skip paragraphs or sections
- Make assumptions about what should or shouldn't be included
- Extrapolate or guess content
- Consider professional improvements (grammar fixes, notation cleanup) as missing content
- Stop comparing unless explicitly instructed
- Quote entire paragraphs unless specifically needed for context

### 5. Professional Transcription Context
The professional transcription is expected to:
- Convert spoken notation into proper mathematical symbols (e.g., "C infinity" → "$C^∞$")
- Fix obvious speech errors (e.g., "homorphisms" → "homomorphisms")
- Remove excessive filler words appropriately
- Add proper formatting and structure

These improvements are NOT considered missing content.

### 6. Scope Control
- Only report actual missing substantive content
- Ignore formatting differences
- Ignore mathematical notation improvements
- Focus on content gaps, not quality improvements

## Example Output
```
**PARAGRAPH 1 COMPARISON:**

**MISSING from professional transcription:**
- "So let's begin." (timestamp [0:08])
```

## Continuation Protocol
After each set of paragraphs, wait for instruction to continue with the next section. Respond only with "Proceed to next section" or similar brief acknowledgment when ready to continue.
