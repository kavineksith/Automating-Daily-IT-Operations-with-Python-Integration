#!/bin/bash

# Check if no arguments are provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file1> [<file2> ... | .]"
    echo "Use '.' to stage all files and folders in the current directory."
    exit 1
fi

# Check if the current directory is a Git repository
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
    echo "Not a Git repository. Exiting..."
    exit 1
fi

# If the argument is '.', stage all files and folders in the current directory
if [ "$1" = "." ]; then
    echo "Staging all files and folders in the current directory..."
    git add .
else
    # Loop through each argument and add them
    for file in "$@"; do
        # Check if the file exists
        if [ -e "$file" ]; then
            echo "Staging file: $file"
            git add "$file"
        else
            echo "File not found: $file"
        fi
    done
fi
