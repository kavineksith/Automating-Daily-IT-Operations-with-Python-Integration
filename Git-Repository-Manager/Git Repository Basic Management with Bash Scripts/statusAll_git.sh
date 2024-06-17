#!/bin/bash

# Iterate over child folders
for folder in */; do
    folder=${folder%*/}  # Remove trailing slash
    echo "Processing repository: $folder"

    # Check if the folder is a Git repository
    if [ -d "$folder/.git" ]; then
        # Change directory to the repository
        cd "$folder" || continue

        # Run git status command
        echo "Status for repository: $folder"
        git status
    else
        echo "Not a Git repository: $folder"
    fi
done
