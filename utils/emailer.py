import smtplib, ssl
from django.conf import settings

login_message="""\
From: [FROM]
Reply-To: [FROM]
To: [TO]
Subject: OTP for login
Hi,

OTP for your login is [OTP].

Regards,
Support Team
"""

register_message="""\
From: [FROM]
Reply-To: [FROM]
To: [TO]
Subject: Account Verification
Hi,

Greetings!

You are just a step away from accessing your account. 
OTP for your account verification is [OTP].

Regards,
Support Team
"""

class Emailer(object):
    
    def __init__(self, smtp_server=settings.SMTP_SERVER, port=settings.SMTP_PORT, sender=settings.SMTP_SENDER_EMAIL, password=settings.SMTP_SENDER_PASSWORD):
        self.url = smtp_server
        self.port = port
        self.sender = sender
        self.password = password

    def send_otp_email(self, receiver_email, otp):
        msg=login_message.replace('[FROM]', self.sender).replace('[TO]', receiver_email).replace('[OTP]', otp)
        self.send_email(receiver_email, msg)
        
    def send_verify_email(self, receiver_email, otp):
        msg=register_message.replace('[FROM]', self.sender).replace('[TO]', receiver_email).replace('[OTP]', otp)
        self.send_email(receiver_email, msg)

    def send_email(self, receiver_email, msg):
        with smtplib.SMTP(self.url,self.port) as smtp_server:
            smtp_server.login(self.sender, self.password)
            smtp_server.sendmail(self.sender, receiver_email, msg)
