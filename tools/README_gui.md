# TonUINO Audio Content Manager - GUI

A powerful graphical user interface for managing audio content on TonUINO SD cards with database tracking and file integrity verification.

![TonUINO GUI](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-green.svg)

## Features

### Core Features
- 🎨 **User-Friendly Interface** - Easy-to-use graphical interface
- 📁 **File Browser** - Select MP3 or AAX files/folders with built-in browser
- 🔢 **Auto-Numbering** - Automatically detects next available folder
- ✏️ **Content Types** - Support for audiobooks, albums, stories, and singles
- 📚 **AAX Support** - Convert Audible audiobooks to MP3 automatically
- 📊 **Real-Time Log** - See progress and status messages
- ✅ **Validation** - Built-in validation for all inputs
- 🎯 **Minimal Dependencies** - Uses built-in Python tkinter

### New Database Features
- 📚 **Content Browser** - View all existing audio content at a glance
- 🔍 **Status Monitoring** - Real-time sync status for each folder
  - ✅ **Synced**: Files match database and hash records
  - ⚠️ **Modified**: Files changed since last sync
  - ⚠️ **Mismatch**: Track count doesn't match database
  - ❌ **Not in DB**: Folder exists but not tracked in database
- 🔐 **Hash Tracking** - MD5 hash verification for file integrity
- 🗑️ **Delete Content** - Remove content from both filesystem and database
- 🔄 **Verify Sync** - Check synchronization between files and database
- 💾 **Persistent Tracking** - Maintains `.tonuino_hash.json` for integrity checks

### AAX Audiobook Features
- 🎧 **Direct AAX Import** - Load Audible audiobooks directly
- 🔄 **Automatic Conversion** - Converts AAX to MP3 during import
- 🔓 **DRM Removal** - Uses activation bytes for DRM removal
- 📦 **Batch Processing** - Handle multiple AAX files at once

For detailed AAX setup and usage, see [AAX Audiobook Support Guide](README_AAX_SUPPORT.md)

### Database Files
- **.tonuino_hash.json**: Primary database with all content metadata and integrity hashes

## Screenshots

```
┌─────────────────────────────────────────────────────┐
│      TonUINO Audio Content Manager                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Content Selection                                  │
│  File/Folder: [________________] [Browse File   ]  │
│                                  [Browse Folder ]  │
│                                                     │
│  Content Information                                │
│  Name: [____________________]                       │
│  Type: ( ) Audiobook ( ) Album ( ) Story ( ) Single│
│                                                     │
│  Folder Configuration                               │
│  [✓] Auto-detect next available folder              │
│  Folder Number: [03] (1-99)                         │
│  SD Card Dir: [________________] [Browse]          │
│                                                     │
│  [Add Content] [Clear Form] [Exit]                 │
│                                                     │
│  Log                                                │
│  ┌───────────────────────────────────────────────┐ │
│  │ ✅ Content added successfully!                │ │
│  │ ℹ️  Folder: 03                                │ │
│  │ ℹ️  Tracks: 12                                │ │
│  └───────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

## Prerequisites

- **Python 3.6+** (comes pre-installed on most Linux/macOS systems)
- **tkinter** (usually included with Python)

### Optional: For AAX Audiobook Support
- **AAXtoMP3** or **FFmpeg** - Required for converting Audible AAX files
- **Activation Bytes** - Your Audible account's activation bytes

See [AAX Audiobook Support Guide](README_AAX_SUPPORT.md) for installation instructions.

### Check Prerequisites

```bash
# Check Python version
python3 --version

# Check if tkinter is available
python3 -c "import tkinter; print('tkinter is available')"

# Check if AAX converter is available (optional)
AAXtoMP3 -version
# or
ffmpeg -version
```

### Install Python (if needed)

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-tk
```

**macOS:**
```bash
brew install python-tk
```

