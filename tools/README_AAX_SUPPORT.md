# AAX Audiobook Support for TonUINO

The TonUINO Audio Content Manager now supports Audible AAX audiobooks with automatic conversion to MP3 format.

## Features

- **Direct AAX File Support**: Browse and select AAX files just like MP3 files
- **Automatic Conversion**: AAX files are automatically converted to MP3 during import
- **Batch Processing**: Support for folders containing multiple AAX files
- **DRM Removal**: Uses activation bytes to remove DRM protection

## Requirements

### AAX Converter Tools

#### Option 2: AaxAudioConverter (Windows)
- **Repository**: https://github.com/audiamus/AaxAudioConverter
- **Platform**: Windows desktop application
- **Features**: 
  - GUI-based converter
  - Can extract activation bytes
  - Direct AAX to MP3/M4A/M4B conversion
  - Chapter support
- **Installation**: Download from releases page and install
- **Note**: Can be used standalone for conversion, or just to get activation bytes for use with this GUI

#### Option 3: AAXtoMP3 (Linux/Mac)
- **Repository**: https://github.com/KrumpetPirate/AAXtoMP3
- **Installation** (Linux/Mac):
  ```bash
  git clone https://github.com/KrumpetPirate/AAXtoMP3.git
  cd AAXtoMP3
  sudo make install
  ```

#### Option 4: FFmpeg with AAX Support
- **Download**: https://ffmpeg.org/download.html
- **Installation** (Ubuntu/Debian):
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```
- **Installation** (Mac with Homebrew):
  ```bash
  brew install ffmpeg
  ```

### Activation Bytes

To convert AAX files, you need your Audible account's activation bytes:

1. **Get Your Activation Bytes**:
   - **Recommended**: Use AaxAudioConverter - https://github.com/audiamus/AaxAudioConverter
     - Windows desktop application with GUI
     - Can extract activation bytes from your Audible account
     - Also provides full AAX conversion capabilities
   - Alternative web tool: https://audible-tools.kamsker.at/
   - Alternative CLI tool: https://github.com/inAudible-NG/audible-activator

2. **Format**: 8 hexadecimal characters (e.g., `1a2b3c4d`)

## How to Use

### Adding AAX Audiobooks

1. **Launch the GUI**:
   ```bash
   cd tools
   ./launch_gui.sh
   ```

2. **Select AAX File**:
   - Click "Browse File" button
   - Select your AAX audiobook file
   - The file browser now shows AAX files alongside MP3 files

3. **Enter Activation Bytes**:
   - When an AAX file is selected, an "Activation Bytes" field appears
   - Enter your 8-character activation bytes
   - Example: `1a2b3c4d`

4. **Configure Content**:
   - Enter a name for your audiobook
   - Select content type (typically "Audiobook")
   - Choose folder number (auto-detect recommended)

5. **Add Content**:
   - Click "Add Content" button
   - The GUI will:
     - Convert AAX to MP3 format
     - Copy converted files to the SD card structure
     - Update the database
     - Clean up temporary files

### Conversion Process

The conversion process:
1. Creates a temporary directory for conversion
2. Runs the converter with your activation bytes
3. Extracts audio as high-quality MP3 files
4. Copies MP3 files to destination with proper naming (001.mp3, 002.mp3, etc.)
5. Cleans up temporary files automatically

### Supported Scenarios

- ✅ Single AAX file
- ✅ Folder containing multiple AAX files
- ✅ Mixed folders (AAX and MP3 files together)
- ✅ Large audiobooks (supports files up to 1 hour conversion time)

## Troubleshooting

### "No AAX converter found"
**Solution**: Install AAXtoMP3 or FFmpeg as described in Requirements section.

### "Activation bytes required for AAX conversion"
**Solution**: Get your activation bytes using AaxAudioConverter (https://github.com/audiamus/AaxAudioConverter) or the web tool and enter them in the GUI.

### "Conversion failed"
**Possible causes**:
- Incorrect activation bytes
- Corrupted AAX file
- Insufficient disk space for temporary files

**Solutions**:
- Verify your activation bytes are correct
- Try re-downloading the AAX file
- Check available disk space in /tmp

### "Conversion timed out"
**Cause**: Very large audiobook file (>1 hour of conversion time)

**Solutions**:
- Close other applications to free up CPU resources
- Try converting the file manually using command line tools
- Split the audiobook if possible

## Technical Details

### File Organization

Converted files are organized as:
```
sd-card-englisch/
  01/
    001.mp3  (Chapter 1)
    002.mp3  (Chapter 2)
    ...
```

### Conversion Quality

- **Codec**: MP3 with libmp3lame
- **Quality**: High quality (VBR quality 2)
- **Format**: Preserves original audio quality

### Database Tracking

- MD5 hashes are calculated after conversion
- Track counts are automatically detected
- Metadata is stored in `.tonuino_hash.json`

## Command Line Conversion (Advanced)

If you prefer to convert manually:

### Using AAXtoMP3:
```bash
AAXtoMP3 -A <activation_bytes> -e:mp3 -o output_folder input.aax
```

### Using FFmpeg:
```bash
ffmpeg -activation_bytes <activation_bytes> -i input.aax -vn -c:a libmp3lame -q:a 2 output.mp3
```

## Legal Notice

⚠️ **Important**: 
- Only convert AAX files that you have legally purchased
- Activation bytes are tied to your Audible account
- Removing DRM is for personal use only
- Respect copyright laws in your jurisdiction

## Support

For issues or questions:
1. Check this README
2. Verify converter installation
3. Test activation bytes with command line tools
4. Check the GUI log output for detailed error messages

## Related Documentation

- [GUI User Guide](README_gui.md)
- [Audio Content Management](README_add_audio_content.md)
- [Quick Reference](QUICK_REFERENCE.md)
