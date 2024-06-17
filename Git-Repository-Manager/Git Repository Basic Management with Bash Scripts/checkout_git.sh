#!/bin/bash

# Function to switch to a branch
switch_to_branch() {
    read -p "Enter the name of the branch to switch to: " new_branch_name
    git checkout $new_branch_name
}

# Function to delete a branch
delete_branch() {
    read -p "Enter the name of the branch to delete: " branch_to_delete
    git branch -D $branch_to_delete
}

# Function to create a new branch
create_branch() {
    read -p "Enter the name of the new branch to create: " new_branch_name
    git checkout -b $new_branch_name
}

# Main menu
echo "Select an action:"
echo "1. Switch to a branch"
echo "2. Delete a branch"
echo "3. Create a new branch"
read -p "Enter your choice (1-3): " choice

case $choice in
    1) switch_to_branch ;;
    2) delete_branch ;;
    3) create_branch ;;
    *) echo "Invalid choice. Exiting." ;;
esac
