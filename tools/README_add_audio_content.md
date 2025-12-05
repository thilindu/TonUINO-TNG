# TonUINO Audio Content Manager

A bash script to automate adding audio files to the TonUINO SD card structure.

## Features

- ✅ Automatically increments folder numbers
- ✅ Converts file names to proper 4-digit format (0001.mp3, 0002.mp3, etc.)
- ✅ Supports single files or entire folders
- ✅ Updates media-list.csv automatically
- ✅ Validates MP3 files
- ✅ Multiple content types (audiobook, album, story, single)
- ✅ Color-coded output for better readability
- ✅ Safety checks to prevent overwrites

## Prerequisites

- Bash shell (Linux/macOS/WSL)
- MP3 files to add

## Usage

### Basic Syntax

```bash
./add_audio_content.sh --type <TYPE> --content <PATH> [OPTIONS]
```

### Required Arguments

- `--type TYPE` - Content type: `audiobook`, `album`, `story`, or `single`
- `--content PATH` - Path to MP3 file or folder containing MP3 files

### Optional Arguments

- `--name NAME` - Name/description for the content (used in CSV)
- `--folder NUM` - Specific folder number (1-99). Auto-detects next available if not specified
- `--sd-dir PATH` - Custom SD card directory path
- `--help` - Show help message

## Examples

### 1. Add an Audiobook from a Folder

```bash
./add_audio_content.sh \
  --type audiobook \
  --content "/path/to/harry_potter_book1" \
  --name "Harry Potter and the Philosopher's Stone"
```

This will:
- Find the next available folder (e.g., `01/`)
- Copy all MP3 files from the folder
- Rename them as `0001.mp3`, `0002.mp3`, etc.
- Update `media-list.csv` with entries like "Harry Potter... - Chapter 1"

### 2. Add an Album

```bash
./add_audio_content.sh \
  --type album \
  --content "/path/to/beatles_abbey_road" \
  --name "The Beatles - Abbey Road"
```

### 3. Add a Single Story File

```bash
./add_audio_content.sh \
  --type story \
  --content "/path/to/bedtime_story.mp3" \
  --name "The Three Little Pigs"
```

### 4. Add to a Specific Folder Number

```bash
./add_audio_content.sh \
  --type album \
  --content "/path/to/music" \
  --folder 15 \
  --name "My Favorite Songs"
```

This will create/overwrite folder `15/` specifically.

### 5. Quick Add (Auto-generate Name)

```bash
./add_audio_content.sh \
  --type audiobook \
  --content "/path/to/peter_pan"
```

Name will be auto-generated from the folder/file name: "peter_pan"

## Content Types

| Type | Description | Use Case |
|------|-------------|----------|
| `audiobook` | Multi-chapter audiobook | Long-form content with progress saving |
| `album` | Music album or collection | Multiple songs to play in order |
| `story` | Single story or episode | Individual stories for children |
| `single` | Single track | One-off songs or sounds |

## How It Works

### Step-by-Step Process

1. **Validates inputs** - Checks if content exists and type is valid
2. **Determines folder number** - Auto-detects next available or uses specified number
3. **Creates destination folder** - Creates `XX/` folder in `sd-card-englisch/`
4. **Copies and renames files** - Copies MP3s and renames to 4-digit format
5. **Updates CSV** - Adds entries to `media-list.csv`
6. **Shows summary** - Displays what was done and next steps

### File Naming

Input files (any name):
```
chapter_01.mp3
part-two.mp3
03_final_chapter.mp3
```

Output (standardized):
```
0001.mp3
0002.mp3
0003.mp3
```

### Folder Numbering

The script automatically finds the next available folder:

```
sd-card-englisch/
├── 01/  (existing)
├── 02/  (existing)
└── 03/  (will be created automatically)
```

## Output Example

