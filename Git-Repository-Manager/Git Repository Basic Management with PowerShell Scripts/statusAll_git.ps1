# Iterate over child folders
foreach ($folder in Get-ChildItem -Directory) {
    $folderName = $folder.Name
    Write-Host "Processing repository: $folderName"

    # Check if the folder is a Git repository
    if (Test-Path -Path "$folderName\.git" -PathType Container) {
        # Change directory to the repository
        Set-Location -Path $folder.FullName

        # Run git status command
        Write-Host "Status for repository: $folderName"
        git status

        # Return to the original directory
        Set-Location -Path $PSScriptRoot
    } else {
        Write-Host "Not a Git repository: $folderName"
    }
}
