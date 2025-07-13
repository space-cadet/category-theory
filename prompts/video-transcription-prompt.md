# Video Transcription Prompt

```
Transcribe the lecture from [START_TIME] to [END_TIME] into human readable form using the final_transcript.txt file. Follow these requirements exactly:

1. FIDELITY: Include every word, phrase, and idea from the transcript within the specified time range. Do not omit any content, no matter how small or seemingly redundant. Remove filler utterances such as "uh," "um," "ah," etc.

2. MATHEMATICAL NOTATION: Convert mathematical references to proper LaTeX:
   - Functions: f: A → B becomes $f: A \to B$
   - Sets: R^n becomes $\mathbb{R}^n$
   - Categories: C becomes $\mathcal{C}$
   - Composition: g after f becomes $g \circ f$
   - Use display equations ($$...$$) for important mathematical expressions
   - Use LaTeX commutative diagrams with \begin{CD}...\end{CD} format
   - Insert tables, diagrams, and other formatting elements as needed to represent the content clearly

3. STRUCTURE: Organize with clear section headers based on topic changes and break text into paragraphs for readability. Do not impose artificial organization that wasn't present in the lecture.

4. ANNOTATIONS: Include speaker actions in italics when mentioned: [writing on board] becomes *[writing on board]*

5. TIMESTAMPS: Add timestamp labels **[MM:SS]** at every section and subsection heading to mark progression through the lecture. Verify timestamps against the actual source transcript to ensure accuracy.

6. NO EDITORIAL CHANGES: Do not:
   - Paraphrase or summarize
   - "Clean up" the language beyond removing filler utterances
   - Add explanations not present in the original
   - Skip repetitive or unclear sections
   - Impose formal academic structure where it doesn't exist

Use block edits to add the transcribed content to the file named as [VIDEO TITLE].md in videos/[VIDEO TITLE]/

Important: When transcribing in segments, break into multiple block edits rather than one large edit for better version control and error handling.
```
