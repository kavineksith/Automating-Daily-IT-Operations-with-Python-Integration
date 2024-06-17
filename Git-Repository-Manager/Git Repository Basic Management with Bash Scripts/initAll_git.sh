#!/bin/bash

# Loop through each folder in the current directory
for folder in */; do
    folder=${folder%*/}  # Remove trailing slash
    echo "Processing folder: $folder"
    
    # Initialize Git repository in the folder
    if [ ! -d "$folder/.git" ]; then
        echo "Initializing Git repository in $folder"
        (cd "$folder" && git init)
    else
        echo "Git repository already exists in $folder"
    fi
done
