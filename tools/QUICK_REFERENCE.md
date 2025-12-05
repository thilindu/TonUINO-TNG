# TonUINO Audio Content Manager - Quick Reference

## Launch GUI

```bash
cd tools
./launch_gui.sh
```

Or:
```bash
python3 tools/audio_content_gui.py
```

## Quick Start (3 Steps)

1. **Select Content** → Click "Browse File" or "Browse Folder"
2. **Enter Name** → Type a descriptive name
3. **Add** → Click "Add Content" button

Done! ✅

## Interface Overview

```
┌──────────────────────────────────────────┐
│  File/Folder: [path]  [Browse File    ] │
│                       [Browse Folder  ] │
├──────────────────────────────────────────┤
│  Name: [Your Content Name]              │
│  Type: (•) Audiobook ( ) Album          │
│        ( ) Story ( ) Single             │
├──────────────────────────────────────────┤
│  [✓] Auto-detect folder                 │
│  Folder: [03] (1-99)                    │
│  SD Dir: [sd-card-englisch/]  [Browse] │
├──────────────────────────────────────────┤
│  [Add Content] [Clear] [Exit]           │
├──────────────────────────────────────────┤
│  Log:                                    │
│  ✅ Content added successfully!          │
└──────────────────────────────────────────┘
```

## Content Types

| Type | Use For | Example |
|------|---------|---------|
| **Audiobook** | Multi-chapter books | Harry Potter |
| **Album** | Music collections | Beatles Album |
| **Story** | Single episodes | Bedtime Story |
| **Single** | Individual tracks | One Song |

## Common Tasks

### Add Audiobook
1. Browse Folder → Select audiobook folder
2. Name → "Harry Potter Book 1"
3. Type → Audiobook
4. Add Content

### Add Single Song
1. Browse File → Select MP3 file
2. Name → "Song Title"
3. Type → Single
4. Add Content

### Use Specific Folder
1. Uncheck "Auto-detect"
2. Enter folder number (1-99)
3. Add Content

## File Naming

Input (any name):
```
chapter1.mp3
part_two.mp3
final.mp3
```

Output (auto-formatted):
```
0001.mp3
0002.mp3
0003.mp3
```

## Tips

✅ **DO:**
- Use descriptive names
- Let it auto-detect folder
- Organize files before adding
- Keep original files safe

❌ **DON'T:**
- Use generic names like "book1"
- Manually change folder numbers unnecessarily
- Delete original files before testing
- Mix different content in one folder

## Troubleshooting

| Problem | Solution |
|---------|----------|
| GUI won't start | Install: `sudo apt install python3-tk` |
| Permission denied | Run: `chmod +x launch_gui.sh` |
| No MP3 files found | Check file extensions (.mp3) |
| Folder exists | Choose Yes to overwrite or select different folder |

## Keyboard Navigation

- **Tab** - Move between fields
- **Enter** - Click focused button
- **Space** - Toggle checkboxes/radio buttons
- **Escape** - Close dialogs

## After Adding Content

1. Copy `sd-card-englisch/` to SD card
2. Insert SD card in TonUINO
3. Enter Admin Menu (hold 3 buttons)
4. Configure new RFID card
5. Select folder number from GUI
6. Test with RFID card

## CLI Alternative

Prefer command line?

```bash
./add_audio_content.sh \
  --type audiobook \
  --content "/path/to/folder" \
  --name "Content Name"
```

## Support

- **Forum**: discourse.voss.earth
- **Wiki**: www.tonuino.de/TNG
- **Issues**: github.com/tonuino/TonUINO-TNG/issues

---

**Happy TonUINO-ing! 🎵**
