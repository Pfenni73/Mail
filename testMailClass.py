from mailClient import MailClient

mc = MailClient('mail.gmx.net', 587, 'mp.raspi@gmx.net', 'password', 'mp.raspi@gmx.net')
mc.attach(['/home/pi/Pictures/Bild2018-06-21.jpeg','/home/pi/Pictures/Bild2018-06-22T13:40:42.516702.jpeg'])
mc.sendMail('michael.pfenninger@voegele.com', 'Mein Test erfolgreich', 'Dies ist der Body')