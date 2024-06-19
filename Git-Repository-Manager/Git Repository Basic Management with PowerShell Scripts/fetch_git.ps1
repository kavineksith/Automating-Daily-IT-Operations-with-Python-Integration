# Define the remote repository URL
$remote_repo = "https://github.com/yourusername/yourrepository.git"

# Define the local repository directory
$local_repo = "/path/to/your/local/repository"

# Check if the local repository directory exists
if (-not (Test-Path $local_repo -PathType Container)) {
    Write-Host "Local repository directory not found!"
    exit 1
}

# Change directory to the local repository
Set-Location $local_repo -ErrorAction Stop

# Check if there are any uncommitted changes in the local repository
if ((git status --porcelain | Measure-Object).Count -ne 0) {
    Write-Host "There are uncommitted changes in the local repository. Please commit or stash them first."
    exit 1
}

# Check if the origin remote exists, if not, add it
if (-not (git remote show origin -ErrorAction SilentlyContinue)) {
    Write-Host "Adding 'origin' remote..."
    git remote add origin $remote_repo
}

# Fetch updates from the remote repository
Write-Host "Fetching updates from the remote repository..."
git fetch origin

# Check if there are updates available
if (git diff --quiet FETCH_HEAD) {
    Write-Host "No updates available."
}
else {
    # Merge updates into the local branch
    Write-Host "Merging updates into the local branch..."
    git merge origin/master  # Change 'master' to your branch name if different
    if ($LastExitCode -eq 0) {
        Write-Host "Updates successfully merged."
    }
    else {
        Write-Host "Failed to merge updates."
        exit 1
    }
}
