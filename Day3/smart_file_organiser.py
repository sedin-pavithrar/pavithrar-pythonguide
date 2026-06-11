# Smart File Organiser 
# Real-world app: macOS Finder / Windows Explorer 
# Problem 
# Build a file organiser using Python's builtin modules (os, shutil, pathlib). 
# Given a messy folder path, scan all files and automatically move them into subfolders by extension type - Images, Documents, Videos, Others. 
# Print a summary report of how many files were moved where.


import os 

import shutil 

from pathlib import Path 

  

CATEGORIES = { 

    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".webp"], 

    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"], 

    "Videos":    [".mp4", ".mov", ".avi", ".mkv"], 

    "Others":    []   # catch-all 

} 

  

def organise_folder(folder_path: str) -> dict: 

    # scans folder, moves files, returns summary dict 
    

    pass 

  

def print_report(summary: dict) -> None: 

    # prints formatted report 

    pass 