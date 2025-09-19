# Video Transcription Prompt

```
Transcribe the lecture from [START_TIME] to [END_TIME] into human readable form using the final_transcript.txt file. Follow these requirements exactly:

1. FIDELITY: Include every word, phrase, and idea from the transcript within the specified time range.
   - Remove only filler utterances ("uh," "um," "ah")
   - Preserve directional references ("this way", "that way") as they often relate to diagrams
   - Maintain verbal forms of sequences (e.g., "one one one two") while adding mathematical notation where appropriate
   - Keep repetitions and unclear sections - they may be intentional teaching devices

2. MATHEMATICAL NOTATION: Convert mathematical references to proper LaTeX:
   - Functions: f: A → B becomes $f: A \to B$
   - Sets: R^n becomes $\mathbb{R}^n$
   - Categories: C becomes $\mathcal{C}$
   - Composition: g after f becomes $g \circ f$
   - Use display equations ($$...$$) for important mathematical expressions
   - Use LaTeX commutative diagrams with \begin{CD}...\end{CD} format
   - Preserve the natural flow of mathematical discussion even when formatting in LaTeX

3. STRUCTURE: 
   - Add clear section headers at topic changes
   - Break text into paragraphs for readability
   - Do not impose structure not present in the lecture

4. TIMESTAMPS: Add **[MM:SS]** at:
   - Section and subsection headings
   - Major topic transitions
   - Key mathematical definitions or theorems
   Verify all timestamps against the source transcript.

5. NO EDITORIAL CHANGES: Do not:
   - Paraphrase or summarize
   - "Clean up" language beyond removing fillers
   - Add explanations
   - Skip content
   - Impose formal structure

Use block edits to add content to [VIDEO TITLE].md in videos/[VIDEO TITLE]/. Break into multiple block edits (<30 lines) for better version control.
```