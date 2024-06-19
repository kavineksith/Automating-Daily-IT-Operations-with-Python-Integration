# Define functions to remove files

function Remove-License {
    if (Test-Path "LICENSE" -PathType Leaf) {
        Write-Host "Removing LICENSE file in current folder..."
        Remove-Item "LICENSE"
        Write-Host "LICENSE file removed."
    }
    else {
        Write-Host "LICENSE file not found in current folder."
    }
}

function Remove-GitAttributes {
    if (Test-Path ".gitattributes" -PathType Leaf) {
        Write-Host "Removing .gitattributes file in current folder..."
        Remove-Item ".gitattributes"
        Write-Host ".gitattributes file removed."
    }
    else {
        Write-Host ".gitattributes file not found in current folder."
    }
}

function Remove-GitIgnore {
    if (Test-Path ".gitignore" -PathType Leaf) {
        Write-Host "Removing .gitignore file in current folder..."
        Remove-Item ".gitignore"
        Write-Host ".gitignore file removed."
    }
    else {
        Write-Host ".gitignore file not found in current folder."
    }
}

# Store the current directory
$current_dir = Get-Location

# Get a list of directories in the current directory
$folders = Get-ChildItem -Directory

# Iterate over each folder
foreach ($folder in $folders) {
    $folderName = $folder.Name
    Write-Host "Processing folder: $folderName"

    # Check if the folder is not empty
    if ((Get-ChildItem -Path $folder.FullName).Count -gt 0) {
        Write-Host "Folder is not empty"

        # Navigate to the folder
        Set-Location -Path $folder.FullName -ErrorAction Continue

        # Remove license, .gitattributes, and .gitignore files
        Remove-License
        Remove-GitAttributes
        Remove-GitIgnore

        # Navigate back to the parent directory
        Set-Location -Path $current_dir
    }
    else {
        Write-Host "Folder is empty"
        Write-Host "Skipping removal of files in empty folder."
    }
}

Write-Host "Done."
