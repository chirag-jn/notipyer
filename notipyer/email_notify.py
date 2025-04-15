from .credential_handler import _set_email_credentials, _set_smtp_credentials
from .errors import GmailLoginException, RecipientNotPresentException
from .async_decorator import Async
from notipyer import _get_creds
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os

mail_cred = _get_creds()


def _check_valid_string(string):
    if len(string) > 0:
        return True
    return False


def set_email_config(email, password, sender_name="", smtp_host=None, smtp_port=None):
    global mail_cred
    if _check_valid_string(email) and _check_valid_string(password):
        _set_email_credentials(mail_cred, email, password, sender_name)
    _set_smtp_credentials(
        mail_cred,
        host=smtp_host if smtp_host else "smtp.gmail.com",
        port=smtp_port if smtp_port else 587,
    )


def _send_email_helper(
    subject,
    message,
    to_addr=None,
    reply_to_addr=None,
    cc_addr=None,
    bcc_addr=None,
    attachment_path=None,
    html_text=None,
):
    global mail_cred

    to_addr, cc_addr, bcc_addr = _check_recipients(to_addr, cc_addr, bcc_addr)

    client = smtplib.SMTP(
        mail_cred.EMAIL_SMTP_HOST, mail_cred.EMAIL_SMTP_PORT, timeout=10
    )
    client.ehlo()
    client.starttls()
    client.ehlo()

    client = _login_client(client)

    recipients, email_body = _build_email(
        subject,
        message,
        to_addr,
        reply_to_addr,
        cc_addr,
        bcc_addr,
        attachment_path,
        html_text=html_text,
    )
    client.sendmail(mail_cred.EMAIL_ID, recipients, email_body)
    client.quit()
    return True


def send_email(
    subject,
    message,
    to_addr=None,
    reply_to_addr=None,
    cc_addr=None,
    bcc_addr=None,
    attachment_path=None,
    html_text=None,
    is_async=True,
):
    global _send_email_helper
    if is_async:
        _send_email_helper = Async(_send_email_helper)

    return _send_email_helper(
        subject,
        message,
        to_addr,
        reply_to_addr,
        cc_addr,
        bcc_addr,
        attachment_path,
        html_text,
    )


def _login_client(client):
    try:
        client.login(mail_cred.EMAIL_ID, mail_cred.EMAIL_PASS)
        return client
    except smtplib.SMTPAuthenticationError:
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


def _build_email(
    subject,
    text,
    to_emails,
    reply_to_email,
    cc_emails,
    bcc_emails,
    attachment_path,
    html_text,
):
    global mail_cred
    if len(mail_cred.EMAIL_USER) > 0:
        sender = mail_cred.EMAIL_USER + " <" + mail_cred.EMAIL_ID + ">"
    else:
        sender = mail_cred.EMAIL_ID
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ",".join(to_emails)
    message["CC"] = ",".join(cc_emails)
    message["Subject"] = subject

    if reply_to_email:
        message.add_header("Reply-To", reply_to_email)

    if text is not None:
        message.attach(MIMEText(text, "plain"))
    if html_text is not None:
        message.attach(MIMEText(html_text, "html"))

    if attachment_path is not None:
        attachment = open(attachment_path, "rb")
        filename = os.path.basename(attachment_path)
        p = MIMEBase("application", "octet-stream")
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header("Content-Disposition", "attachment; filename=%s" % filename)
        message.attach(p)

    toaddrs = to_emails + cc_emails + bcc_emails
    return toaddrs, message.as_string()
