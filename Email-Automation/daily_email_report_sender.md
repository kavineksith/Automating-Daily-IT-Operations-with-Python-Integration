## Email Scheduler Documentation

### Overview

The Email Scheduler script automates the sending of daily reports via email using Python's `smtplib`, `schedule`, and `email` libraries. It allows users to specify a sender's Gmail credentials, recipient email address, daily report content, and an optional attachment.

### Requirements

- Python 3.x
- Gmail account (sender) with less secure app access enabled or using app passwords for Gmail

### Dependencies

- `smtplib`: Used for sending emails via SMTP.
- `email.mime`: Provides classes to create and manipulate email messages.
- `schedule`: Library for scheduling tasks.
- `time`: Standard Python library for time-related functions.
- `ssl`: Standard library for SSL/TLS support.

### Installation

No additional installation is required beyond Python's standard libraries.

### Configuration

1. **Sender's Email Credentials:**
   - Provide your Gmail email address (`sender_email`) and password (`sender_password`) in the `send_daily_report()` function.

2. **Receiver's Email Address:**
   - Specify the recipient's email address (`receiver_email`) where the daily report will be sent.

3. **Daily Report Content:**
   - Customize the `subject` and `body` variables in the `send_daily_report()` function to tailor the email content as needed.

4. **Attachment (Optional):**
   - If a file needs to be attached, specify its path (`attachment`) in the `send_daily_report()` function.

### Usage

#### EmailSender Class

The `EmailSender` class encapsulates methods for sending emails.

##### Methods:

- **`__init__(self, sender_email, sender_password, receiver_email)`**
  - Initializes the sender's email, password, and receiver's email.

- **`send_email(self, subject, body, attachment=None)`**
  - Sends an email with the specified `subject`, `body`, and optional `attachment`.

### send_daily_report Function

This function sends the daily report email using the `EmailSender` class.

### Scheduling

The script schedules the `send_daily_report()` function to run daily at 09:00 using `schedule.every().day.at("09:00").do(send_daily_report)`.

### Running the Script

The script runs indefinitely (`while True`) to continuously check and execute scheduled tasks.

### Error Handling

Errors encountered during email sending are caught and displayed via console output (`print(f"Error: {e}")`).

### Security Considerations

- **TLS Encryption:** Uses `smtplib.SMTP_SSL` with TLS encryption to securely connect to Gmail.
- **Credentials Handling:** Requires storing sender's email and password securely.

### Conclusion

This script provides a straightforward method to automate the sending of daily reports via Gmail, offering flexibility with email content and optional attachments while ensuring secure and reliable email delivery. This documentation should help users understand, configure, and effectively use the provided Python script for scheduling and sending daily emails.

## **License**

This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**

Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.