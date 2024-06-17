#!/bin/bash

# Specify the files you want to copy
files_to_copy=(".gitattributes" ".gitignore" "LICENSE" "robots.txt")

# Loop through each folder in the current directory
for folder in */; do
    folder=${folder%*/}  # Remove trailing slash
    echo "Processing folder: $folder"
    
    # Check if the folder is not empty
    if [ "$(ls -A "$folder")" ]; then
        echo "Folder is not empty"
        
        # Check if the files don't exist in the folder
        for file in "${files_to_copy[@]}"; do
            if [ ! -e "$folder/$file" ]; then
                echo "Copying $file to $folder"
                cp "$file" "$folder"
            else
                echo "$file already exists in $folder"
            fi
        done
    else
        echo "Folder is empty"
        
        # Copy files directly into empty folders
        for file in "${files_to_copy[@]}"; do
            echo "Copying $file to $folder"
            cp "$file" "$folder"
        done
    fi
done
