#!/bin/bash

# Specify the current directory as the folder to process
folder="."

# Specify the files you want to copy
files_to_copy=(".gitattributes" ".gitignore" "LICENSE" "robots.txt")

# Check if the folder exists
if [ -d "$folder" ]; then
    echo "Processing folder: $folder"

    # Loop through the specified files to copy
    for file in "${files_to_copy[@]}"; do
        # Check if the file exists in the current directory
        if [ -e "$file" ]; then
            # Loop through each subfolder in the current directory
            for subfolder in "$folder"/*/; do
                subfolder=${subfolder%*/}  # Remove trailing slash
                echo "Processing subfolder: $subfolder"

                # Check if the subfolder is not empty
                if [ "$(ls -A "$subfolder")" ]; then
                    echo "Subfolder is not empty"

                    # Check if the file doesn't exist in the subfolder
                    if [ ! -e "$subfolder/$file" ]; then
                        echo "Copying $file to $subfolder"
                        cp "$file" "$subfolder"

