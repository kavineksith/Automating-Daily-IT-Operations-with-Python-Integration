# Specify the files you want to copy
$files_to_copy = @(".gitattributes", ".gitignore", "LICENSE", "robots.txt")

# Get a list of directories in the current directory
$folders = Get-ChildItem -Directory

# Loop through each folder
foreach ($folder in $folders) {
    $folderName = $folder.Name
    Write-Host "Processing folder: $folderName"

    # Check if the folder is not empty
    if ((Get-ChildItem $folder.FullName).Count -gt 0) {
        Write-Host "Folder is not empty"

        # Check if the files don't exist in the folder
        foreach ($file in $files_to_copy) {
            if (-not (Test-Path (Join-Path $folder.FullName $file))) {
                Write-Host "Copying $file to $folderName"
                Copy-Item $file $folder.FullName
            }
            else {
                Write-Host "$file already exists in $folderName"
            }
        }
    }
    else {
        Write-Host "Folder is empty"

        # Copy files directly into empty folders
        foreach ($file in $files_to_copy) {
            Write-Host "Copying $file to $folderName"
            Copy-Item $file $folder.FullName
        }
    }
}
