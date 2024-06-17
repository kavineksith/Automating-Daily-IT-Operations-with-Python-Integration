#!/bin/bash

# Define the remote repository URL
remote_repo="https://github.com/yourusername/yourrepository.git"

# Define the local repository directory
local_repo="/path/to/your/local/repository"

# Check if the local repository directory exists
if [ ! -d "$local_repo" ]; then
    echo "Local repository directory not found!"
    exit 1
fi

# Change directory to the local repository
cd "$local_repo" || exit

# Check if there are any uncommitted changes in the local repository
if ! git diff --quiet --exit-code; then
    echo "There are uncommitted changes in the local repository. Please commit or stash them first."
    exit 1
fi

# Check if the origin remote exists, if not, add it
if ! git remote show origin &>/dev/null; then
    echo "Adding 'origin' remote..."
    git remote add origin "$remote_repo"
fi

# Fetch updates from the remote repository
echo "Fetching updates from the remote repository..."
git fetch origin

# Check if there are updates available
if git diff --quiet FETCH_HEAD; then
    echo "No updates available."
else
    # Merge updates into the local branch
    echo "Merging updates into the local branch..."
    git merge origin/master  # Change 'master' to your branch name if different
    if [ $? -eq 0 ]; then
        echo "Updates successfully merged."
    else
        echo "Failed to merge updates."
        exit 1
    fi
fi
