## Bash Email Sender Script Documentation

## Overview

The Bash Email Sender script automates the process of sending emails with optional attachments using Bash scripting and OpenSSL for encryption and SMTP communication. It provides functionalities to generate and encrypt an encryption key, send basic emails, and send emails with attachments.

## Requirements

- Bash shell (tested on Bash 4.x)
- OpenSSL (for encryption)
- SMTP server credentials (stored in `config.json`)

## Features

1. **Key Encryption:**
   - Generates a random encryption key and encrypts it using a passphrase stored in the script (`MySuperSecurePassphrase`).

2. **Email Sending:**
   - Allows sending of basic emails and emails with attachments.
   - Validates sender and receiver email addresses.

3. **Configuration Loading:**
   - Loads SMTP server configuration from `config.json` file and decrypts it using the decrypted encryption key.

## Functions

### `key_encryption()`

- **Description:**
  Generates a random encryption key, encrypts it using a predefined passphrase, and saves both the encryption key and its encrypted form to files.

### `send_email()`

- **Description:**
  Prompts the user for email details (sender, receiver, subject, message), loads SMTP server configuration from `config.json`, and sends a basic email using OpenSSL for SMTP communication.

### `basic_send_email(sender_email, receiver_email, subject, message)`

- **Parameters:**
  - `sender_email`: Sender's email address.
  - `receiver_email`: Receiver's email address.
  - `subject`: Email subject.
  - `message`: Email message content.

- **Description:**
  Sends a basic email with provided parameters. Validates email addresses and creates an email text file (`email.txt`) formatted for SMTP communication.

### `send_email_with_attachments(sender_email, receiver_email, subject, message, attachments...)`

- **Parameters:**
  - `sender_email`: Sender's email address.
  - `receiver_email`: Receiver's email address.
  - `subject`: Email subject.
  - `message`: Email message content.
  - `attachments`: Array of attachment filenames.

- **Description:**
  Sends an email with attachments. Validates email addresses, creates an email text file (`email.txt`) with multipart MIME format for attachments, and sends via SMTP using OpenSSL.

### `load_config()`

- **Description:**
  Loads SMTP server configuration (`smtp_server`, `smtp_port`, `smtp_username`, `smtp_password`) from `config.json` file. Decrypts the configuration using the decrypted encryption key.

#### `main()`

- **Description:**
  Main function to execute the `send_email()` function.

## Usage

1. **Configure `config.json`:**
   - Ensure `config.json` contains SMTP server details encrypted with the same encryption key as `encrypted_encryption_key.key`.

2. **Execute Script:**
   - Run the script (`./email_sender.sh`).
   - Follow prompts to input sender email, receiver email, subject, and message for basic email sending.
   - Attachments are predefined (`attachment_1.pdf`, `attachment_2.pdf`).

## Security Considerations

- **Encryption:**
  Uses AES-256-CBC encryption with PBKDF2 for both the encryption key and SMTP configuration, ensuring secure storage and transmission.

- **Passphrase:**
  Change the default passphrase (`MySuperSecurePassphrase`) for stronger security.

- **Email Validation:**
  Validates sender and receiver email addresses to prevent invalid inputs.

## Conclusion

This script provides a robust solution for sending secure emails with attachments using Bash scripting, OpenSSL for encryption, and SMTP for email delivery. It ensures data security through encryption and provides flexibility with email customization and attachment capabilities. This documentation aims to guide users in understanding, configuring, and effectively utilizing the provided Bash script for automated email sending with attachments securely.

## **License**

This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

## **Disclaimer:**

Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.