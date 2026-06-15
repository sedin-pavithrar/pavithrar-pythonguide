# Smart File Organiser 
# Real-world app: macOS Finder / Windows Explorer 
# Problem 
# Build a file organiser using Python's builtin modules (os, shutil, pathlib). 
# Given a messy folder path, scan all files and automatically move them into subfolders by extension type - Images, Documents, Videos, Others. 
# Print a summary report of how many files were moved where.


import os #checks if folder exists or creates
import shutil #move files 
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Others": []
}

def organise_folder(folder_path: str) -> dict:

    # if not os.path.exists(folder_path):
    #     print("Folder does not exist")
    #     return {} #checks if folder exists if not program stops returns empty dict
    
    if not Path(folder_path).exists():
        print("Folder does not exist")
        return {}

    summary = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Others": 0
    }

    print(f"Organising: {folder_path}")

    folder = Path(folder_path) #D:\python\...

    #iter dir = to iterate over the directory 

    for item in folder.iterdir(): 

        if item.is_dir():
            continue  #skips folder checks only files in that particular dir 

        extension = item.suffix.lower() # item is the file and we are taking that extension alone 
        category = "Others" # default category 

        for cat, extensions in CATEGORIES.items():
            if extension in extensions:
                category = cat
                break # once particular category is found stops search

        destination = folder / category # Downloads/Images
        os.makedirs(destination, exist_ok=True)

        shutil.move(str(item), str(destination / item.name))  #Downloads / Images / photo.jpg

        print(f"Moved {item.name} -> {category}/")

        summary[category] += 1

    return summary


def print_report(summary: dict) -> None:

    print("\nSummary:")

    total = 0

    for category, count in summary.items():
        print(f"{category}: {count} files")
        total += count

    print(f"Total: {total} files organised")  


folder_path = input("Enter folder path: ")

summary = organise_folder(folder_path)

print_report(summary)
