# Function to merge a branch into main
function Merge-BranchToMain {
    param (
        [string]$branch_to_merge
    )
    
    git checkout main
    git merge $branch_to_merge
}

# Main menu
Write-Host "Merge another branch into main:"
$branch_to_merge = Read-Host "Enter the name of the branch to merge into main"
Merge-BranchToMain -branch_to_merge $branch_to_merge
