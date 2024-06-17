## Email Sender Documentation

### Overview

The Email Sender script facilitates the sending of emails with optional attachments using Python's `smtplib`, `email.mime`, and `ssl` libraries. It allows customization of sender's Gmail credentials, recipient email address, email subject, body content, and attachment file.

### Requirements

- Python 3.x
- Gmail account (sender) with less secure app access enabled or using app passwords for Gmail

### Dependencies

- `smtplib`: Used for sending emails via SMTP.
- `email.mime`: Provides classes to create and manipulate email messages.
- `ssl`: Standard library for SSL/TLS support.

### Installation

No additional installation is required beyond Python's standard libraries.

### Configuration

1. **Sender's Email Credentials:**
   - Set `sender_email` and `sender_password` variables in `send_user_email()` function with your Gmail credentials.

2. **Receiver's Email Address:**
   - Specify the recipient's email address (`receiver_email`) where the email will be sent.

3. **Email Content:**
   - Customize `subject` and `body` variables in `send_user_email()` function to define email subject and body text.

4. **Attachment (Optional):**
   - If needed, specify the file path (`attachment`) of the attachment in `send_user_email()` function.

### Usage

#### EmailSender Class

The `EmailSender` class encapsulates methods for sending emails.

##### Methods:

- **`__init__(self, sender_email, sender_password, receiver_email)`**
  - Initializes the sender's email, password, and receiver's email.

- **`send_email(self, subject, body, attachment=None)`**
  - Sends an email with the specified `subject`, `body`, and optional `attachment`.

#### send_user_email Function

This function sends an email using the `EmailSender` class with predefined content and attachment.

#### Main Execution

The script is configured to send a specific email once (`send_user_email()`) when executed directly (`if __name__ == "__main__"`).

### Error Handling

Errors encountered during email sending are caught and printed to the console (`print(f"Error: {e}")`).

### Security Considerations

- **TLS Encryption:** Utilizes `smtplib.SMTP_SSL` with TLS encryption for secure email transmission.
- **Credentials Handling:** Requires securely storing sender's email and password.

### Conclusion

This script provides a straightforward method to send customized emails with optional attachments using Gmail's SMTP server, facilitating automation of email sending tasks. This documentation serves to guide users in understanding, configuring, and effectively utilizing the provided Python script for sending emails with attachments.

### **License**

This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**

Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.