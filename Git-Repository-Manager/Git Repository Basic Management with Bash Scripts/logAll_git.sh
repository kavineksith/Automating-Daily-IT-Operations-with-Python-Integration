#!/bin/bash

# Define the number of log entries to display
log_entries=10

# Check if there's an argument provided for the number of log entries
if [ $# -eq 1 ]; then
    log_entries="$1"
fi

# Iterate over child folders
for folder in */; do
    folder=${folder%*/}  # Remove trailing slash
    echo "Processing repository: $folder"

    # Check if the folder is a Git repository
    if [ -d "$folder/.git" ]; then
        # Change directory to the repository
        cd "$folder" || continue

        # Run git log command
        echo "Commit log for repository: $folder"
        git log -n "$log_entries"
    else
        echo "Not a Git repository: $folder"
    fi
done
