import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python"
sender_email = "sender@gmail.com"
receiver_email = "receive@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject