
class MailAccountInfo:
    
    SMTP_PORT   = 993

    def __init__(self, usr = "", pwd="",server=""):
        self.mail_user = usr
        self.password = pwd
        self.server = server

    
