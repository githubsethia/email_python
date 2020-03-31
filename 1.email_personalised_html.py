#this file can be used to send Personalised message using HTML 
#Please do not use filename as email.py - it causes some issues
#Turn Allow less secure apps to ON. 
#Be aware that this makes it easier for others to gain access to your account.
#read the html (message) file and save it as a template object
#substitute name with actual name in the template object

# Import smtplib for the actual sending function
import smtplib
from pathlib import Path
from string import Template

email_pwd = 'XXXXXX'
# Import the email modules we'll need
from email.message import EmailMessage

#Create the container email message
msg = EmailMessage()
msg['From'] = 'Manish Sethia'
msg['To'] = 'manish.sethia@gmail.com'
msg['Subject'] = 'Testing 1'
#Email body
body = Template(Path('index.html').read_text())
msg.set_content(body.substitute(name = 'Lovely'),'html')

#send the message via GMAIL SMTP server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() #Identify yourself to the server
    smtp.starttls() #Used to encrypt the SMTP connection (Transport Layer Security)
    smtp.login('manish.sethia@gmail.com', email_pwd)
    smtp.send_message(msg)
    print('all good boss!')
