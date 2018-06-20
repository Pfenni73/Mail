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
smtp_server = 'mail.gmx.net' # 1und1 SMTP Server
smtp_port = 587
benutzer = 'mp.raspi@gmx.net'
pwd = 'mp1998Raspi!'
sender = 'mp.raspi@gmx.net'
receiver = 'michael.pfenninger@voegele.com' # mehrer receiver müssen mit ', ' getrennt werden
subject = 'Raspi-Datei WWarmwasser.png und Fussbodenheizung.png'
preambletext = 'Graphikdateien vom Raspi02, die um 0:01 Uhr erstellt wurden, fuer den vorangegangenen Tag.'
filepath_selected = "/media/usb/daten/*.png"


msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Date'] = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
msg['Subject'] = subject

msg.attach(MIMEText(preambletext))


##for file in glob.glob(filepath_selected):
##    with open(file, "rb") as fp:
##        part = MIMEApplication(
##        fp.read(),
##        Name=basename(file))
##        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
##        msg.attach(part)


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