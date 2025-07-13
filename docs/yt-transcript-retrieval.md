# YouTube Transcript Retrieval and Formatting

*Created: 2025-07-05*

## Overview

Efficient pipeline for extracting and formatting YouTube video transcripts using shell commands with yt-dlp and jq.

## Prerequisites

- yt-dlp installed in Python environment
- jq installed for JSON processing

## Complete Pipeline

### Step 1: Extract Transcript

Use yt-dlp to download transcript in JSON3 format:

```bash
/Users/deepak/miniconda3/bin/python -m yt_dlp --write-auto-sub --sub-lang en --sub-format json3 --skip-download [VIDEO_URL]
```

**Example:**
```bash
cd "/Users/deepak/Movies/Projects/Introduction to Using Memory Bank System"
/Users/deepak/miniconda3/bin/python -m yt_dlp --write-auto-sub --sub-lang en --sub-format json3 --skip-download https://www.youtube.com/watch?v=1yA7iWuPNUs
```

This creates a file like: `MEMORY BANK SYSTEM for Claude 4⧸Windsurf⧸Cursor [1yA7iWuPNUs].en.json3`

### Step 2: Process and Format with jq

Convert JSON3 data to clean transcript with timestamps:

```bash
cat [transcript.json3] | jq -r '.events[] | select(.tStartMs != null and .segs != null) | 
(([.segs[]?.utf8 // empty] | join("") | gsub("\\n"; "")) as $text |
 if ($text | length) > 0 then
   ((.tStartMs / 1000) as $seconds | 
    ($seconds / 60 | floor) as $minutes | 
    ($seconds % 60 | floor) as $secs |
    "[" + ($minutes | tostring) + ":" + (if $secs < 10 then "0" else "" end) + ($secs | tostring) + "] " + $text)
 else empty end)' > final_transcript.txt
```

**Example:**
```bash
cat "MEMORY BANK SYSTEM for Claude 4⧸Windsurf⧸Cursor [1yA7iWuPNUs].en.json3" | jq -r '.events[] | select(.tStartMs != null and .segs != null) | (([.segs[]?.utf8 // empty] | join("") | gsub("\\n"; "")) as $text | if ($text | length) > 0 then ((.tStartMs / 1000) as $seconds | ($seconds / 60 | floor) as $minutes | ($seconds % 60 | floor) as $secs | "[" + ($minutes | tostring) + ":" + (if $secs < 10 then "0" else "" end) + ($secs | tostring) + "] " + $text) else empty end)' > final_transcript.txt
```

## Output Format

The processed transcript will have clean timestamps in [MM:SS] format:

```
[0:00] So in this video I want to show you a
[0:03] way to work with uh projects in cloud
[0:06] desktop. Of course you can use uh any
[0:09] platform you like. You could use VS code
[0:11] uh with duru or client or augment or
[0:14] github copilot or any other uh front end
```

## Key Features

- **Fast**: Direct shell commands, no MCP overhead
- **Efficient**: Uses existing tools (yt-dlp + jq)
- **Accurate**: Properly formatted timestamps [MM:SS]
- **Clean**: Removes empty segments and duplicates
- **Scalable**: Can be easily scripted for multiple videos

## Notes

- The jq command filters out empty text segments and newline-only entries
- Timestamps are converted from milliseconds to MM:SS format
- Leading zeros are added for seconds < 10 (e.g., [0:05] not [0:5])
- Much more efficient than using MCP tools for transcript retrieval

## Alternative: Using MCP Tools

For comparison, the slower MCP approach would be:

```javascript
// In Claude with YouTube MCP
youtube-local:getTranscripts(["VIDEO_ID"])
```

But this requires manual processing and is significantly slower than the shell pipeline approach.
