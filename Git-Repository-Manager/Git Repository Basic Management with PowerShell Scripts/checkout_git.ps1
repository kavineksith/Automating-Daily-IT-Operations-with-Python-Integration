# Function to switch to a branch
function switch_to_branch {
    $new_branch_name = Read-Host "Enter the name of the branch to switch to"
    git checkout $new_branch_name
}

# Function to delete a branch
function delete_branch {
    $branch_to_delete = Read-Host "Enter the name of the branch to delete"
    git branch -D $branch_to_delete
}

# Function to create a new branch
function create_branch {
    $new_branch_name = Read-Host "Enter the name of the new branch to create"
    git checkout -b $new_branch_name
}

# Main menu
Write-Host "Select an action:"
Write-Host "1. Switch to a branch"
Write-Host "2. Delete a branch"
Write-Host "3. Create a new branch"
$choice = Read-Host "Enter your choice (1-3)"

switch ($choice) {
    "1" { switch_to_branch }
    "2" { delete_branch }
    "3" { create_branch }
    Default { Write-Host "Invalid choice. Exiting." }
}
