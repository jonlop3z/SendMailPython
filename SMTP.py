# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
from email.mime.base import MIMEBase
from email import encoders
 
# create message object instance
msg = MIMEMultipart()

message = "Este correo se envio desde python3"

# setup the parameters of the message
sender = 'MailFrom@Dominio.com'
recipients = 'MailTo@Dominio.com,MailTo@Dominio.es'
password = "password"
msg['From'] = sender
msg['To'] =  recipients
msg['Subject'] = "Correo de prueba"

#Attach File
part = MIMEBase('application', "octet-stream")
part.set_payload(open("1.png", "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="1.png"')
msg.attach(part)

part = MIMEBase('application', "octet-stream")
part.set_payload(open("Adjunto.txt", "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="Adjunto.txt"')
msg.attach(part)
# attach image to message body
#msg.attach(MIMEImage(open("1.png","rb").read()))
msg.attach(MIMEText(message, 'plain')) 

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(sender, recipients.split(','), msg.as_string())
 
server.quit()
 
print ("successfully sent email to %s:" % (msg['To']))