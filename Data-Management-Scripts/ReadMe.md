# Data Management Scripts

## Overview
This Python script offers functionalities for system monitoring and data processing. It includes components for uploading data, managing databases, previewing CSV files, processing images, replacing domains in email lists, calculating disk storage, generating timestamps, and previewing CSV data in a formatted manner.

## Components

### 1. DataUploader Class
- Uploads data from a source file to an export file.
- Checks for the existence of source and export files before proceeding with data upload.

### 2. DatabaseManager Class
- Manages SQLite database operations, including database creation, data insertion, and connection closing.
- Processes CSV files to insert data into the database.

### 3. CSVPreviewer Class
- Previews the content of a CSV file by reading each line and displaying it in a formatted manner.
- Provides information about the total number of lines processed.

### 4. ImageProcessor Class
- Processes images within a specified directory by resizing, rotating, and converting them to a different format.
- Handles exceptions such as file not found, permission errors, and unexpected errors during image processing.

### 5. DomainReplacer Class
- Replaces old domain names in a list of email addresses with new domain names.
- Processes source files, performs domain replacement, and writes the modified data to an export file.

### 6. DiskStorageCalculator Class
- Calculates the total size of disk storage based on input values such as cylinders, heads, sectors per track, and bytes per sector.
- Ensures that input values are numeric and provides the total size in gigabytes.

### 7. TimeStampGenerator Class
- Generates timestamps in the format HH:MM:SS for time and DD/MM/YYYY for date.
- Includes a method to generate a report with the current time and date.

### 8. CSVPreviewer Class (Second Implementation)
- An alternative implementation of the CSVPreviewer class.
- Formats the CSV data and displays it with improved readability.

## Dependencies
- Python 3.x
- Standard libraries: os, sys, csv, sqlite3
- Third-party libraries: PIL (Pillow)

## Usage
1. Execute each script using Python 3.x.
2. Follow the provided usage instructions for each script to provide input files, directories, or parameters.
3. View the output or generated files as per the script's functionality.

## Conclusion
The System Monitoring script offers a comprehensive set of tools for system management and data processing tasks. From handling data uploads and managing databases to processing images and generating timestamps, these scripts cover various aspects of system monitoring and data manipulation. Users can leverage these functionalities to streamline their workflows and efficiently manage system resources and data.

