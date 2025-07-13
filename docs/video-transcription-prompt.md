# Video Transcription Prompt

```
Transcribe the lecture from [START_TIME] to [END_TIME] into human readable form using the final_transcript.txt file. Follow these requirements exactly:

1. FIDELITY: Include every word, phrase, and idea from the transcript within the specified time range. Do not omit any content, no matter how small or seemingly redundant.

2. MATHEMATICAL NOTATION: Convert mathematical references to proper LaTeX:
   - Functions: f: A → B becomes $f: A \to B$
   - Sets: R^n becomes $\mathbb{R}^n$
   - Categories: C becomes $\mathcal{C}$
   - Composition: g after f becomes $g \circ f$

3. STRUCTURE: Organize with clear section headers based on topic changes, but do not impose artificial organization that wasn't present in the lecture.

4. ANNOTATIONS: Include speaker actions in italics when mentioned: [writing on board] becomes *[writing on board]*

5. NO EDITORIAL CHANGES: Do not:
   - Paraphrase or summarize
   - "Clean up" the language
   - Add explanations not present in the original
   - Skip repetitive or unclear sections
   - Impose formal academic structure where it doesn't exist

Use block edits to add the transcribed content to the existing file at the appropriate location.
```
