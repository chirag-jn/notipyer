from .credential_handler import EMAIL_ID, EMAIL_PASS, _set_email_credentials
import smtplib


SMTP_GMAIL_URL = 'smtp.gmail.com'
SMTP_GMAIL_PORT = 587


def _check_valid_string(string):
    if len(string) > 0:
        return True
    return False


def set_email_config(email, password):
    if _check_valid_string(email) and _check_valid_string(password):
        _set_email_credentials(email, password)


def send_emails(recipients, message):
    global SMTP_GMAIL_URL, SMTP_GMAIL_PORT
    client = smtplib.SMTP(SMTP_GMAIL_URL, SMTP_GMAIL_PORT)
    client.starttls()
    # TODO: Check if unsecure app access on
    client.login(EMAIL_ID, EMAIL_PASS)
    for recipient in recipients:
        _send_email(client, recipient, message)
    client.quit()


def _send_email(client, recipient, message):
    if client is not None:
        client.sendmail(EMAIL_ID, recipient, message)


def send_email(recipient, message):
    global SMTP_GMAIL_URL, SMTP_GMAIL_PORT
    client = smtplib.SMTP(SMTP_GMAIL_URL, SMTP_GMAIL_PORT)
    client.starttls()
    # TODO: Check if unsecure app access on
    client.login(EMAIL_ID, EMAIL_PASS)
    for recipient in recipient:
        _send_email(client, recipient, message)
    client.quit()