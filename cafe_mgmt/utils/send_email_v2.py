import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests


def send_email():
    return requests.post(
  		"https://api.mailgun.net/v3/sandbox9788fd2d07244b52aedb93860dbd216b.mailgun.org/messages",
  		auth=("api", "0f1db83d-004332df"),
  		data={"from": "mailgun@sandbox9788fd2d07244b52aedb93860dbd216b.mailgun.org",
  			"to": ["aakash.auth@yopmail.com", "aakash.auth2@yopmail.com"],
  			"subject": "Hello",
  			"text": "Testing some Mailgun awesomeness!"})

# Usage
if __name__ == "__main__":
    send_email()
