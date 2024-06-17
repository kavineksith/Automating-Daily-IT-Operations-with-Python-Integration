#!/bin/bash

# Function to remove license file
remove_license() {
    if [[ -f "LICENSE" ]]; then
        echo "Removing LICENSE file in current folder..."
        rm LICENSE
        echo "LICENSE file removed."
    else
        echo "LICENSE file not found in current folder."
    fi
}

# Function to remove .gitattributes file
remove_gitattributes() {
    if [[ -f ".gitattributes" ]]; then
        echo "Removing .gitattributes file in current folder..."
        rm .gitattributes
        echo ".gitattributes file removed."
    else
        echo ".gitattributes file not found in current folder."
    fi
}

# Function to remove .gitignore file
remove_gitignore() {
    if [[ -f ".gitignore" ]]; then
        echo "Removing .gitignore file in current folder..."
        rm .gitignore
        echo ".gitignore file removed."
    else
        echo ".gitignore file not found in current folder."
    fi
}

# Store the current directory
current_dir=$(pwd)

# Loop through each folder in the current directory
for folder in */; do
    folder=${folder%*/}  # Remove trailing slash
    echo "Processing folder: $folder"

    # Check if the folder is not empty
    if [ "$(ls -A "$folder")" ]; then
        echo "Folder is not empty"

        # Navigate to the folder
        cd "$folder" || { echo "Error: Could not navigate to $folder"; exit 1; }

        # Remove license, .gitattributes, and .gitignore files
        remove_license
        remove_gitattributes
        remove_gitignore

        # Navigate back to the parent directory
        cd "$current_dir"
    else
        echo "Folder is empty"
        echo "Skipping removal of files in empty folder."
    fi
done

echo "Done."
