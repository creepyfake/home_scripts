import smtplib
import time
from imaplib import IMAP4_SSL
import email

class MailPdfDownloader:
    """Si occupa di scaricare il pdf allegato ad una mail"""
    def __init__(self, info):
        # do nothing
        self.accountInfo = info

    # non funziona così vedi https://developers.google.com/identity/protocols/OAuth2ForDevices
    # bisogna fare login a google e poi usare oauth2 per le successive chiamate.
    # Rivedere struttura: 1 login -> n home_script specifici di google
    def read_email(self):
        
        try:
            # login
            mail = IMAP4_SSL(self.accountInfo.server,993)
            mail.login(self.accountInfo.mail_user,self.accountInfo.password)

            # select the label
            mail.select('inbox')

            type, data = mail.search(None, 'ALL')
            mail_ids = data[0]

            id_list = mail_ids.split()   
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])


            for i in range(latest_email_id,first_email_id, -1):
                typ, data = mail.fetch(i, '(RFC822)' )

                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print('From : ' + email_from + '\n')
                        print('Subject : ' + email_subject + '\n')
        except Exception as e:
            print(str(e))
