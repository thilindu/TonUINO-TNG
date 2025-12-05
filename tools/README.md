# TonUINO Tools

Tools for managing and maintaining your TonUINO audio content.

---

## 🎉 New Features

### Enhanced GUI Experience
Our graphical interface now includes powerful features to make content management effortless:

- **🎨 Modern Interface** - Clean, intuitive design with real-time feedback
- **🔄 Auto-Detection** - Automatically finds the next available folder number
- **📝 Smart Naming** - Auto-fills content names from folder/file names
- **📊 Live Logging** - Color-coded progress messages with emojis for easy tracking
  - ✅ Success messages in green
  - ❌ Errors in red
  - ⚠️ Warnings in orange
  - ℹ️ Info messages in black
- **🎯 Validation** - Real-time input validation prevents common mistakes
- **💾 CSV Auto-Update** - Automatically maintains media-list.csv
- **🔀 Flexible Paths** - Choose custom SD card locations on-the-fly
- **🎵 Multi-Type Support** - Handles audiobooks, albums, stories, and singles

### CLI Enhancements
The command-line tool now supports:

- **🚀 Batch Processing** - Process multiple files/folders in sequence
- **🎨 Color Output** - Better visual feedback with color-coded messages
- **🔧 Custom Configuration** - Override default paths and settings
- **📋 Detailed Logging** - Verbose output for troubleshooting

### TTS Improvements
Text-to-speech tools have been enhanced with:

- **🌍 Multi-Language Support** - German, English, and French
- **🎤 Quality Options** - Choose voice quality and speech rate
- **📦 Batch Generation** - Generate all messages at once

---

## Available Tools

### 1. 🎨 Audio Content Manager - GUI (Recommended)

**Graphical interface for easy content management**

```bash
./launch_gui.sh
```

**Features:**
- ✅ User-friendly graphical interface
- ✅ File/folder browser
- ✅ Auto-numbering and validation
- ✅ Real-time log viewer
- ✅ No external dependencies

