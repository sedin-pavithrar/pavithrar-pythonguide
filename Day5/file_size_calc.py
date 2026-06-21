# Recursion -- File System Size Calculator
# recursion base case os.scandir tree traversal
# Real-world App
# macOS / Windows folder size
# Overview
# folder_size() recursively scans a directory: base case = file (return st_size), recursive case = 
# subdirectory (accumulate). print_tree() prints with 2*indent per level. Also implements factorial and 
# Fibonacci to show clean base case / recursive case pattern. The fundamental building block of 
# compilers, file systems, and DOM parsing.
# Problem
# Recursively calculate total folder size. Print folder tree with indentation like the "tree" terminal 
# command.
# Core Logic
# def folder_size(path):
#  total=0
#  for entry in os.scandir(path):
#  if entry.is_file(): total+=entry.stat().st_size
#  elif entry.is_dir(): total+=folder_size(entry.path) # recursive
#  return total
# Constraints
# • Every recursive function needs a clear base case
# • Display in KB/MB
# • print_tree uses indent*2 spaces per level
# Bonus: Add memoization to fibonacci using a dict cache.

import os


def folder_size(path):
    total = 0

    for entry in os.scandir(path):

        # Base case: file
        if entry.is_file():
            total += entry.stat().st_size

        # Recursive case: subfolder
        elif entry.is_dir():
            total += folder_size(entry.path)

    return total


def print_tree(path, indent=0):
    print("  " * indent + os.path.basename(path))

    for entry in os.scandir(path):

        if entry.is_file():
            print("  " * (indent + 1) + entry.name)

        elif entry.is_dir():
            print_tree(entry.path, indent + 1)


path = input("Enter folder path: ")

print("\nFolder Tree:")
print_tree(path)

size = folder_size(path)

print(f"\nTotal Size: {size / 1024:.2f} KB")