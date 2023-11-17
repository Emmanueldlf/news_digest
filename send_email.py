import smtplib, ssl
from dotenv import load_dotenv
import os


#Load environment variables
load_dotenv()

#Assigne environment variables
email = os.getenv("email")
email_password = os.getenv("password")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    receiver = email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, email_password)
        server.sendmail(email, receiver, message)
