# Markdown to HTML Converter Script Documentation

## Overview
This Python script facilitates the conversion of Markdown files to HTML format. It utilizes the `markdown` library to parse and convert Markdown text to HTML. The converted HTML content can be saved to a specified output file.

## Features
- **Markdown to HTML Conversion**: Converts Markdown files to HTML format.
- **File Handling**: Reads Markdown content from a specified input file and saves the converted HTML content to an output file.
- **Error Handling**: Provides robust error handling to handle file not found, invalid input format, and other unexpected errors.

## Script Components

### 1. MarkdownToHTMLConverter Class
- Manages the conversion process from Markdown to HTML.
- Utilizes the `markdown` library to perform the conversion.

### 2. Utility Functions
- **get_non_empty_input**: Ensures user input is not empty, prompting for re-entry if necessary.

### 3. Main Functionality
- **main**: Orchestrates the conversion process by obtaining input and output file paths from the user and invoking the MarkdownToHTMLConverter methods.

## Dependencies
- Python 3.x
- `markdown` library for Markdown to HTML conversion
- `sys` library for system-specific parameters and functions
- `pathlib` library for handling file paths

## Usage
1. **Input Markdown File**: Provide the path to the Markdown file you want to convert.
2. **Output HTML File**: Specify the path where you want to save the converted HTML file.
3. **Conversion Process**: The script converts the Markdown content to HTML and saves it to the specified output file.
4. **Completion**: Upon successful conversion, the script confirms the completion of the conversion process.

## Conclusion
The Markdown to HTML Converter script offers a simple yet effective solution for converting Markdown content to HTML format. With its intuitive interface and robust error handling, it provides a seamless conversion experience for users.

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.