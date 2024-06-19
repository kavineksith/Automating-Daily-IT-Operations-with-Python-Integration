# Specify the current directory as the folder to process
$folder = Get-Location

# Check if the folder exists
if (Test-Path $folder -PathType Container) {
    Write-Host "Processing folder: $folder"

    # Change directory to the folder
    Set-Location $folder

    # Add and commit files in the folder
    Write-Host "Committing changes in $folder"
    git add .
    git commit -m "Initial commit"
}
else {
    Write-Host "Folder '$folder' not found."
}
