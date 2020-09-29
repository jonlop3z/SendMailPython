# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Este correo se envio desde python"
 
# setup the parameters of the message
sender = 'MailFrom@Dominio.com'
recipients = 'MailTo@Dominio.com,MailTo@Dominio.es'
password = "password"
msg['From'] = sender
msg['To'] =  recipients
msg['Subject'] = "Correo de prueba"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(sender, recipients.split(','), msg.as_string())
 
server.quit()
 
print ("successfully sent email to %s:" % (msg['To']))