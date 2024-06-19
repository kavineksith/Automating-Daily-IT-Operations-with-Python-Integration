# Define the number of log entries to display
$log_entries = 10

# Check if there's an argument provided for the number of log entries
if ($args.Count -eq 1) {
    $log_entries = $args[0]
}

# Get a list of directories in the current directory
$folders = Get-ChildItem -Directory

# Iterate over each folder
foreach ($folder in $folders) {
    $folderName = $folder.Name
    Write-Host "Processing repository: $folderName"

    # Check if the folder is a Git repository
    if (Test-Path (Join-Path $folder.FullName ".git") -PathType Container) {
        # Change directory to the repository
        Set-Location $folder.FullName -ErrorAction Continue

        # Run git log command
        Write-Host "Commit log for repository: $folderName"
        git log -n $log_entries
    }
    else {
        Write-Host "Not a Git repository: $folderName"
    }
}
