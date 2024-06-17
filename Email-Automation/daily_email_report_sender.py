import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time
import ssl


class EmailSender:
    def __init__(self, sender_email, sender_password, receiver_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email

    def send_email(self, subject, body, attachment=None):
        # Create message
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = self.receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        if attachment:
            with open(attachment, 'rb') as attachment_file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment_file.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {attachment}'
            )
            message.attach(part)

        # Send email
        try:
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL('smtp.gmail.com', 587, context=context)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            server.quit()


def send_daily_report():
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'
    receiver_email = 'receiver_email@gmail.com'
    subject = 'Daily Report'
    body = 'This is your daily report.'
    attachment = 'daily_report.pdf'  # Example attachment file

    try:
        email_sender = EmailSender(sender_email, sender_password, receiver_email)
        email_sender.send_email(subject, body, attachment)
    except Exception as e:
        print(f"Error: {e}")


# Schedule the email to be sent daily at a specific time
schedule.every().day.at("09:00").do(send_daily_report)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
