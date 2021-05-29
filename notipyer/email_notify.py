from .credential_handler import credentials, _set_email_credentials
from .errors import GmailLoginException, RecipientNotPresentException
from .async_decorator import Async
import smtplib

SMTP_GMAIL_URL = 'smtp.gmail.com'
SMTP_GMAIL_PORT = 587

mail_cred = credentials()


def _check_valid_string(string):
    if len(string) > 0:
        return True
    return False


def set_email_config(email, password):
    global mail_cred
    if _check_valid_string(email) and _check_valid_string(password):
        _set_email_credentials(mail_cred, email, password)


@Async
def send_email(subject, message, to_addr, cc_addr=None, bcc_addr=None):
    global mail_cred
    global SMTP_GMAIL_URL, SMTP_GMAIL_PORT

    to_addr, cc_addr, bcc_addr = _check_recipients(to_addr, cc_addr, bcc_addr)

    client = smtplib.SMTP(SMTP_GMAIL_URL, SMTP_GMAIL_PORT)
    client.starttls()
    client = _login_client(client)
    recipients, email_body = _build_email(subject, message, mail_cred.EMAIL_ID, to_addr, cc_addr, bcc_addr)
    client.sendmail(mail_cred.EMAIL_ID, recipients, email_body)
    client.quit()


def _login_client(client):
    try:
        client.login(mail_cred.EMAIL_ID, mail_cred.EMAIL_PASS)
        return client
    except smtplib.SMTPAuthenticationError as _:
        raise GmailLoginException()


def _check_recipients(to_addr, cc_addr, bcc_addr):
    if to_addr is None:
        to_addr = []
    if cc_addr is None:
        cc_addr = []
    if bcc_addr is None:
        bcc_addr = []

    if type(to_addr) is str:
        to_addr = [to_addr]
    if type(cc_addr) is str:
        cc_addr = [cc_addr]
    if type(bcc_addr) is str:
        bcc_addr = [bcc_addr]

    if len(to_addr + cc_addr + bcc_addr) < 1:
        raise RecipientNotPresentException()

    return to_addr, cc_addr, bcc_addr


def _build_email(subject, text, from_email, to_emails, cc_emails, bcc_emails):
    message = "From: %s\r\n" % from_email \
              + "To: %s\r\n" % ",".join(to_emails) \
              + "CC: %s\r\n" % ",".join(cc_emails) \
              + "Subject: %s\r\n" % subject \
              + "\r\n" \
              + text
    toaddrs = to_emails + cc_emails + bcc_emails
    return toaddrs, message