```
[INFO] =========================================
[INFO] TonUINO Audio Content Manager
[INFO] =========================================
[INFO] Type: audiobook
[INFO] Content: /home/user/audiobooks/harry_potter
[INFO] Name: Harry Potter Book 1
[INFO] Folder: 03
[INFO] Destination: /path/to/sd-card-englisch/03
[INFO] =========================================
[INFO] Copying MP3 files...
[INFO] Copied: chapter_01.mp3 -> 0001.mp3
[INFO] Copied: chapter_02.mp3 -> 0002.mp3
[INFO] Copied: chapter_03.mp3 -> 0003.mp3
[SUCCESS] Copied 3 track(s) to folder 03
[INFO] Updating media-list.csv...
[SUCCESS] Updated media-list.csv with 3 entries
[INFO] =========================================
[SUCCESS] Content added successfully!
[INFO] =========================================
[INFO] Folder: 03 (/path/to/sd-card-englisch/03)
[INFO] Tracks: 3
[INFO] Type: audiobook
[INFO] Name: Harry Potter Book 1
[INFO] 
[INFO] Next steps:
[INFO] 1. Copy the sd-card-englisch folder contents to your SD card
[INFO] 2. Use Admin Menu to create an RFID card for folder 03
[INFO] 3. Select playback mode 'audiobook' when configuring the card
[INFO] =========================================
```

## CSV Format

The script updates `media-list.csv` with the following format:

```csv
Folder,Index,Type,Track
01,0001,audiobook,"Harry Potter Book 1 - Chapter 1"
01,0002,audiobook,"Harry Potter Book 1 - Chapter 2"
01,0003,audiobook,"Harry Potter Book 1 - Chapter 3"
02,0001,album,"Beatles - Abbey Road - Track 1"
03,0001,story,"The Three Little Pigs"
```

## Safety Features

- **Overwrite protection** - Asks for confirmation before overwriting existing folders
- **Validation** - Checks file types, folder numbers, and paths
- **Error handling** - Stops on errors with clear messages
- **Preview** - Shows what will be done before executing

## Troubleshooting

### "Permission denied"

Make sure the script is executable:
```bash
chmod +x add_audio_content.sh
```

### "No MP3 files were copied"

- Check that your content folder contains `.mp3` files (case-insensitive)
- Verify the path is correct

### "Folder number must be between 1 and 99"

TonUINO supports folders 01-99 only. Use auto-detection or choose a valid number.

### Files not in correct order

The script sorts files alphabetically. Ensure your source files are named in the order you want:
```
01_chapter_one.mp3
02_chapter_two.mp3
03_chapter_three.mp3
```

## Advanced Usage

### Batch Processing

Add multiple audiobooks:

```bash
for dir in /audiobooks/*; do
  ./add_audio_content.sh \
    --type audiobook \
    --content "$dir" \
    --name "$(basename "$dir")"
done
```

### Custom SD Card Location

```bash
./add_audio_content.sh \
  --type album \
  --content "/path/to/music" \
  --sd-dir "/mnt/sdcard/custom-location"
```

## Integration with TonUINO

After running the script:

1. **Copy to SD Card** - Copy the entire `sd-card-englisch` folder to your SD card
2. **Insert SD Card** - Put the SD card in your TonUINO
3. **Create RFID Card**:
   - Enter Admin Menu (hold all 3 buttons)
   - Select "Configure New Card"
   - Choose playback mode matching your type
   - Select the folder number the script created
   - Place blank RFID card on reader

## Notes

- The script preserves the `mp3/` and `advert/` system folders
- Only `.mp3` files are processed (case-insensitive: `.MP3`, `.Mp3` also work)
- Files are sorted alphabetically when copying from folders
- The script is non-destructive to existing content (unless you confirm overwrite)

## Contributing

Feel free to enhance the script with additional features like:
- Support for other audio formats (with conversion)
- GUI interface
- Automatic RFID card writing
- Bulk CSV import
- Custom track naming patterns
