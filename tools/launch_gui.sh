#!/bin/bash
# TonUINO Audio Content Manager - GUI Launcher

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed"
    echo "Please install Python3 to use the GUI"
    exit 1
fi

# Launch the GUI
python3 "$SCRIPT_DIR/audio_content_gui.py"
