# Check if no arguments are provided
if ($args.Count -eq 0) {
    Write-Host "Usage: $PSCommandPath <file1> [<file2> ... | .]"
    Write-Host "Use '.' to stage all files and folders in the current directory."
    exit 1
}

# Check if the current directory is a Git repository
if (-not (Test-Path .git)) {
    Write-Host "Not a Git repository. Exiting..."
    exit 1
}

# If the argument is '.', stage all files and folders in the current directory
if ($args[0] -eq ".") {
    Write-Host "Staging all files and folders in the current directory..."
    git add .
}
else {
    # Loop through each argument and add them
    foreach ($file in $args) {
        # Check if the file exists
        if (Test-Path $file) {
            Write-Host "Staging file: $file"
            git add $file
        }
        else {
            Write-Host "File not found: $file"
        }
    }
}
