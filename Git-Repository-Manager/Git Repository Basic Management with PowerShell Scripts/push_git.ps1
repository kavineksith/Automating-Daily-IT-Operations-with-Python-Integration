# Define the remote repository URL
$remote_repo = "https://github.com/yourusername/yourrepository.git"

# Define the branch to push
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

# Set up the main branch if it doesn't exist
if (-not (git show-ref --verify --quiet "refs/heads/$branch")) {
    Write-Host "Creating '$branch' branch locally..."
    git checkout -b $branch
}

# Push changes to the remote repository
Write-Host "Pushing changes to the remote repository..."
git push -u origin $branch
