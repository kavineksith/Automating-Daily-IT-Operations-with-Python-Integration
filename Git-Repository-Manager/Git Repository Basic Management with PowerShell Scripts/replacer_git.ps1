# Function to prompt for input and validate
function Prompt-ForInput {
    param(
        [string]$Prompt
    )
    
    do {
        $input = Read-Host -Prompt $Prompt
        if ([string]::IsNullOrWhiteSpace($input)) {
            Write-Host "Input cannot be empty."
        }
    } while ([string]::IsNullOrWhiteSpace($input))
    
    return $input
}

# Prompt for first name
$firstName = Prompt-ForInput -Prompt "Enter your first name"

# Prompt for last name
$lastName = Prompt-ForInput -Prompt "Enter your last name"

# Template file path
$templateFile = ".\LICENSE_Template.txt"

# Check if the template file exists
if (-not (Test-Path -Path $templateFile -PathType Leaf)) {
    Write-Host "Template file '$templateFile' not found."
    exit 1
}

# Directory where new files will be created
$outputDirectory = "."
if (-not (Test-Path -Path $outputDirectory -PathType Container)) {
    New-Item -ItemType Directory -Path $outputDirectory | Out-Null
}

# Output filename
$outputFile = Join-Path -Path $outputDirectory -ChildPath "LICENSE"

# Replace placeholders with user-provided names
(Get-Content $templateFile) |
    ForEach-Object { $_ -replace "FIRST_NAME", $firstName -replace "LAST_NAME", $lastName } |
    Set-Content -Path $outputFile

Write-Host "Names replaced in file:"
Write-Host "  $outputFile"
