# Define the number of log entries to display
$log_entries = 10

# Check if there's an argument provided for the number of log entries
if ($args.Count -eq 1) {
    $log_entries = $args[0]
}

# Check if the current directory is a Git repository
if (-not (Test-Path .git -PathType Container)) {
    Write-Host "Not a Git repository. Exiting..."
    exit 1
}

# Run git log command
git log -n $log_entries
