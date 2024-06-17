#!/bin/bash

# Check if the current directory is a Git repository
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
    echo "Not a Git repository. Exiting..."
    exit 1
fi

# Run git status command
git status
