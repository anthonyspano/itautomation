#creating message
from email.message import EmailMessage
message = EmailMessage()
sender = "emailID@gmail.com"
recipient = "you@example.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = "Email title"
body = "Body of the message"
message.set_content(body)

#email attachments
import os.path
attachment_path = ""
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1) # separate
with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=os.path.basename(attachment_path))
 
#sending message through smtp
import smtplib
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1) # strictly for debug
import getpass
mail_pass = getpass.getpass('Password: ') # sent in plain text

mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()

