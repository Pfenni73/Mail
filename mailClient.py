class MailClient():
    import smtplib
    import glob
    import datetime
    from os.path import basename
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.utils import COMMASPACE, formatdate

    def __init__(self, mc_smtp_server, mc_smtp_port, mc_user, mc_pwd, mc_sender):
        self.smtp_server = mc_smtp_server
        self.smtp_port = mc_smtp_port
        self.user = mc_user
        self.pwd = mc_pwd
        self.sender = mc_sender
        
    def sendMail(self, mc_receiver, mc_subject, mc_text):
        msg = self.MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = mc_receiver
        msg['Date'] = self.datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        msg['Subject'] = mc_subject

        msg.attach(self.MIMEText(mc_text))
        
        try:
            server = self.smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.ehlo()
            server.starttls()
            server.ehlo ()
            server.login(self.user, self.pwd)
            server.send_message(msg)
            server.quit()
            now = self.datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            print( now + " - Wettergraphiken erfolgreich gesendet")
        except:
            now = self.datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            print(now + " - Achtung! e-mail wurde nicht versendet")