# Define the remote repository URL
$remote_repo = "https://github.com/yourusername/yourrepository.git"

# Define the branch to pull
$branch = "main"  # Change this to your desired branch name

# Check if the current directory is a Git repository
if (-not (Test-Path .git -PathType Container)) {
    Write-Host "Not a Git repository. Exiting..."
    exit 1
}

# Check if there are any uncommitted changes in the local repository
if ((git status --porcelain | Measure-Object).Count -ne 0) {
    Write-Host "There are uncommitted changes in the local repository. Please commit or stash them first."
    exit 1
}

# Check if 'origin' remote already exists, if not, add it
if (-not (git remote show origin -ErrorAction SilentlyContinue)) {
    Write-Host "Adding 'origin' remote..."
    git remote add origin $remote_repo
}

# Pull changes from the remote repository
Write-Host "Pulling changes from the remote repository..."
git pull origin $branch
