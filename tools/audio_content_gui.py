#!/usr/bin/env python3
"""
TonUINO Audio Content Manager - GUI
A graphical interface for managing audio content on TonUINO SD cards
"""

import os
import sys
import csv
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
from typing import List, Optional
import threading


class TonUINOContentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("TonUINO Audio Content Manager")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Default paths
        self.script_dir = Path(__file__).parent.absolute()
        self.project_root = self.script_dir.parent
        self.sd_card_dir = self.project_root / "sd-card-englisch"
        self.media_list_file = self.project_root / "media-list.csv"
        
        # Variables
        self.content_path = tk.StringVar()
        self.content_name = tk.StringVar()
        self.content_type = tk.StringVar(value="audiobook")
        self.folder_number = tk.StringVar()
        self.auto_folder = tk.BooleanVar(value=True)
        self.sd_dir_path = tk.StringVar(value=str(self.sd_card_dir))
        
        self.setup_ui()
        self.update_next_folder()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        row = 0
        
        # Title
        title_label = ttk.Label(main_frame, text="TonUINO Audio Content Manager", 
                               font=('Helvetica', 16, 'bold'))
        title_label.grid(row=row, column=0, columnspan=3, pady=(0, 20))
        row += 1
        
        # Content Selection
        ttk.Label(main_frame, text="Content Selection", 
                 font=('Helvetica', 12, 'bold')).grid(row=row, column=0, columnspan=3, 
                                                       sticky=tk.W, pady=(0, 5))
        row += 1
        
        # Content path
        ttk.Label(main_frame, text="File/Folder:").grid(row=row, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.content_path, width=50).grid(
            row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        ttk.Button(main_frame, text="Browse File", 
                  command=self.browse_file).grid(row=row, column=2, pady=5)
        row += 1
        
        ttk.Button(main_frame, text="Browse Folder", 
                  command=self.browse_folder).grid(row=row, column=2, pady=5)
        row += 1
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').grid(
            row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        row += 1
        
        # Content Information
        ttk.Label(main_frame, text="Content Information", 
                 font=('Helvetica', 12, 'bold')).grid(row=row, column=0, columnspan=3, 
                                                       sticky=tk.W, pady=(0, 5))
        row += 1
        
        # Content name
        ttk.Label(main_frame, text="Name:").grid(row=row, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.content_name, width=50).grid(
            row=row, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)
        row += 1
        
        # Content type
        ttk.Label(main_frame, text="Type:").grid(row=row, column=0, sticky=tk.W, pady=5)
        type_frame = ttk.Frame(main_frame)
        type_frame.grid(row=row, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        types = [
            ("Audiobook", "audiobook"),
            ("Album", "album"),
            ("Story", "story"),
            ("Single", "single")
        ]
        
        for i, (text, value) in enumerate(types):
            ttk.Radiobutton(type_frame, text=text, variable=self.content_type, 
                           value=value).grid(row=0, column=i, padx=5)
        row += 1
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').grid(
            row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        row += 1
        
        # Folder Configuration
        ttk.Label(main_frame, text="Folder Configuration", 
                 font=('Helvetica', 12, 'bold')).grid(row=row, column=0, columnspan=3, 
                                                       sticky=tk.W, pady=(0, 5))
        row += 1
        
        # Auto folder
        ttk.Checkbutton(main_frame, text="Auto-detect next available folder", 
                       variable=self.auto_folder,
                       command=self.toggle_folder_entry).grid(
            row=row, column=0, columnspan=2, sticky=tk.W, pady=5)
        row += 1
        
        # Manual folder
        ttk.Label(main_frame, text="Folder Number:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.folder_entry = ttk.Entry(main_frame, textvariable=self.folder_number, width=10)
        self.folder_entry.grid(row=row, column=1, sticky=tk.W, pady=5, padx=5)
        ttk.Label(main_frame, text="(1-99)", foreground="gray").grid(
            row=row, column=1, sticky=tk.W, pady=5, padx=(80, 0))
        row += 1
        
        # SD card directory
        ttk.Label(main_frame, text="SD Card Dir:").grid(row=row, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.sd_dir_path, width=50).grid(
            row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        ttk.Button(main_frame, text="Browse", 
                  command=self.browse_sd_dir).grid(row=row, column=2, pady=5)
        row += 1
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').grid(
            row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        row += 1
        
        # Action buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=row, column=0, columnspan=3, pady=10)
        
        ttk.Button(button_frame, text="Add Content", command=self.add_content,
                  style='Accent.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear Form", command=self.clear_form).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(
            side=tk.LEFT, padx=5)
        row += 1
        
        # Progress/Log area
        ttk.Label(main_frame, text="Log", font=('Helvetica', 12, 'bold')).grid(
            row=row, column=0, columnspan=3, sticky=tk.W, pady=(10, 5))
        row += 1
        
        self.log_text = scrolledtext.ScrolledText(main_frame, height=12, width=70, 
                                                   state='disabled', wrap=tk.WORD)
        self.log_text.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), 
                          pady=5)
        main_frame.rowconfigure(row, weight=1)
        
        # Configure styles
        self.setup_styles()
        
        # Initial state
        self.toggle_folder_entry()
        
    def setup_styles(self):
        """Setup custom styles"""
        style = ttk.Style()
        try:
            style.theme_use('clam')
        except:
            pass
            
    def browse_file(self):
        """Browse for a single MP3 file"""
        filename = filedialog.askopenfilename(
            title="Select MP3 File",
            filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")]
        )
        if filename:
            self.content_path.set(filename)
            if not self.content_name.get():
                # Auto-fill name from filename
                name = Path(filename).stem
                self.content_name.set(name)
            
    def browse_folder(self):
        """Browse for a folder containing MP3 files"""
        folder = filedialog.askdirectory(title="Select Folder with MP3 Files")
        if folder:
            self.content_path.set(folder)
            if not self.content_name.get():
                # Auto-fill name from folder name
                name = Path(folder).name
                self.content_name.set(name)
                
    def browse_sd_dir(self):
        """Browse for SD card directory"""
        folder = filedialog.askdirectory(title="Select SD Card Directory")
        if folder:
            self.sd_dir_path.set(folder)
            self.sd_card_dir = Path(folder)
            self.update_next_folder()
            
    def toggle_folder_entry(self):
        """Enable/disable folder number entry based on auto-detect"""
        if self.auto_folder.get():
            self.folder_entry.config(state='disabled')
            self.update_next_folder()
        else:
            self.folder_entry.config(state='normal')
            
    def update_next_folder(self):
        """Update the next available folder number"""
        if self.auto_folder.get():
            next_folder = self.get_next_folder()
            self.folder_number.set(str(next_folder))
            
    def get_next_folder(self) -> int:
        """Get the next available folder number"""
        max_folder = 0
        sd_dir = Path(self.sd_dir_path.get())
        
        if sd_dir.exists():
            for item in sd_dir.iterdir():
                if item.is_dir() and item.name.isdigit() and len(item.name) == 2:
                    folder_num = int(item.name)
                    if folder_num > max_folder:
                        max_folder = folder_num
                        
        return max_folder + 1
    
    def log(self, message: str, level: str = "INFO"):
        """Add a message to the log"""
        self.log_text.config(state='normal')
        
        # Color coding
        if level == "ERROR":
            tag = "error"
            prefix = "❌ ERROR: "
        elif level == "SUCCESS":
            tag = "success"
            prefix = "✅ SUCCESS: "
        elif level == "WARNING":
            tag = "warning"
            prefix = "⚠️  WARNING: "
        else:
            tag = "info"
            prefix = "ℹ️  INFO: "
            
        self.log_text.insert(tk.END, prefix + message + "\n", tag)
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')
        
        # Configure tags
        self.log_text.tag_config("error", foreground="red")
        self.log_text.tag_config("success", foreground="green")
        self.log_text.tag_config("warning", foreground="orange")
        self.log_text.tag_config("info", foreground="black")
        
        self.root.update()
        
    def clear_log(self):
        """Clear the log"""
        self.log_text.config(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state='disabled')
        
    def clear_form(self):
        """Clear all form fields"""
        self.content_path.set("")
        self.content_name.set("")
        self.content_type.set("audiobook")
        self.auto_folder.set(True)
        self.toggle_folder_entry()
        self.clear_log()
        self.log("Form cleared")
        
    def validate_inputs(self) -> bool:
        """Validate all inputs"""
        # Check content path
        content = self.content_path.get().strip()
        if not content:
            self.log("Please select a file or folder", "ERROR")
            return False
            
        content_path = Path(content)
        if not content_path.exists():
            self.log(f"Content path does not exist: {content}", "ERROR")
            return False
            
        # Check if it contains MP3 files
        if content_path.is_file():
            if not content.lower().endswith('.mp3'):
                self.log("Selected file is not an MP3", "ERROR")
                return False
        else:
            mp3_files = list(content_path.glob("*.mp3")) + list(content_path.glob("*.MP3"))
            if not mp3_files:
                self.log("Selected folder contains no MP3 files", "ERROR")
                return False
                
        # Check content name
        if not self.content_name.get().strip():
            self.log("Please enter a name for the content", "ERROR")
            return False
            
        # Check folder number
        try:
            folder_num = int(self.folder_number.get())
            if folder_num < 1 or folder_num > 99:
                self.log("Folder number must be between 1 and 99", "ERROR")
                return False
        except ValueError:
            self.log("Invalid folder number", "ERROR")
            return False
            
        # Check SD card directory
        sd_dir = Path(self.sd_dir_path.get())
        if not sd_dir.exists():
            self.log(f"SD card directory does not exist: {sd_dir}", "ERROR")
            return False
            
        return True
        
    def copy_mp3_files(self, source: Path, dest_folder: Path) -> int:
        """Copy MP3 files to destination folder"""
        dest_folder.mkdir(parents=True, exist_ok=True)
        
        track_num = 1
        copied_count = 0
        
        if source.is_file():
            # Single file
            dest_file = dest_folder / f"{track_num:04d}.mp3"
            shutil.copy2(source, dest_file)
            self.log(f"Copied: {source.name} -> {dest_file.name}")
            copied_count = 1
        else:
            # Directory - copy all MP3 files in sorted order
            mp3_files = sorted(list(source.glob("*.mp3")) + list(source.glob("*.MP3")))
            
            for mp3_file in mp3_files:
                dest_file = dest_folder / f"{track_num:04d}.mp3"
                shutil.copy2(mp3_file, dest_file)
                self.log(f"Copied: {mp3_file.name} -> {dest_file.name}")
                track_num += 1
                copied_count += 1
                
        return copied_count
        
    def update_media_list(self, folder_num: int, content_type: str, 
                         content_name: str, track_count: int):
        """Update the media-list.csv file"""
        # Create CSV if it doesn't exist
        if not self.media_list_file.exists():
            with open(self.media_list_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Folder', 'Index', 'Type', 'Track'])
                
        # Add entries for each track
        with open(self.media_list_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            for i in range(1, track_count + 1):
                folder_str = f"{folder_num:02d}"
                index_str = f"{i:04d}"
                
                if track_count == 1:
                    track_name = content_name
                elif content_type == "audiobook":
                    track_name = f"{content_name} - Chapter {i}"
                else:
                    track_name = f"{content_name} - Track {i}"
                    
                writer.writerow([folder_str, index_str, content_type, track_name])
                
        self.log(f"Updated media-list.csv with {track_count} entries", "SUCCESS")
        
    def add_content(self):
        """Main function to add content"""
        # Validate inputs
        if not self.validate_inputs():
            return
            
        # Clear previous log
        self.clear_log()
        
        # Get values
        content_path = Path(self.content_path.get())
        content_name = self.content_name.get().strip()
        content_type = self.content_type.get()
        folder_num = int(self.folder_number.get())
        sd_dir = Path(self.sd_dir_path.get())
        
        folder_str = f"{folder_num:02d}"
        dest_folder = sd_dir / folder_str
        
        self.log("=" * 60)
        self.log("Starting content addition process...")
        self.log(f"Type: {content_type}")
        self.log(f"Name: {content_name}")
        self.log(f"Folder: {folder_str}")
        self.log("=" * 60)
        
        # Check if folder exists
        if dest_folder.exists():
            result = messagebox.askyesno(
                "Folder Exists",
                f"Folder {folder_str} already exists. Do you want to overwrite it?"
            )
            if not result:
                self.log("Operation cancelled by user", "WARNING")
                return
            shutil.rmtree(dest_folder)
            self.log(f"Removed existing folder {folder_str}", "WARNING")
            
        try:
            # Copy files
            self.log("Copying MP3 files...")
            track_count = self.copy_mp3_files(content_path, dest_folder)
            
            if track_count == 0:
                self.log("No MP3 files were copied", "ERROR")
                return
                
            self.log(f"Successfully copied {track_count} track(s)", "SUCCESS")
            
            # Update media list
            self.log("Updating media-list.csv...")
            self.update_media_list(folder_num, content_type, content_name, track_count)
            
            # Success message
            self.log("=" * 60)
            self.log("Content added successfully!", "SUCCESS")
            self.log("=" * 60)
            self.log(f"Folder: {folder_str} ({dest_folder})")
            self.log(f"Tracks: {track_count}")
            self.log(f"Type: {content_type}")
            self.log("")
            self.log("Next steps:")
            self.log("1. Copy sd-card folder contents to your SD card")
            self.log(f"2. Use Admin Menu to create RFID card for folder {folder_str}")
            self.log(f"3. Select playback mode '{content_type}' when configuring")
            
            # Update next folder if auto-detect is on
            if self.auto_folder.get():
                self.update_next_folder()
                
            messagebox.showinfo(
                "Success",
                f"Content added successfully!\n\n"
                f"Folder: {folder_str}\n"
                f"Tracks: {track_count}\n"
                f"Type: {content_type}"
            )
            
        except Exception as e:
            self.log(f"Error occurred: {str(e)}", "ERROR")
            messagebox.showerror("Error", f"An error occurred:\n\n{str(e)}")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = TonUINOContentManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()
