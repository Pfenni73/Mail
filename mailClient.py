import os
import datetime
import smtplib

class MailClient():
    
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.utils import formatdate

    def __init__(self, mc_smtp_server, mc_smtp_port, mc_user, mc_pwd, mc_sender):
        self.smtp_server = mc_smtp_server
        self.smtp_port = mc_smtp_port
        self.user = mc_user
        self.pwd = mc_pwd
        self.sender = mc_sender
        self.attachment = []
        
    def attach(self, mc_attachment):
        self.attachment = mc_attachment
        
    def sendMail(self, mc_receiver, mc_subject, mc_text):
        msg = self.MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = mc_receiver
        msg['Date'] = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        msg['Subject'] = mc_subject

        msg.attach(self.MIMEText(mc_text))
        
        if len(self.attachment) > 0:
            for fileN in self.attachment:
                fp =  open(fileN, "rb")
                part = self.MIMEApplication(fp.read(), Name=os.path.basename(fileN))
                part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(fileN)
                msg.attach(part)
        
        try:
            server = self.smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.ehlo()
            server.starttls()
            server.ehlo ()
            server.login(self.user, self.pwd)
            server.send_message(msg)
            server.quit()
            now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            print( now + " - Mail erfolgreich gesendet")
        except:
            now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            print(now + " - Achtung! e-mail wurde nicht versendet")