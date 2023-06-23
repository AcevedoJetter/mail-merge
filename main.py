# Code to send emails using Python3 and macOS

#   Code and allowing Google account to send emails: https://www.youtube.com/watch?v=g_j6ILT-X0k
#   Creating an environment variable: https://support.apple.com/guide/terminal/use-environment-variables-apd382cc5fa-4f58-4449-b20a-41c53c006f8f/mac

import os
import ssl
import smtplib
from email.message import EmailMessage

email_sender = "YOUR EMAIL"
sender_password = os.environ.get("NAME-OF-ENVIRONMENT-VARIABLE")

f = open("people.txt", "r")
for people in f:
    parsed_info = people.replace("\n", "").split(" ")
    title = parsed_info[0]
    last_name = parsed_info[1]
    email_receiver = parsed_info[2]

    msg = EmailMessage()
    body = f"""
Dear {title} {last_name},

BODY

Best,

SIGNATURE
    """

    msg["From"] = email_sender
    msg["To"] = email_receiver
    msg["Subject"] = "ENTER SUBJECT"
    msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, sender_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())

f.close()
