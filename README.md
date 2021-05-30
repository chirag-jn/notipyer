# Notipyer
##### Notification Triggers for Python
Send async email notifications via Python. Get updates/crashlogs from your scripts with ease. 

## Installation
```bash
python -m venv env
source env/bin/activate
pip install notipyer
```

## Email Notifications
Notipyer currently supports Gmail accounts as senders. To allow the library to use your gmail account, make the following changes:
1. Turn off 2-Step authentication. [Ref](https://support.google.com/accounts/answer/1064203)
2. Turn on "Less Secure App Access" [here](https://myaccount.google.com/intro/security)
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