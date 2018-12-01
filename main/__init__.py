from downloader.MailPdfDownloader import MailPdfDownloader
from downloader.MailAccountInfo import MailAccountInfo

if __name__ == "__main__":
    a = ['Hello','World']
    print(a)
    print('Hello','World',sep=' ')

    account = MailAccountInfo("address@gmail.com","password","imap.gmail.com")
    mailDownloader = MailPdfDownloader(account)

    mailDownloader.read_email()