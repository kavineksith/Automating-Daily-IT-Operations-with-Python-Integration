# Specify the current directory as the folder to process
$folder = Get-Location

# Check if the folder exists
if (Test-Path $folder -PathType Container) {
    Write-Host "Processing folder: $folder"

    # Initialize Git repository in the folder if it doesn't exist
    if (-not (Test-Path (Join-Path $folder ".git") -PathType Container)) {
        Write-Host "Initializing Git repository in $folder"
        git init $folder
    }
    else {
        Write-Host "Git repository already exists in $folder"
    }
}
else {
    Write-Host "Folder '$folder' not found."
}
