#!/bin/bash

# Function to prompt for input and validate
prompt_for_input() {
    read -p "$1: " input
    while [[ -z "$input" ]]; do
        echo "Input cannot be empty."
        read -p "$1: " input
    done
    echo "$input"
}

# Prompt for first name
first_name=$(prompt_for_input "Enter your first name")

# Prompt for last name
last_name=$(prompt_for_input "Enter your last name")

# Template file path
template_file="./LICENSE_Template.txt"

# Check if the template file exists
if [ ! -f "$template_file" ]; then
    echo "Template file '$template_file' not found."
    exit 1
fi

# Directory where new files will be created
output_directory="."
mkdir -p "$output_directory"

# Output filenames
output_file="$output_directory/LICENSE"

# Replace placeholders with user-provided names
sed "s/FIRST_NAME/$first_name/g; s/LAST_NAME/$last_name/g" "$template_file" > "$output_file"

echo "Names replaced in file:"
echo "  $output_file"
