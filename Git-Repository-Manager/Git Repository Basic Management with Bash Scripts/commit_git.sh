#!/bin/bash

# Specify the current directory as the folder to process
folder="."

# Check if the folder exists
if [ -d "$folder" ]; then
    echo "Processing folder: $folder"

    # Add and commit files in the folder
    echo "Committing changes in $folder"
    (cd "$folder" && git add . && git commit -m "Initial commit")
else
    echo "Folder '$folder' not found."
fi
