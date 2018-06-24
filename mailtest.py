#[code=php]
#!/usr/bin/python
# -*- coding: utf-8 -*-


import smtplib
import glob
import datetime
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


#Mail parameter
smtp_server = 'mail.gmx.net' # gmx SMTP Server
smtp_port = 587
<<<<<<< HEAD
benutzer = 'user@gmx.net'
pwd = 'password'
sender = 'user@gmx.net'
receiver = 'receiver@gmail.com' # mehrer receiver müssen mit ', ' getrennt werden
>>>>>>> ffab2c2f505491372e32ecf1a2a9aa6df993662a
subject = 'Mein Bild'
preambletext = 'Eben aufgenommen!'
filepath_selected = "/home/pi/Pictures/*.jpeg"


msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Date'] = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
msg['Subject'] = subject

msg.attach(MIMEText(preambletext))
print (msg)


##for file in glob.glob(filepath_selected):
##    with open(file, "rb") as fp:
##        part = MIMEApplication(
##        fp.read(),
##        Name=basename(file))
##        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
##        msg.attach(part)

fp =  open("/home/pi/Pictures/Bild2018-06-21.jpeg", "rb")
part = MIMEApplication(fp.read(), Name=basename("/home/pi/Pictures/Bild2018-06-21.jpeg"))
part['Content-Disposition'] = 'attachment; filename="%s"' % basename("/home/pi/Pictures/Bild2018-06-21.jpeg")
msg.attach(part)

# Send the email via 1und1 SMTP server.
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo ()
    server.login(benutzer, pwd)
    server.send_message(msg)
    server.quit()
    now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    print( now + " - Wettergraphiken erfolgreich gesendet")
except:
    now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    print(now + " - Achtung! e-mail wurde nicht versendet")


#[/php]
