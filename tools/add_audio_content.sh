#!/bin/bash

# TonUINO Audio Content Manager
# This script automates adding audio files to the SD card structure
# and updates the media-list.csv file

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SD_CARD_DIR="$PROJECT_ROOT/sd-card-englisch"
MEDIA_LIST="$PROJECT_ROOT/media-list.csv"

# Function to print colored messages
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to show usage
usage() {
    cat << EOF
Usage: $0 --type <TYPE> --content <PATH> [OPTIONS]

Required Arguments:
  --type TYPE           Content type: audiobook, album, story, single
  --content PATH        Path to MP3 file or folder containing MP3 files

Optional Arguments:
  --name NAME          Name/description for the content (for CSV)
  --folder NUM         Specific folder number to use (auto-detects next available if not specified)
  --sd-dir PATH        Path to SD card directory (default: $SD_CARD_DIR)
  --help               Show this help message

Examples:
  # Add an audiobook from a folder
  $0 --type audiobook --content "/path/to/audiobook" --name "Harry Potter Book 1"

  # Add a single MP3 file as an album
  $0 --type album --content "/path/to/album_folder" --name "Greatest Hits"

  # Add to a specific folder number
  $0 --type story --content "/path/to/story.mp3" --folder 15 --name "Bedtime Story"

Supported Types:
  - audiobook: Audio book with multiple chapters
  - album: Music album or collection
  - story: Single story or episode
  - single: Single track

EOF
    exit 1
}

# Function to get next available folder number
get_next_folder() {
    local max_folder=0
    
    if [[ -d "$SD_CARD_DIR" ]]; then
        for dir in "$SD_CARD_DIR"/[0-9][0-9]; do
            if [[ -d "$dir" ]]; then
                folder_num=$(basename "$dir")
                folder_num=$((10#$folder_num))  # Force decimal interpretation
                if [[ $folder_num -gt $max_folder ]]; then
                    max_folder=$folder_num
                fi
            fi
        done
    fi
    
    echo $((max_folder + 1))
}

# Function to format folder number with leading zero
format_folder_number() {
    printf "%02d" "$1"
}

# Function to format track number with leading zeros
format_track_number() {
    printf "%04d" "$1"
}

# Function to check if file is MP3
is_mp3() {
    local file="$1"
    [[ "${file,,}" == *.mp3 ]]
}

# Function to copy and rename MP3 files
copy_mp3_files() {
    local source="$1"
    local dest_folder="$2"
    local track_num=1
    local copied_count=0
    
    mkdir -p "$dest_folder"
    
    if [[ -f "$source" ]]; then
        # Single file
        if is_mp3 "$source"; then
            local dest_file="$dest_folder/$(format_track_number $track_num).mp3"
            cp "$source" "$dest_file"
            print_info "Copied: $(basename "$source") -> $(basename "$dest_file")"
            copied_count=1
        else
            print_error "File is not an MP3: $source"
            return 1
        fi
    elif [[ -d "$source" ]]; then
        # Directory - copy all MP3 files in order
        while IFS= read -r -d '' file; do
            if is_mp3 "$file"; then
                local dest_file="$dest_folder/$(format_track_number $track_num).mp3"
                cp "$file" "$dest_file"
                print_info "Copied: $(basename "$file") -> $(basename "$dest_file")"
                ((track_num++))
                ((copied_count++))
            fi
        done < <(find "$source" -maxdepth 1 -type f -name "*.mp3" -print0 | sort -z)
    else
        print_error "Content path does not exist: $source"
        return 1
    fi
    
    echo "$copied_count"
}

# Function to update media-list.csv
update_media_list() {
    local folder_num="$1"
    local content_type="$2"
    local content_name="$3"
    local track_count="$4"
    
    # Create CSV if it doesn't exist
    if [[ ! -f "$MEDIA_LIST" ]]; then
        echo "Folder,Index,Type,Track" > "$MEDIA_LIST"
    fi
    
    # Add entries for each track
    for ((i=1; i<=track_count; i++)); do
        local index=$(format_track_number $i)
        local track_name="${content_name} - Track ${i}"
        
        if [[ $track_count -eq 1 ]]; then
            track_name="$content_name"
        elif [[ "$content_type" == "audiobook" ]]; then
            track_name="${content_name} - Chapter ${i}"
        fi
        
        echo "$(format_folder_number $folder_num),${index},${content_type},\"${track_name}\"" >> "$MEDIA_LIST"
    done
    
    print_success "Updated media-list.csv with $track_count entries"
}

# Parse command line arguments
TYPE=""
CONTENT=""
NAME=""
FOLDER=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --type)
            TYPE="$2"
            shift 2
            ;;
        --content)
            CONTENT="$2"
            shift 2
            ;;
        --name)
            NAME="$2"
            shift 2
            ;;
        --folder)
            FOLDER="$2"
            shift 2
            ;;
        --sd-dir)
            SD_CARD_DIR="$2"
            shift 2
            ;;
        --help)
            usage
            ;;
        *)
            print_error "Unknown option: $1"
            usage
            ;;
    esac
