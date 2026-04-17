# ==========================================================
# File Organizer Module (Part B)
# Project: SysInfo Pro
# Author: Prince M. Gbolon
#
# Description:
# This program organizes files in a user-selected folder
# into categories based on their file extensions.
# It automatically creates folders and moves files into them.
# ==========================================================

import os
import shutil

# Dictionary that maps file categories to their extensions
CATEGORIES = {
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Programs": [".exe", ".msi", ".bat", ".sh", ".py"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

# Function to determine the category of a file based on its extension
def get_category(file):
    ext = os.path.splitext(file)[1].lower()  # Extract file extension
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category  # Return matching category
    return "Others"  # Default category if no match is found

# Main function that organizes files in a folder
def organize_folder():
    # Ask user to input folder path
    path = input("Enter folder path: ")

    # Check if the folder exists
    if not os.path.exists(path):
        print("❌ Folder does not exist!")
        return

    summary = {}  # Dictionary to store count of moved files per category

    # Loop through all items in the folder
    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        # Only process files (ignore subfolders)
        if os.path.isfile(full_path):
            category = get_category(file)  # Get file category
            dest_folder = os.path.join(path, category)

            # Create destination folder if it does not exist
            os.makedirs(dest_folder, exist_ok=True)

            dest_file = os.path.join(dest_folder, file)

            # Handle duplicate file names by renaming
            count = 1
            base, ext = os.path.splitext(file)
            while os.path.exists(dest_file):
                dest_file = os.path.join(dest_folder, f"{base}_{count}{ext}")
                count += 1

            try:
                # Move file to the appropriate folder
                shutil.move(full_path, dest_file)

                # Update summary count
                summary[category] = summary.get(category, 0) + 1

            except Exception as e:
                # Handle errors without stopping the program
                print(f"⚠️ Could not move {file}: {e}")

    # Print summary of organized files
    print("\n📊 Summary:")
    for category, count in summary.items():
        print(f"  {category}: {count} files")

# Start function for main.py integration
def start():
    """Entry point called by main.py for file organization feature"""
    print("\n" + "="*45)
    print("        FILE ORGANIZER")
    print("="*45)
    organize_folder()