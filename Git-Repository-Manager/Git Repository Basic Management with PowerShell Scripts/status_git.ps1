# Check if the current directory is a Git repository
if (-not (Test-Path -Path ".git" -PathType Container)) {
    Write-Host "Not a Git repository. Exiting..."
    exit 1
}

# Run git status command
git status
