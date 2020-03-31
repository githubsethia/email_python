#This file can be used for general understanding and sending emails using python
# Please do not use filename as email.py - it causes some issues
#Turn Allow less secure apps to ON. 
#Be aware that this makes it easier for others to gain access to your account.

# Import smtplib for the actual sending function
import smtplib
email_pwd = 'XXXXXXXX'
# Import the email modules we'll need
from email.message import EmailMessage

#Create the container email message
msg = EmailMessage()
msg['From'] = 'Manish Sethia'
msg['To'] = 'manish.sethia@chubb.com'
msg['Subject'] = 'Testing 1'

#Email body
msg.set_content('Hurray! My first automated email from python!!')

#send the message via GMAIL SMTP server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() #Identify yourself to the server
    smtp.starttls() #Used to encrypt the SMTP connection (Transport Layer Security)
    smtp.login('manish.sethia@gmail.com', email_pwd)
    smtp.send_message(msg)
    print('all good boss!')
