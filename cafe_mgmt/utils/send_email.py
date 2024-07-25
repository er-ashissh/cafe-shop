import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)  # Login to the SMTP server
            server.send_message(msg)  # Send the email
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Usage
if __name__ == "__main__":
    SUBJECT = "Test Email"
    BODY = "This is a test email sent from Python."
    TO_EMAIL = "ashish.sondagar@yopmail.com"
    FROM_EMAIL = "postmaster@sandbox9788fd2d07244b52aedb93860dbd216b.mailgun.org"
    SMTP_SERVER = "smtp.mailgun.org"  # Replace with your SMTP server
    SMTP_PORT = 587  # Port for TLS, 465 for SSL, or 25 for non-secure
    SMTP_USER = "postmaster@sandbox9788fd2d07244b52aedb93860dbd216b.mailgun.org"
    SMTP_PASSWORD = "24800f73ed5c484ea0b32ddae0bf4348-0f1db83d-930eaf8d"

    send_email(SUBJECT, BODY, TO_EMAIL, FROM_EMAIL, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
