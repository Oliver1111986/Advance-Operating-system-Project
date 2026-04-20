"""
organizer.py - File Organizer Module (Part B)
Project: SysInfo Pro
Developer: Prince M. Gbolon
SRS Reference: Section 3.2 (ORG-CAT-01 to ORG-SUM-04)
Allowed Libraries: os, shutil

This module scans a user-specified directory, categorizes files by extension,
and moves them into organized subfolders. It handles duplicates, permissions,
and invalid paths gracefully while preserving all original data.
"""

import os
import shutil

# ============================================================================
# FILE CATEGORY MAPPING (SRS Requirement B1)
# ============================================================================
CATEGORIES = {
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Programs": [".exe", ".msi", ".bat", ".sh", ".py"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

def get_category(filename: str) -> str:
    """
    Determine the category of a file based on its extension.
    Args:
        filename: Name of the file to categorize
    Returns:
        Category name (e.g., 'Documents', 'Images', 'Others')
    """
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_folder(target_path: str) -> dict:
    """
    Core logic: Scan, categorize, and move files safely.
    Args:
        target_path: Absolute path to the folder to organize
    Returns:
        Dictionary containing counts of moved files per category
    """
    summary = {}    
    for filename in os.listdir(target_path):
        source_path = os.path.join(target_path, filename)
        
        if not os.path.isfile(source_path):
            continue
            
        category = get_category(filename)
        dest_folder = os.path.join(target_path, category)
        os.makedirs(dest_folder, exist_ok=True)
        dest_path = os.path.join(dest_folder, filename)
        
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            counter = 2
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
                counter += 1
                
        try:
            shutil.move(source_path, dest_path)
            summary[category] = summary.get(category, 0) + 1
        except PermissionError:
            print(f"  ⚠️  Skipped '{filename}': Permission denied")
        except Exception as e:
            print(f"  ⚠️  Skipped '{filename}': {e}")
            
    return summary

def start():
    """
    Entry point called by main.py. Handles user input, validation, and summary output.
    Integrates cleanly with the main menu flow.
    """
    target_path = input("  Enter folder path to organize: ").strip().strip('"').strip("'")
    
    if not os.path.exists(target_path):
        print("\n  ❌ Error: Path does not exist.")
        return
    if not os.path.isdir(target_path):
        print("\n  ❌ Error: Path is not a valid directory.")
        return
        
    print(f"\n  📂 Scanning: {target_path}")
    print("  Organizing files... Please wait.\n")
    
    summary = organize_folder(target_path)
    
    print("  ══ ORGANIZATION SUMMARY ══")
    if not summary:        print("  No files found to organize.")
    else:
        total_moved = 0
        for category, count in sorted(summary.items()):
            print(f"  {category:<12}: {count} file(s)")
            total_moved += count
        print(f"  {'─' * 25}")
        print(f"  {'Total Moved':<12}: {total_moved} file(s)")
    print("  ════════════════════════")