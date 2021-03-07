import smtplib
from decouple import config

class Mailer:
    # Load enviromental variables
    def __init__(self):
        self.smtpAddress = config('MAIL_SMTP_ADDRESS')
        self.port = config('MAIL_PORT')
        self.email = config('MAIL_USER')
        self.password = config('MAIL_PASSWORD')
        self.mailingList = config('MAIL_TO').split(',')
    
    # Establish a connection to the mail server
    def connect(self):
        server = smtplib.SMTP(self.smtpAddress, self.port)
        self.server = server
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.email, self.password) 

    # Build and send the email
    def sendEmail(self, message, subject = ''):
        # Establish a connection to the mail server
        self.connect()

        # Build the email
        email = "\r\n".join([
            "From: {}".format(self.email),
            "To: {}".format(', '.join(self.mailingList)),
            "Subject: {}".format(subject),
            "",
            "{}".format(message)
        ])

        # Send the email
        self.server.sendmail(self.email, self.mailingList, email)

        print('Email sent!')