done

# Validate required arguments
if [[ -z "$TYPE" ]]; then
    print_error "Content type is required (--type)"
    usage
fi

if [[ -z "$CONTENT" ]]; then
    print_error "Content path is required (--content)"
    usage
fi

# Validate content type
case "$TYPE" in
    audiobook|album|story|single)
        ;;
    *)
        print_error "Invalid type: $TYPE. Must be one of: audiobook, album, story, single"
        exit 1
        ;;
esac

# Validate content path
if [[ ! -e "$CONTENT" ]]; then
    print_error "Content path does not exist: $CONTENT"
    exit 1
fi

# Generate default name if not provided
if [[ -z "$NAME" ]]; then
    if [[ -f "$CONTENT" ]]; then
        NAME=$(basename "$CONTENT" .mp3)
    else
        NAME=$(basename "$CONTENT")
    fi
    print_warning "No name provided, using: $NAME"
fi

# Determine folder number
if [[ -z "$FOLDER" ]]; then
    FOLDER=$(get_next_folder)
    print_info "Auto-detected next available folder: $FOLDER"
else
    # Validate folder number
    if [[ ! "$FOLDER" =~ ^[0-9]+$ ]] || [[ $FOLDER -lt 1 ]] || [[ $FOLDER -gt 99 ]]; then
        print_error "Folder number must be between 1 and 99"
        exit 1
    fi
fi

FOLDER_FORMATTED=$(format_folder_number $FOLDER)
DEST_FOLDER="$SD_CARD_DIR/$FOLDER_FORMATTED"

# Check if folder already exists
if [[ -d "$DEST_FOLDER" ]]; then
    print_warning "Folder $FOLDER_FORMATTED already exists"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_info "Operation cancelled"
        exit 0
    fi
    rm -rf "$DEST_FOLDER"
fi

# Main execution
print_info "========================================="
print_info "TonUINO Audio Content Manager"
print_info "========================================="
print_info "Type: $TYPE"
print_info "Content: $CONTENT"
print_info "Name: $NAME"
print_info "Folder: $FOLDER_FORMATTED"
print_info "Destination: $DEST_FOLDER"
print_info "========================================="

# Copy files
print_info "Copying MP3 files..."
TRACK_COUNT=$(copy_mp3_files "$CONTENT" "$DEST_FOLDER")

if [[ $TRACK_COUNT -eq 0 ]]; then
    print_error "No MP3 files were copied"
    exit 1
fi

print_success "Copied $TRACK_COUNT track(s) to folder $FOLDER_FORMATTED"

# Update media list
print_info "Updating media-list.csv..."
update_media_list "$FOLDER" "$TYPE" "$NAME" "$TRACK_COUNT"

# Summary
print_info "========================================="
print_success "Content added successfully!"
print_info "========================================="
print_info "Folder: $FOLDER_FORMATTED ($DEST_FOLDER)"
print_info "Tracks: $TRACK_COUNT"
print_info "Type: $TYPE"
print_info "Name: $NAME"
print_info ""
print_info "Next steps:"
print_info "1. Copy the sd-card-englisch folder contents to your SD card"
print_info "2. Use Admin Menu to create an RFID card for folder $FOLDER_FORMATTED"
print_info "3. Select playback mode '$TYPE' when configuring the card"
print_info "========================================="
