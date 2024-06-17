#!/bin/bash

# Function to merge a branch into main
merge_branch_to_main() {
    read -p "Enter the name of the branch to merge into main: " branch_to_merge
    git checkout main && git merge $branch_to_merge
}

# Main menu
echo "Merge another branch into main:"
merge_branch_to_main
