# Essential Video Workflow

## Project Structure:
```
Projects/[Video Title]/
├── final_transcript.txt
├── video_details.md
├── description.md
└── [video files]
```

## Required Files to Create:
1. `final_transcript.txt` - Clean transcript with timestamps
2. `video_details.md` - Complete video metadata  
3. `description.md` - YouTube description
4. `V[X].md` - Task file in memory-bank/tasks/

## Essential Steps:

**1. Setup Project Folder**
```bash
mkdir "Projects/[Video Title]"
cd "Projects/[Video Title]"
```

**2. Extract Content**
```bash
# Use full Python path for yt-dlp
/Users/deepak/miniconda3/bin/python -m yt_dlp --write-auto-sub --sub-lang en --sub-format json3 --skip-download "[URL]"

# Process transcript to clean format:
# - One line per timestamp
# - No empty lines
# - Words properly joined
# - Preserves all original content for later transcription
cat "[file].json3" | jq -r '.events[] | select(.tStartMs != null and .segs != null and ([.segs[].utf8] | join("") | test("\\S"))) | "[" + (.tStartMs/1000|floor|tostring) + "s] " + ([.segs[].utf8] | join("") | gsub("\\s+"; " "))' > "final_transcript.txt"

# Note: This produces a raw transcript that will later be processed according to:
# /prompts/video-transcription-prompt.md
# including LaTeX formatting, structure, and annotations
```

**3. Get Video Data**
- YouTube MCP: `getVideoDetails` → save to `video_details.md` via shell

**4. Create Description**  
- Analyze transcript for chapters
- Write `description.md` with: problem → solution → chapters → links

**5. Create Task**
- `V[X].md` in memory-bank/tasks/ with progress tracking

**Tools:** yt-dlp + jq (transcripts), YouTube MCP (metadata), shell commands (file ops)

Five files, five steps.
