import json
import os
import smtplib
import re
import ssl
import sys
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet


class SecureEmailConfig:
    def __init__(self, config_file_path, key_file_path, passphrase):
        self.config_file_path = config_file_path
        self.key_file_path = key_file_path
        self.passphrase = passphrase
        self.config = None
        self.load_config()

    def load_config(self):
        try:
            # Generate and save the encryption key if the key file doesn't exist
            if not os.path.exists(self.key_file_path):
                key_encryption()

            # Decrypt the encryption key using the passphrase
            with open(self.key_file_path, 'rb') as key_file:
                key_data = key_file.read()
            cipher_suite = Fernet(self.passphrase)
            decrypted_key = cipher_suite.decrypt(key_data)

            # Load the encrypted configuration file using the decrypted key
            with open(self.config_file_path, 'rb') as config_file:
                encrypted_data = config_file.read()
            fernet = Fernet(decrypted_key)
            decrypted_data = fernet.decrypt(encrypted_data).decode()
            self.config = json.loads(decrypted_data)
        except (FileNotFoundError, ValueError, KeyError, json.JSONDecodeError) as e:
            print(f"Error loading configuration: {e}")
            sys.exit(1)


class EmailSender:
    def __init__(self, config):
        self.config = config

    def basic_send_email(self, sender_email, receiver_email, subject, message):
        try:
            smtp_server = self.config['smtp_server']
            smtp_port = self.config['smtp_port']
            smtp_username = self.config['smtp_username']
            smtp_password = self.config['smtp_password']

            # Validate email addresses
            if not self._is_valid_email(sender_email) or not self._is_valid_email(receiver_email):
                raise ValueError("Invalid email address.")

            # Create message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # sender_email = self.config['sender_email']
            # receiver_email = self.config['receiver_email']
            # subject = self.config['subject']
            # message = self.config['message']

            context = ssl.create_default_context()

            # Connect to SMTP server
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
        except (smtplib.SMTPException, ValueError, KeyError) as e:
            print(f"An error occurred while sending the email: {e}")
        finally:
            print("Email sending process completed.")

    def send_email_with_attachments(self, sender_email, receiver_email, subject, message, attachments=None):
        try:
            smtp_server = self.config['smtp_server']
            smtp_port = self.config['smtp_port']
            smtp_username = self.config['smtp_username']
            smtp_password = self.config['smtp_password']

            # Validate email addresses
            if not self._is_valid_email(sender_email) or not self._is_valid_email(receiver_email):
                raise ValueError("Invalid email address.")

            # Create message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # sender_email = self.config['sender_email']
            # receiver_email = self.config['receiver_email']
            # subject = self.config['subject']
            # message = self.config['message']

            # Attach files
            if attachments:
                for attachment in attachments:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(open(attachment, 'rb').read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(attachment)}"')
                    msg.attach(part)

            context = ssl.create_default_context()

            # Connect to SMTP server
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
        except (smtplib.SMTPException, ValueError, KeyError) as e:
            print(f"An error occurred while sending the email: {e}")
        finally:
            print("Email sending process completed.")

    def _is_valid_email(self, email):
        # Regular expression for advanced email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None


class SecureEmailSender:
    def __init__(self, config_file_path, key_file_path, passphrase):
        config = SecureEmailConfig(config_file_path, key_file_path, passphrase).config
        self.email_sender = EmailSender(config)

    def send_email(self, sender_email, receiver_email, subject, message, attachments=None, template=None):
        """
        Sends an email with optional attachments and using a custom template.
        """
        if template:
            with open(template, 'r') as template_file:
                email_template = template_file.read()

            # Replace placeholders in the template with actual content
            placeholders = {
                '{{sender_email}}': sender_email,
                '{{receiver_email}}': receiver_email,
                '{{subject}}': subject,
                '{{message}}': message
            }
            for placeholder, value in placeholders.items():
                email_template = email_template.replace(placeholder, value)

            message = email_template

        # Send email with attachments if provided
        if attachments:
            self.email_sender.send_email_with_attachments(sender_email, receiver_email, subject, message, attachments)
        else:
            self.email_sender.basic_send_email(sender_email, receiver_email, subject, message)


def key_encryption():
    # Generate a random encryption key
    key = Fernet.generate_key()

    # Save the encryption key to a file
    with open('encryption_key.key', 'wb') as key_file:
        key_file.write(key)

    # Encrypt the key file using a passphrase
    passphrase = b'MySuperSecurePassphrase'  # Replace with your passphrase
    cipher_suite = Fernet(passphrase)

    with open('encryption_key.key', 'rb') as key_file:
        key_data = key_file.read()

    encrypted_data = cipher_suite.encrypt(key_data)

    # Save the encrypted data to a new file
    with open('encrypted_encryption_key.key', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


def get_non_empty_input(prompt):
    """
    Prompt the user for input and validate it until a non-empty value is provided.
    """
    user_input = input(prompt)
    while not user_input:
        print("Input cannot be empty.")
        user_input = input(prompt)
    return user_input


def main():
    try:
        # Define parameters and assigning values for them
        config_file_path = 'config.json'  # configuration file
        key_file_path = 'encrypted_encryption_key.key'  # encryption key file
        passphrase = os.environ.get('SMTP_PASSPHRASE', b'MySuperSecurePassphrase')  # passphrase for encryption

        # Get user input for email details
        sender_email = get_non_empty_input("Enter sender email address: ")
        receiver_email = get_non_empty_input("Enter receiver email address: ")
        subject = get_non_empty_input("Enter email subject: ")
        message = get_non_empty_input("Enter email message: ")
        attachments = ['attachment_1.pdf', 'attachment_2.pdf']
        template = 'custom_template.txt'

        email_sender = SecureEmailSender(config_file_path, key_file_path, passphrase)
        email_sender.send_email(sender_email, receiver_email, subject, message, attachments, template)
    except KeyboardInterrupt:
        print("Process interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
