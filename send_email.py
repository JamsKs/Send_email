import smtplib
import ssl
from email.message import EmailMessage

password = input("Enter your password here: ")
subject = input("Enter the subject here: ")
body = input("Enter the body here: ")
sender_email = input("Enter the sender mail here: ")
receiver_email = input("Enter the receiver's mail here: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())