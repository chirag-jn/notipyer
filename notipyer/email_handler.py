from .credential_handler import EMAIL_ID, EMAIL_PASS
import smtplib


SMTP_GMAIL_URL = 'smtp.gmail.com'
SMTP_GMAIL_PORT = 587


def _check_valid_string(string):
    if len(string) > 0:
        return True
    return False


def set_email_credentials(email, password):
    if _check_valid_string(email):
        EMAIL_ID = email
    if _check_valid_string(password):
        EMAIL_PASS = password


def send_emails(recipeints, message):
    global SMTP_GMAIL_URL, SMTP_GMAIL_PORT
    client = smtplib.SMTP(SMTP_GMAIL_URL, SMTP_GMAIL_PORT)
    client.starttls()
    # TODO: Check if valid credentials
    # TODO: Check if unsecure app access on
    client.login(EMAIL_ID, EMAIL_PASS)
    for recipient in recipeints:
        send_email(client, recipient, message)
    client.quit()


def send_email(client, recipient, message):
    if client is not None:
        client.sendmail(EMAIL_ID, recipient, message)

