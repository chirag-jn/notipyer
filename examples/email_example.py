from notipyer.email_notify import set_email_config, send_email

SENDER_EMAIL = 'myemail@gmail.com'
SENDER_PASS = 'password'
set_email_config(SENDER_EMAIL, SENDER_PASS)

subject = 'My Email Subject'
body = 'My Email Body'
to_recipients = ['to-email-1@domain.com', 'toemail2@domain.com']
cc_recipients = ['cc-email-1@domain.com', 'cc-email-2@domain.com']
bcc_recipients = ['bcc-email-1@domain.com', 'bcc-email-2@domain.com']

send_email(subject=subject,
           message=body,
           to_addr=to_recipients,
           cc_addr=cc_recipients,
           bcc_addr=bcc_recipients)
