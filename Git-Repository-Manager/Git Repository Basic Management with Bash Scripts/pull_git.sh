#!/bin/bash

# Define the remote repository URL
remote_repo="https://github.com/yourusername/yourrepository.git"

# Define the branch to pull
branch="main"  # Change this to your desired branch name

# Check if the current directory is a Git repository
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
    echo "Not a Git repository. Exiting..."
    exit 1
fi

# Check if there are any uncommitted changes in the local repository
if ! git diff --quiet --exit-code; then
    echo "There are uncommitted changes in the local repository. Please commit or stash them first."
    exit 1
fi

# Check if 'origin' remote already exists, if not, add it
if ! git remote show origin &>/dev/null; then
    echo "Adding 'origin' remote..."
    git remote add origin "$remote_repo"
fi

# Pull changes from the remote repository
echo "Pulling changes from the remote repository..."
git pull origin "$branch"
