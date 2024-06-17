#!/bin/bash

# Iterate over child folders
for folder in */; do
    folder=${folder%*/}  # Remove trailing slash
    echo "Processing repository: $folder"

    # Check if the folder is a Git repository
    if [ -d "$folder/.git" ]; then
        # Change directory to the repository
        cd "$folder" || continue

        # If the argument is '.', stage all files and folders in the current directory
        if [ "$1" = "." ]; then
            echo "Staging all files and folders in the repository..."
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
    else
        echo "Not a Git repository: $folder"
    fi
done
