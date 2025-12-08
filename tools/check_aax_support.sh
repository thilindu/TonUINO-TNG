#!/bin/bash
# Check if system is ready for AAX audiobook conversion

echo "=================================================="
echo "TonUINO AAX Support - System Check"
echo "=================================================="
echo

# Check Python
echo "Checking Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    echo "  ✅ $PYTHON_VERSION"
else
    echo "  ❌ Python3 not found"
    echo "     Install: sudo apt install python3"
    exit 1
fi

# Check tkinter
echo "Checking tkinter..."
if python3 -c "import tkinter" 2>/dev/null; then
    echo "  ✅ tkinter is available"
else
    echo "  ❌ tkinter not found"
    echo "     Install: sudo apt install python3-tk"
    exit 1
fi

# Check for AAX converters
echo "Checking AAX converters..."
CONVERTER_FOUND=0

if command -v AAXtoMP3 &> /dev/null; then
    echo "  ✅ AAXtoMP3 found"
    CONVERTER_FOUND=1
else
    echo "  ❌ AAXtoMP3 not found"
fi

if command -v ffmpeg &> /dev/null; then
    FFMPEG_VERSION=$(ffmpeg -version 2>&1 | head -n1)
    echo "  ✅ ffmpeg found: $FFMPEG_VERSION"
    CONVERTER_FOUND=1
else
    echo "  ❌ ffmpeg not found"
fi

echo
if [ $CONVERTER_FOUND -eq 0 ]; then
    echo "⚠️  WARNING: No AAX converter found!"
    echo "   You can still use the GUI for MP3 files."
    echo "   To enable AAX support, install one of:"
    echo
    echo "   Option 1 - AAXtoMP3 (Recommended):"
    echo "     https://github.com/KrumpetPirate/AAXtoMP3"
    echo
    echo "   Option 2 - FFmpeg:"
    echo "     Ubuntu/Debian: sudo apt install ffmpeg"
    echo "     Mac: brew install ffmpeg"
    echo
else
    echo "✅ AAX conversion is supported!"
fi

echo
echo "=================================================="
echo "Summary"
echo "=================================================="
echo "  Python:           ✅ Ready"
echo "  tkinter:          ✅ Ready"
if [ $CONVERTER_FOUND -eq 1 ]; then
    echo "  AAX Converter:    ✅ Ready"
    echo
    echo "🎉 Your system is ready for AAX audiobooks!"
    echo
    echo "Next steps:"
    echo "  1. Get your activation bytes from:"
    echo "     https://github.com/audiamus/AaxAudioConverter"
    echo "  2. Launch the GUI: ./launch_gui.sh"
    echo "  3. Select an AAX file and enter activation bytes"
else
    echo "  AAX Converter:    ⚠️  Not available"
    echo
    echo "✅ Your system is ready for MP3 files!"
    echo "⚠️  Install a converter to enable AAX support"
fi

echo
echo "📖 Documentation: README_AAX_SUPPORT.md"
echo "=================================================="
