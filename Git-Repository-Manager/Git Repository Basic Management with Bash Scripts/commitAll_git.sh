#!/bin/bash

# Loop through each folder in the current directory
for folder in */; do
    folder=${folder%*/}  # Remove trailing slash
    echo "Processing folder: $folder"
    
    # Add and commit files in the folder
    echo "Committing changes in $folder"
    (cd "$folder" && git add . && git commit -m "Initial commit")
done
