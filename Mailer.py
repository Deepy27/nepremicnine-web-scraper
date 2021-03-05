import smtplib
from decouple import config

class Mailer:
    def __init__(self):
        smtpAddress = config('MAIL_SMTP_ADDRESS')
        port = config('MAIL_PORT')
        email = config('MAIL_USER')
        password = config('MAIL_PASSWORD')
        server = smtplib.SMTP(smtpAddress, port)
        server.ehlo()
        server.login(email, password)
        server.starttls()
        self.server = server