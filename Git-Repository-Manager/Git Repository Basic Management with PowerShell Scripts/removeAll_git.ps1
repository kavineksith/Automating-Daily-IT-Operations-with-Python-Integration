# Function to remove .git directory
function Remove-GitDirectory {
    if (Test-Path -Path ".git" -PathType Container) {
        Write-Host "Removing .git folder..."
        Remove-Item -Path ".git" -Recurse -Force
        Write-Host ".git folder removed."
    }
    else {
        Write-Host ".git folder not found."
    }
}

# Function to remove license file
function Remove-License {
    if (Test-Path -Path "LICENSE" -PathType Leaf) {
        Write-Host "Removing LICENSE file..."
        Remove-Item -Path "LICENSE"
        Write-Host "LICENSE file removed."
    }
    else {
        Write-Host "LICENSE file not found."
    }
}

# Function to remove .gitattributes file
function Remove-GitAttributes {
    if (Test-Path -Path ".gitattributes" -PathType Leaf) {
        Write-Host "Removing .gitattributes file..."
        Remove-Item -Path ".gitattributes"
        Write-Host ".gitattributes file removed."
    }
    else {
        Write-Host ".gitattributes file not found."
    }
}

# Function to remove .gitignore file
function Remove-GitIgnore {
    if (Test-Path -Path ".gitignore" -PathType Leaf) {
        Write-Host "Removing .gitignore file..."
        Remove-Item -Path ".gitignore"
        Write-Host ".gitignore file removed."
    }
    else {
        Write-Host ".gitignore file not found."
    }
}

# Get a list of directories in the current directory
$folders = Get-ChildItem -Directory

# Store the current directory
$current_dir = Get-Location

# Iterate over each folder
foreach ($folder in $folders) {
    $folderName = $folder.Name
    Write-Host "Processing folder: $folderName"

    # Navigate to the folder
    Set-Location -Path $folder.FullName -ErrorAction Continue

    # Remove .git directory
    Remove-GitDirectory

    # Remove license, .gitattributes, and .gitignore files
    Remove-License
    Remove-GitAttributes
    Remove-GitIgnore

    # Navigate back to the parent directory
    Set-Location -Path $current_dir
}

Write-Host "Done."
