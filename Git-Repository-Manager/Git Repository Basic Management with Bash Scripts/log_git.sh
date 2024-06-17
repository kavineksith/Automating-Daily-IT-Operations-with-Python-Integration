#!/bin/bash

# Define the number of log entries to display
log_entries=10

# Check if there's an argument provided for the number of log entries
if [ $# -eq 1 ]; then
    log_entries="$1"
fi

# Check if the current directory is a Git repository
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
    echo "Not a Git repository. Exiting..."
    exit 1
fi

# Run git log command
git log -n "$log_entries"
