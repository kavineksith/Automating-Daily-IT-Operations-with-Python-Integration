#!/bin/bash

# Function to remove .git directory
remove_git() {
    if [[ -d ".git" ]]; then
        echo "Removing .git folder..."
        rm -rf .git
        echo ".git folder removed."
    else
        echo ".git folder not found."
    fi
}

# Function to remove license file
remove_license() {
    if [[ -f "LICENSE" ]]; then
        echo "Removing LICENSE file..."
        rm LICENSE
        echo "LICENSE file removed."
    else
        echo "LICENSE file not found."
    fi
}

# Function to remove .gitattributes file
remove_gitattributes() {
    if [[ -f ".gitattributes" ]]; then
        echo "Removing .gitattributes file..."
        rm .gitattributes
        echo ".gitattributes file removed."
    else
        echo ".gitattributes file not found."
    fi
}

# Function to remove .gitignore file
remove_gitignore() {
    if [[ -f ".gitignore" ]]; then
        echo "Removing .gitignore file..."
        rm .gitignore
        echo ".gitignore file removed."
    else
        echo ".gitignore file not found."
    fi
}

# Array of folder names
# Fetch list of folders using ls command and add them to folders array
folders=$(ls -d */)

# Store the current directory
current_dir=$(pwd)

# Loop through each folder
for folder in $folders; do
    echo "Processing $folder..."
    # Navigate to the folder
    cd "$folder" || { echo "Error: Could not navigate to $folder"; exit 1; }
    # Remove .git directory
    remove_git
    # Remove license, .gitattributes, and .gitignore files
    remove_license
    remove_gitattributes
    remove_gitignore
    # Navigate back to the parent directory
    cd "$current_dir"
done

echo "Done."
