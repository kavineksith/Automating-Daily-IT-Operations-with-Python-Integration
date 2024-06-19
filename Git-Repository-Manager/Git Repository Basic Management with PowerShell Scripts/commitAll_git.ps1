# Get a list of directories in the current directory
$folders = Get-ChildItem -Directory

# Loop through each folder
foreach ($folder in $folders) {
    $folderName = $folder.Name
    Write-Host "Processing folder: $folderName"
    
    # Change directory to the folder
    Set-Location $folder.FullName

    # Add and commit files in the folder
    Write-Host "Committing changes in $folderName"
    git add .
    git commit -m "Initial commit"

    # Return to the original directory
    Set-Location $PSScriptRoot
}
