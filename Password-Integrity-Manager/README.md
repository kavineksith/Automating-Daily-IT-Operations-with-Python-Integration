# Password Checksum Generator Script Documentation

## Overview
This Python script generates a checksum hash value for user-provided passwords using various hashing algorithms. Users can choose from a range of hashing algorithms to generate the checksum. The script provides an interactive interface for entering passwords and selecting the desired checksum method.

## Features
- **Checksum Generation**: Computes checksum hash values for user passwords using specified hashing algorithms.
- **Multiple Hashing Algorithms**: Supports commonly used hashing algorithms such as SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, and MD5.
- **Interactive Interface**: Prompts users for input regarding password and checksum method, ensuring user engagement and ease of use.
- **Error Handling**: Provides robust error handling to handle unexpected inputs and interruptions gracefully.

## Script Components

### 1. ScreenManager Class
- Manages clearing the screen based on the operating system.
- Utilizes the `os` library for clearing the screen.

### 2. ChecksumPWD Class
- Computes the checksum hash value for user-provided passwords using the selected hashing algorithm.
- Utilizes the `hashlib` library for hashing.

### 3. Utility Functions
- **get_usr_password**: Prompts the user for a password and validates it.
- **get_checksum_method**: Prompts the user for a checksum method (hashing algorithm) and validates it.

### 4. Main Functionality
- **main**: Orchestrates the password checksum generation process by obtaining user input for the password and checksum method and invoking the appropriate methods from the ChecksumPWD class.

## Dependencies
- Python 3.x
- `hashlib` library for cryptographic hashing functions
- `os` library for system-specific functions
- `time` library for time-related operations
- `sys` library for system-specific parameters and functions

## Usage
1. **User Password**: Enter the password for which you want to generate the checksum.
2. **Checksum Method**: Choose the hashing algorithm (Checksum Method) from the provided list (sha1, sha224, sha256, sha384, sha512, md5).
3. **Checksum Generation**: The script computes the checksum hash value for the entered password using the selected hashing algorithm.
4. **Completion**: Upon successful generation, the script displays the original password and its corresponding checksum hash value.

## Conclusion
The Password Checksum Generator script provides a convenient tool for generating checksum hash values for user passwords using various hashing algorithms. With its interactive interface and robust error handling, it offers a seamless user experience for password checksum generation and verification.

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.