**Windows:**
Download from [python.org](https://www.python.org/downloads/) - tkinter is included by default.

## Installation

No installation required! Just clone the repository:

```bash
git clone https://github.com/tonuino/TonUINO-TNG.git
cd TonUINO-TNG/tools
```

## Usage

### Method 1: Using the Launcher Script (Recommended)

```bash
./launch_gui.sh
```

### Method 2: Direct Python Execution

```bash
python3 audio_content_gui.py
```

### Method 3: Double-Click (on some systems)

Make the file executable and double-click `audio_content_gui.py`

## How to Use

### Step-by-Step Guide

#### Viewing Existing Content

1. **Launch the Application**
   ```bash
   ./launch_gui.sh
   ```

2. **Browse Existing Content**
   - The top section displays all existing audio content
   - See folder number, type, track count, and sync status
   - Color-coded status indicators:
     - **✅ Synced** (Green): Everything matches
     - **⚠️ Modified** (Orange): Files changed after adding
     - **⚠️ Mismatch** (Orange): Track count mismatch
     - **❌ Not in DB** (Red): Folder not tracked

3. **Manage Existing Content**
   - **Refresh**: Update the content list
   - **Delete Selected**: Remove content (files + database entries)
   - **Verify Sync**: Check file integrity across all folders

#### Adding New Content

1. **Select Your Content**
   - Click "Browse File" to select a single MP3 file
   - OR click "Browse Folder" to select a folder containing multiple MP3s

2. **Enter Content Information**
   - **Name**: Enter a descriptive name (e.g., "Harry Potter Book 1")
   - **Type**: Select content type:
     - **Audiobook** - Multi-chapter books with progress saving
     - **Album** - Music collections
     - **Story** - Individual stories
     - **Single** - Single tracks

3. **Configure Folder**
   - Leave "Auto-detect next available folder" checked (recommended)
   - OR uncheck and manually enter a folder number (1-99)
   - Verify the SD card directory path is correct

4. **Add Content**
   - Click "Add Content" button
   - Watch the log for progress
   - If folder exists, you'll be asked to confirm overwrite

5. **Success!**
   - The log will show success message
   - Files are copied and renamed automatically
   - media-list.csv is updated
   - Hash is calculated and saved
   - Content list is refreshed
   - Ready for next content!

## Interface Elements

### Existing Content Browser
- **Tree View** - Displays all folders with content information
- **Name Column** - Content name from database
- **Folder Column** - Folder number (01-99)
- **Type Column** - Content type (audiobook/album/story/single)
- **Tracks Column** - Number of MP3 files
- **Status Column** - Sync status with color indicators
- **Refresh Button** - Reload content list
- **Delete Selected** - Remove selected content
- **Verify Sync** - Check integrity of all content

### Content Selection
- **Browse File** - Select a single MP3 file
- **Browse Folder** - Select a folder with multiple MP3 files
- Auto-fills the name field from file/folder name

### Content Information
- **Name** - Display name for the content (used in CSV)
- **Type** - Playback mode type (audiobook/album/story/single)

### Folder Configuration
- **Auto-detect** - Automatically finds next available folder number
- **Manual** - Specify exact folder number (1-99)
- **SD Card Dir** - Path to sd-card-englisch folder

### Action Buttons
- **Add Content** - Process and add the content
- **Clear Form** - Reset all fields
- **Exit** - Close the application

### Log Window
Real-time status messages with color coding:
- ✅ **Green** - Success messages
- ℹ️  **Blue** - Information messages
- ⚠️  **Orange** - Warning messages
- ❌ **Red** - Error messages

## Features in Detail

### Database & Hash Tracking

#### JSON Database (.tonuino_hash.json)
Unified database tracking all content with integrity verification:
```json
{
  "01": {
    "name": "the gruffalo",
    "type": "single",
    "track_count": 1,
    "hash": "ff4666baf74e9505e9010a7bd85f3a31",
    "tracks": [
      {
        "index": "0001",
        "name": "the gruffalo"
      }
    ]
  },
  "03": {
    "name": "Harry Potter Book 1",
    "type": "audiobook",
    "track_count": 12,
    "hash": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
    "tracks": [
      {
        "index": "0001",
        "name": "Harry Potter Book 1 - Chapter 1"
      },
      {
        "index": "0002",
        "name": "Harry Potter Book 1 - Chapter 2"
      }
    ]
  }
}
```

**Fields:**
- **name**: Content display name
- **type**: Content type (audiobook/album/story/single)
- **track_count**: Number of MP3 files
- **hash**: MD5 hash of all files for integrity checking
- **tracks**: Array of track information with index and name

#### Sync Status Detection
The app automatically detects:
- **✅ Synced**: Hash matches, files unchanged
- **⚠️ Modified**: Hash mismatch, files were modified
- **⚠️ Mismatch**: Track count different from database
- **❌ Not in DB**: Folder exists but not tracked

#### Content Deletion
Safe deletion process:
1. Confirms with user before deletion
2. Removes folder and all MP3 files
3. Updates .tonuino_hash.json (removes entry)
4. Refreshes display

### Auto-Naming
When you select a file or folder, the name field is automatically filled:
- File: `audiobook_chapter1.mp3` → Name: `audiobook_chapter1`
- Folder: `Harry Potter Book 1` → Name: `Harry Potter Book 1`

### Auto-Folder Detection
The app scans your SD card directory and finds the next available folder:
- Existing: 01, 02, 04, 05
- Next: 06 (skips 03 if missing)

### File Renaming
Input files (any name):
```
chapter_one.mp3
part2.mp3
final_chapter.mp3
```

Output (standardized):
```
0001.mp3
0002.mp3
0003.mp3
```

### Overwrite Protection
If a folder already exists:
- Shows confirmation dialog
- Allows you to cancel or proceed
- Safely removes old content before adding new
- Updates hash after successful addition
```

## Examples

### Example 1: Add an Audiobook

1. Click "Browse Folder"
2. Select: `/home/user/audiobooks/harry_potter_book1/`
3. Name auto-fills: `harry_potter_book1`
4. Edit to: `Harry Potter and the Philosopher's Stone`
5. Type: Select "Audiobook"
6. Folder: Auto-detected as "03"
7. Click "Add Content"

Result: 12 chapters copied to folder 03/

### Example 2: Add a Single Story

1. Click "Browse File"
2. Select: `/home/user/stories/three_little_pigs.mp3`
3. Name auto-fills: `three_little_pigs`
4. Edit to: `The Three Little Pigs`
5. Type: Select "Story"
6. Folder: Auto-detected as "04"
7. Click "Add Content"

Result: 1 file copied to folder 04/

### Example 3: Add Music Album

1. Click "Browse Folder"
2. Select: `/home/user/music/beatles_abbey_road/`
3. Name: `The Beatles - Abbey Road`
4. Type: Select "Album"
5. Folder: Auto-detected as "05"
6. Click "Add Content"

Result: All tracks copied to folder 05/

### Example 4: Specific Folder Number

1. Select your content
2. Uncheck "Auto-detect next available folder"
3. Enter folder number: `15`
4. Fill in other fields
5. Click "Add Content"

Result: Content added to folder 15/ specifically

## Validation

The app validates all inputs before processing:

✅ **Valid Inputs:**
- MP3 file or folder with MP3 files
- Non-empty content name
- Folder number between 1-99
- Existing SD card directory

❌ **Invalid Inputs:**
- Non-MP3 files
- Empty content name
- Folder number outside 1-99 range
- Non-existent paths

## Troubleshooting

### GUI Won't Start

**Error: "tkinter not found"**
```bash
# Install tkinter
sudo apt install python3-tk
```

**Error: "Python3 not found"**
```bash
# Install Python3
sudo apt install python3
```

### Permission Denied

```bash
# Make scripts executable
chmod +x launch_gui.sh
chmod +x audio_content_gui.py
```

### SD Card Directory Not Found

1. Click "Browse" next to "SD Card Dir"
2. Navigate to your `sd-card-englisch` folder
3. Select and confirm

### Files Not Copying

- Check that source contains MP3 files (case-insensitive)
- Verify you have write permissions to SD card directory
- Check available disk space

### Folder Already Exists

- The app will ask for confirmation
- Choose "Yes" to overwrite
- Choose "No" to cancel and select different folder

## Command Line Alternative

If you prefer command line, use the bash script:

```bash
./add_audio_content.sh --type audiobook --content "/path/to/folder" --name "My Content"
```

See `README_add_audio_content.md` for details.

## Technical Details

### File Structure

```
tools/
├── audio_content_gui.py        # Main GUI application
├── launch_gui.sh               # Launcher script
├── add_audio_content.sh        # CLI version
└── README_gui.md               # This file
```

### Dependencies

- **Python 3.6+** - Core language
- **tkinter** - GUI framework (built-in)
- **pathlib** - Path handling (built-in)
- **shutil** - File operations (built-in)
- **csv** - CSV handling (built-in)

No external dependencies required!

### Platform Support

- ✅ **Linux** - Tested on Ubuntu, Debian
- ✅ **macOS** - Works with system Python
- ✅ **Windows** - Works with Python from python.org
- ✅ **WSL** - Works with X server

## Integration with TonUINO

After adding content:

1. **Copy to SD Card**
   - Copy entire `sd-card-englisch` folder to SD card
   - Preserve folder structure

2. **Create RFID Card**
   - Insert SD card in TonUINO
   - Enter Admin Menu (hold all 3 buttons)
   - Select "Configure New Card"
   - Choose playback mode matching your type
   - Select the folder number from the app
   - Place blank RFID card on reader

3. **Test**
   - Remove admin card
   - Place your new card on reader
   - Content should play!

## Keyboard Shortcuts

- **Tab** - Navigate between fields
- **Enter** - Activate focused button
- **Escape** - Close dialogs
- **Ctrl+Q** - Quit application (on some systems)

## Tips & Best practices

1. **Organize Your Files First**
   - Name files in order: `01_chapter1.mp3`, `02_chapter2.mp3`
   - The app will sort them alphabetically

2. **Use Descriptive Names**
   - Good: `Harry Potter and the Philosopher's Stone`
   - Avoid: `book1`, `audiobook`, `files`

3. **Keep Backups**
   - The app overwrites folders on confirmation
   - Keep original files safe elsewhere

4. **Test First**
   - Add a test file first to verify everything works
   - Then add your full content

5. **Use Auto-Folder**
   - Let the app detect next folder automatically
   - Less chance of conflicts

## Future Enhancements

Planned features:
- Drag & drop file support
- Batch import multiple folders
- Preview MP3 metadata (title, artist, duration)
- Audio format conversion (WAV, FLAC → MP3)
- Direct SD card detection
- RFID card writing integration
- Progress bar for large operations
- Undo functionality

## Contributing

Found a bug or have a feature request?
- Open an issue on [GitHub](https://github.com/tonuino/TonUINO-TNG/issues)
- Submit a pull request

## License

Same as TonUINO-TNG project - see LICENSE file.

## Support

- **Forum**: [discourse.voss.earth](https://discourse.voss.earth)
- **Wiki**: [www.tonuino.de/TNG](https://www.tonuino.de/TNG)
- **Issues**: [GitHub Issues](https://github.com/tonuino/TonUINO-TNG/issues)

---

**Made with ❤️ for the TonUINO Community**
