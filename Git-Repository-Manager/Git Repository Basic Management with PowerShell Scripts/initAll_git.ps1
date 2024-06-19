# Get a list of directories in the current directory
$folders = Get-ChildItem -Directory

# Loop through each folder
foreach ($folder in $folders) {
    $folderName = $folder.Name
    Write-Host "Processing folder: $folderName"

    # Initialize Git repository in the folder if it doesn't exist
    if (-not (Test-Path (Join-Path $folder.FullName ".git") -PathType Container)) {
        Write-Host "Initializing Git repository in $folderName"
        git init $folder.FullName
    }
    else {
        Write-Host "Git repository already exists in $folderName"
    }
}
