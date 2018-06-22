from mailClient import MailClient

mc = MailClient('mail.gmx.net', 587, 'user@gmx.net', 'pw', 'user@gmx.net')
mc.sendMail('receiver@gmail.com', 'Mein Test erfolgreich', 'Dies ist der Body')
