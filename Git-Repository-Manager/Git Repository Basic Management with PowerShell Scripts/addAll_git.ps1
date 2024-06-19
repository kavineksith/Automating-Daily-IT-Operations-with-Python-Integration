# Iterate over child folders
Get-ChildItem -Directory | ForEach-Object {
    $folder = $_.FullName
    Write-Host "Processing repository: $folder"

    # Check if the folder is a Git repository
    if (Test-Path "$folder\.git" -PathType Container) {
        # Change directory to the repository
        Set-Location $folder

        # Check if arguments are provided
        if ($args.Count -eq 0) {
            Write-Host "Usage: $PSCommandPath <file1> [<file2> ... | .]"
            Write-Host "Use '.' to stage all files and folders in the current directory."
            exit 1
        }

        # If the argument is '.', stage all files and folders in the current directory
        if ($args[0] -eq ".") {
            Write-Host "Staging all files and folders in the repository..."
            git add .
        }
        else {
            # Loop through each argument and add them
            foreach ($file in $args) {
                # Check if the file exists
                if (Test-Path $file -PathType Leaf) {
                    Write-Host "Staging file: $file"
                    git add $file
                }
                else {
                    Write-Host "File not found: $file"
                }
            }
        }
    }
    else {
        Write-Host "Not a Git repository: $folder"
    }
}
