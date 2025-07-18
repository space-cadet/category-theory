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
yt-dlp --write-auto-sub --sub-lang en --sub-format json3 --skip-download [URL]
cat [file].json3 | jq [format script] > final_transcript.txt
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
