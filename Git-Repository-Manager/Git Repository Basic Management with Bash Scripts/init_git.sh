#!/bin/bash

# Specify the current directory as the folder to process
folder="."

# Check if the folder exists
if [ -d "$folder" ]; then
    echo "Processing folder: $folder"

    # Initialize Git repository in the folder if it doesn't exist
    if [ ! -d "$folder/.git" ]; then
        echo "Initializing Git repository in $folder"
        (cd "$folder" && git init)
    else
        echo "Git repository already exists in $folder"
    fi
else
    echo "Folder '$folder' not found."
fi
