# Notipyer
Notification triggers for Python

## Installation
```bash
python -m venv env
source env/bin/activate
pip install notipyer
```

## Email Notifications
Currently supports Gmail accounts as senders. 
### Configuration
```python
from notipyer.email_notify import set_email_config

SENDER_EMAIL = 'myemail@gmail.com'
SENDER_PASS = 'password'
set_email_config(SENDER_EMAIL, SENDER_PASS)
```
### Sending Email
```python
from notipyer.email_notify import send_email

subject = 'My Email Subject'
body = 'My Email Body'
to_recipients = ['to-email-1@domain.com', 'toemail2@domain.com'] # Can be None
cc_recipients = ['cc-email-1@domain.com', 'cc-email-2@domain.com'] # Can be None
bcc_recipients = ['bcc-email-1@domain.com', 'bcc-email-2@domain.com'] # Can be None

send_email(subject, body, to_recipients, cc_recipients, bcc_recipients)
```

## Contact
[Chirag Jain](https://github.com/chirag-jn)