import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Code copied from https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python


def emailuser(email, wachtwoord, bericht):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    mail_content = f"""
Skyscanner update. Vlucht AMS-CAN beschikbaar.

{bericht}

{current_time}: Dit is een automatisch bericht.
"""
    # The mail addresses and password
    sender_address = email
    sender_pass = wachtwoord
    receiver_address = email

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = "Raspberry Pi 1"
    message['To'] = receiver_address

    # The subject line
    message['Subject'] = 'Skyscanner Update'

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)

    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
