from mailClient import MailClient

mc = MailClient('mail.gmx.net', 587, 'mp.raspi@gmx.net', 'mp1998Raspi!', 'mp.raspi@gmx.net')
mc.sendMail('michael.pfenninger@voegele.com', 'Mein Test erfolgreich', 'Dies ist der Body')