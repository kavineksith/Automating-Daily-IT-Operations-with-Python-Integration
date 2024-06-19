# Specify the current directory as the folder to process
$folder = Get-Location

# Specify the files you want to copy
$files_to_copy = @(".gitattributes", ".gitignore", "LICENSE", "robots.txt")

# Check if the folder exists
if (Test-Path $folder -PathType Container) {
    Write-Host "Processing folder: $folder"

    # Loop through the specified files to copy
    foreach ($file in $files_to_copy) {
        # Check if the file exists in the current directory
        if (Test-Path (Join-Path $folder $file)) {
            # Loop through each subfolder in the current directory
            Get-ChildItem -Directory | ForEach-Object {
                $subfolder = $_.FullName
                Write-Host "Processing subfolder: $subfolder"

                # Check if the subfolder is not empty
                if ((Get-ChildItem $subfolder).Count -gt 0) {
                    Write-Host "Subfolder is not empty"

                    # Check if the file doesn't exist in the subfolder
                    if (!(Test-Path (Join-Path $subfolder $file))) {
                        Write-Host "Copying $file to $subfolder"
                        Copy-Item (Join-Path $folder $file) $subfolder
                    }
                }
            }
        }
    }
}
else {
    Write-Host "Folder '$folder' not found."
}
