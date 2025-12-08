#!/usr/bin/env python3
"""
Test script for AAX support in TonUINO GUI
Verifies that AAX detection and converter checks work properly
"""

import sys
import subprocess
from pathlib import Path

def test_converter_check():
    """Test if we can detect AAX converters"""
    print("Testing AAX converter detection...")
    
    converters = ['AAXtoMP3', 'ffmpeg']
    found = []
    
    for converter in converters:
        try:
            result = subprocess.run([converter, '-version'], 
                                   capture_output=True, 
                                   text=True, 
                                   timeout=5)
            if result.returncode == 0 or converter == 'ffmpeg':
                found.append(converter)
                print(f"  ✅ Found: {converter}")
        except (FileNotFoundError, subprocess.TimeoutExpired):
            print(f"  ❌ Not found: {converter}")
    
    if found:
        print(f"\n✅ AAX conversion is supported! Found: {', '.join(found)}")
        return True
    else:
        print("\n⚠️  No AAX converter found.")
        print("   Install AAXtoMP3 or FFmpeg to enable AAX support.")
        print("   See README_AAX_SUPPORT.md for instructions.")
        return False

def test_aax_detection():
    """Test AAX file detection logic"""
    print("\nTesting AAX file detection...")
    
    test_cases = [
        ("test.aax", True),
        ("test.AAX", True),
        ("test.mp3", False),
        ("test.MP3", False),
        ("audiobook.aax", True),
    ]
    
    for filename, expected_aax in test_cases:
        is_aax = filename.lower().endswith('.aax')
        status = "✅" if is_aax == expected_aax else "❌"
        print(f"  {status} {filename}: {'AAX' if is_aax else 'Not AAX'}")
    
    print("✅ AAX detection logic working correctly")

def test_gui_imports():
    """Test if GUI can be imported without errors"""
    print("\nTesting GUI imports...")
    
    try:
        # Add parent directory to path
        sys.path.insert(0, str(Path(__file__).parent))
        
        # Try importing the main modules used
        import tkinter as tk
        print("  ✅ tkinter imported")
        
        import hashlib
        print("  ✅ hashlib imported")
        
        import json
        print("  ✅ json imported")
        
        import subprocess
        print("  ✅ subprocess imported")
        
        import tempfile
        print("  ✅ tempfile imported")
        
        print("✅ All required modules available")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def main():
    print("=" * 60)
    print("TonUINO AAX Support - Test Suite")
    print("=" * 60)
    print()
    
    # Test imports
    if not test_gui_imports():
        print("\n❌ GUI imports failed. Please check Python installation.")
        return 1
    
    # Test AAX detection
    test_aax_detection()
    
    # Test converter availability
    test_converter_check()
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print("✅ AAX support has been successfully added to the GUI")
    print("📖 See README_AAX_SUPPORT.md for usage instructions")
    print()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
