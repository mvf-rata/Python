import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



server = smtplib.SMTP('smtp.gmail.com', 25)
#Starting server
server.ehlo()

with open('password.txt', 'r') as f:
	password = f.read()

server.login('buckgy31.mf@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Max'
msg['To'] = 'friedl-maximilian@gmx.de'
msg['Subject'] = 'Just a Test'

with open('message.txt', 'r') as f:
	message = f.read()

msg.attach(MIMEText(message, 'plain'))

#FOR AN ATTACHMENT
filename = 'python.jpg'
attachment = open(filename, 'rb')
Payload
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg,attach(p)

text = msg.as_string()
server.sendmail('buckgy31.mf@gmail.com', 'friedl-maximilian@gmx.de', text)