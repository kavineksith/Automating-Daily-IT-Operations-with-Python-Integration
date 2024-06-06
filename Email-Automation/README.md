# Secure Email Sender Script Documentation

## Overview
This script, written in Python, facilitates secure email transmission by encrypting sensitive email configuration details and utilizing the SMTP protocol for sending emails. It includes functionality for sending basic emails, emails with attachments, and supports custom email templates.

## Features
- **Secure Configuration Handling**: The script securely manages email configuration details by encrypting them using Fernet encryption and a passphrase. Configuration details include SMTP server address, port, username, and password.
- **Email Sending**: Provides methods for sending both basic emails and emails with attachments using the configured SMTP server.
- **Advanced Email Templating**: Supports custom email templates with placeholders for sender, receiver, subject, and message, allowing for dynamic email content generation.

## Script Components

### 1. SecureEmailConfig Class
- Responsible for loading and decrypting the encrypted configuration file.
- Utilizes Fernet encryption to decrypt the configuration file using the provided passphrase.

### 2. EmailSender Class
- Handles the sending of emails using SMTP.
- Includes methods for sending basic emails and emails with attachments.
- Provides email address validation.

### 3. SecureEmailSender Class
- Combines SecureEmailConfig and EmailSender functionalities.
- Initializes the EmailSender with decrypted configuration details.

### 4. Utility Functions
- **key_encryption**: Generates and encrypts an encryption key to be used for securing sensitive data.
- **get_non_empty_input**: Ensures user input is not empty, prompting for re-entry if necessary.

### 5. Main Functionality
- **main**: Orchestrates the email sending process by obtaining user input for email details and invoking SecureEmailSender methods.

## Usage
1. **Configuration Setup**: Ensure the existence of the configuration file containing SMTP server details, and an encrypted encryption key file.
2. **Customization**: Optionally provide custom email templates and attachments.
3. **Execution**: Run the script and follow the prompts to input email details.
4. **Security Considerations**: Maintain the confidentiality of the passphrase and encrypted key file.

## Dependencies
- Python 3.x
- `cryptography` library for Fernet encryption
- `smtplib` library for SMTP functionality
- `email` library for constructing email messages
- `json` library for handling JSON files
- `os` library for operating system related functionalities
- `re` library for regular expression operations
- `sys` library for system-specific parameters and functions

These dependencies are essential for the proper execution and functionality of the Secure Email Sender script.

## Conclusion
The Secure Email Sender script provides a robust solution for sending emails securely, protecting sensitive configuration details through encryption. Its versatility allows for various email transmission scenarios, making it suitable for both personal and professional use cases.

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.