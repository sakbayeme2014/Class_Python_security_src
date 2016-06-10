#!/usr/bin/env python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def smtp_hotmail_file():

 sender = "sender mail"
 receiver = "receiver mail"
 msg_object = MIMEMultipart()
 msg_object['send'] = sender
 msg_object['recv'] = receiver
 msg_object['Subject'] = " file attachment send to you "
 body = " i send you one file "
 msg_object.attach(MIMEText(body, 'plain'))
 filename = "C:/file.pdf"
 file_object = open("C:/file.pdf", "rb")
 msg2_object = MIMEBase('application' , 'octect-stream')
 msg2_object.set_payload((file_object).read())
 msg2_object.add_header('Content-Disposition' , "file_object; filename = %s" % filename)
 msg_object.attach(msg2_object)
 smtp_object = smtplib.SMTP('smtp.live.com' , 587)
 smtp_object.ehlo()
 smtp_object.starttls
 smtp_object.ehlo()
 smtp_object.login('username' , 'password')
 text = msg_object.as_string()
 smtp_object.sendmail(sender , receiver , text)
 smtp_object.quit()

smtp_hotmail_file()
