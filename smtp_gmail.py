use this address and modify 
https://www.google.com/settings/security/lesssecureapps  change off > on 

#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def smtp_gmail():
 sender = "sender e-mail"
 receiver = "receiver e-mail"
 msg_object = MIMEMultipart()
 msg_object['send'] = sender
 msg_object['recv'] = receiver
 msg_object['Subject'] = " hi  "
 body = " bybye bybye"
 msg_object.attach(MIMEText(body, 'plain'))
 smtp_object = smtplib.SMTP("smtp.gmail.com" ,  587)
 smtp_object.ehlo()
 smtp_object.starttls()
 smtp_object.ehlo()
 smtp_object.login("username" , "password")
 text = msg_object.as_string()
 smtp_object.sendmail(sender , receiver , text)
 smtp_object.quit()

smtp_gmail()
