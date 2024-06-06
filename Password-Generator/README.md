# Password Generator Script Documentation

## Overview
This Python script generates passwords of specified length and complexity levels. It allows users to choose between generating normal passwords or secure passwords with specific criteria for complexity. The script utilizes both built-in Python libraries and custom classes for functionality.

## Features
- **Password Generation**: Generates passwords of specified length and complexity.
- **Normal Passwords**: Generates passwords with random characters.
- **Secure Passwords**: Generates passwords with specific criteria for enhanced security.
- **Interactive Interface**: Prompts users for input regarding password length and category.
- **Error Handling**: Provides robust error handling for various user inputs and unexpected errors.

## Script Components

### 1. ScreenManager Class
- Manages clearing the screen based on the operating system.
- Utilizes the `os` library for clearing the screen.

### 2. CharacterLake Class
- Provides a pool of characters (letters, digits, and special characters) for password generation.
- Utilizes the `string` library for character retrieval.

### 3. PasswordGenerator Class
- Handles password generation based on user-defined criteria.
- Utilizes the `random` and `secrets` modules for randomization and secure randomization, respectively.

### 4. Main Functionality
- **main**: Orchestrates the password generation process by obtaining user input for password length and category and invoking the appropriate methods from the PasswordGenerator class.

## Dependencies
- Python 3.x
- `string` library for character pool retrieval
- `secrets` and `random` modules for secure and normal password generation, respectively
- `os` library for system-specific functions
- `time` library for time-related operations
- `sys` library for system-specific parameters and functions

## Usage
1. **Password Length**: Specify the desired length for the generated password.
2. **Password Category**: Choose between generating a normal password (Category 1) or a secure password (Category 2) with specific complexity criteria.
3. **Generated Password**: Upon successful generation, the script displays the generated password.

## Conclusion
The Password Generator script offers a flexible solution for generating passwords tailored to specific requirements. Whether users need a simple, randomly generated password or a secure password meeting specific complexity criteria, this script provides a reliable and user-friendly interface for password generation.