📖 **Documentation:** [README_gui.md](README_gui.md)  
⚡ **Quick Start:** [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

---

### 2. 📟 Audio Content Manager - CLI

**Command-line script for automation and scripting**

```bash
./add_audio_content.sh --type audiobook --content "/path/to/folder" --name "Content Name"
```

**Features:**
- ✅ Full automation support
- ✅ Batch processing friendly
- ✅ Color-coded output
- ✅ Shell scripting integration

📖 **Documentation:** [README_add_audio_content.md](README_add_audio_content.md)

---

### 3. 🎤 Text-to-Speech Tools

**Generate custom voice prompts for TonUINO**

#### create_audio_messages.py
Generate audio files from text files in multiple languages.

```bash
python3 create_audio_messages.py
```

Supports:
- German (audio_messages_de.txt)
- English (audio_messages_en.txt)
- French (audio_messages_fr.txt)

#### text_to_speech.py
Core text-to-speech functionality used by other scripts.

#### add_lead_in_messages.py
Add lead-in messages to audio files.

---

## Quick Start Guide

### For Beginners: Use the GUI

```bash
cd tools
./launch_gui.sh
```

1. Click "Browse Folder" to select your content
2. Enter a name
3. Select content type (audiobook/album/story/single)
4. Click "Add Content"

### For Power Users: Use the CLI

```bash
./add_audio_content.sh \
  --type audiobook \
  --content "/path/to/audiobook" \
  --name "Harry Potter Book 1"
```

### For Automation: Script It

```bash
#!/bin/bash
for dir in /audiobooks/*; do
  ./add_audio_content.sh \
    --type audiobook \
    --content "$dir" \
    --name "$(basename "$dir")"
done
```

---

## Tool Comparison

| Feature | GUI | CLI | TTS Tools |
|---------|-----|-----|-----------|
| **Ease of Use** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Automation** | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Visual Feedback** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Scripting Support** | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Batch Processing** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Learning Curve** | Low | Medium | High |

**Recommendation:**
- **First-time users**: Use GUI
- **Regular management**: Use GUI or CLI
- **Bulk imports**: Use CLI
- **Custom voices**: Use TTS tools

---

## Common Workflows

### Workflow 1: Add New Audiobook (GUI)

1. Launch GUI: `./launch_gui.sh`
2. Browse to audiobook folder
3. Enter name: "Harry Potter and the Philosopher's Stone"
4. Type: Audiobook
5. Click "Add Content"
6. Copy to SD card
7. Create RFID card on TonUINO

### Workflow 2: Batch Import Albums (CLI)

```bash
#!/bin/bash
for album in /music/albums/*; do
  ./add_audio_content.sh \
    --type album \
    --content "$album" \
    --name "$(basename "$album")"
  sleep 1
done
```

### Workflow 3: Create Custom Language Pack (TTS)

1. Create/edit `audio_messages_xx.txt`
2. Run `python3 create_audio_messages.py`
3. Select language
4. Generated files go to `sd-card-xx/`

---

## Prerequisites

### For Content Managers (GUI/CLI)

**Required:**
- Bash shell (Linux/macOS/WSL)
- Basic file system access

**For GUI only:**
- Python 3.6+ with tkinter
  ```bash
  sudo apt install python3 python3-tk  # Ubuntu/Debian
  brew install python-tk               # macOS
  ```

### For TTS Tools

**Required:**
- Python 3.6+
- Additional Python packages (varies by tool)

Check individual tool documentation for specific requirements.

---

## Installation

No installation needed! Just clone the repository:

```bash
git clone https://github.com/tonuino/TonUINO-TNG.git
cd TonUINO-TNG/tools
```

Make scripts executable:

```bash
chmod +x *.sh *.py
```

---

## File Structure

```
tools/
├── README.md                          # This file
├── QUICK_REFERENCE.md                 # Quick reference card
│
├── Audio Content Managers
├── launch_gui.sh                      # GUI launcher
├── audio_content_gui.py               # GUI application
├── README_gui.md                      # GUI documentation
├── add_audio_content.sh               # CLI script
├── README_add_audio_content.md        # CLI documentation
│
└── Text-to-Speech Tools
    ├── create_audio_messages.py       # Generate audio from text
    ├── text_to_speech.py              # TTS core functionality
    └── add_lead_in_messages.py        # Add lead-in messages
```

---

## What These Tools Do

### Content Management Tools

**Problem:** Manually adding audio files is tedious
- Need to create folders (01, 02, 03...)
- Need to rename files (0001.mp3, 0002.mp3...)
- Need to update CSV file
- Easy to make mistakes

**Solution:** Automated tools
- Auto-detect next folder number
- Auto-rename files to proper format
- Auto-update media-list.csv
- Validation and error checking

### Text-to-Speech Tools

**Problem:** Need custom voice prompts in different languages

**Solution:** Generate MP3 files from text
- Support multiple languages
- Consistent voice across all prompts
- Easy to update and regenerate

---

## Troubleshooting

### GUI Won't Start

```bash
# Check Python and tkinter
python3 --version
python3 -c "import tkinter; print('OK')"

# Install if needed
sudo apt install python3-tk
```

### Permission Denied

```bash
# Make scripts executable
chmod +x launch_gui.sh
chmod +x add_audio_content.sh
```

### Command Not Found

```bash
# Run from tools directory
cd tools
./launch_gui.sh
```

### Files Not Copying

- Check source path exists
- Check you have write permission to sd-card directory
- Check file extensions are .mp3 (case-insensitive)

---

## Integration with TonUINO

After using these tools:

1. **Copy to SD Card**
   ```bash
   # Copy entire folder structure
   cp -r sd-card-englisch/* /path/to/sdcard/
   ```

2. **Create RFID Cards**
   - Insert SD card in TonUINO
   - Enter Admin Menu (hold all 3 buttons)
   - Configure new card
   - Select folder number from tool output

3. **Test**
   - Place RFID card on reader
   - Content should play!

---

## Tips & Best Practices

### 1. Organize Before Adding
Sort and name your files properly before using the tools:
```
01_chapter_one.mp3
02_chapter_two.mp3
03_chapter_three.mp3
```

### 2. Use Descriptive Names
- ✅ Good: "Harry Potter and the Philosopher's Stone"
- ❌ Bad: "book1", "audiobook", "files"

### 3. Keep Backups
- Tools can overwrite folders
- Keep original files safe elsewhere

### 4. Test First
- Add a test file/folder first
- Verify it works before bulk import

### 5. Use Auto-Detection
- Let tools find next folder automatically
- Prevents conflicts and duplicates

---

## Advanced Usage

### Custom SD Card Location

**GUI:** Click "Browse" next to SD Card Dir

**CLI:**
```bash
./add_audio_content.sh \
  --type audiobook \
  --content "/path/to/content" \
  --sd-dir "/custom/path/to/sdcard"
```

### Specific Folder Number

**GUI:** Uncheck "Auto-detect" and enter number

**CLI:**
```bash
./add_audio_content.sh \
  --type album \
  --content "/path/to/music" \
  --folder 42
```

### Batch Processing

```bash
# Import all audiobooks
for dir in /audiobooks/*; do
  ./add_audio_content.sh \
    --type audiobook \
    --content "$dir" \
    --name "$(basename "$dir")"
done

# Import with custom naming
find /music -type d -name "Album*" | while read album; do
  artist=$(basename "$(dirname "$album")")
  name=$(basename "$album")
  ./add_audio_content.sh \
    --type album \
    --content "$album" \
    --name "$artist - $name"
done
```

---

## Contributing

Contributions welcome!

**Ideas for new tools:**
- Audio format converter (FLAC/WAV → MP3)
- Metadata editor
- Bulk RFID card writer
- SD card backup/restore
- Audio quality checker
- Duplicate detector

**How to contribute:**
1. Fork the repository
2. Create your feature branch
3. Test thoroughly
4. Submit pull request

---

## Support

- **Forum**: [discourse.voss.earth](https://discourse.voss.earth)
- **Wiki**: [www.tonuino.de/TNG](https://www.tonuino.de/TNG)
- **Issues**: [GitHub Issues](https://github.com/tonuino/TonUINO-TNG/issues)

---

## License

Same as TonUINO-TNG project - see main LICENSE file.

---

**Made with ❤️ for the TonUINO Community**

🎵 Happy audio content managing! 🎵
