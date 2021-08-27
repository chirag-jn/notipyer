# Notipyer
#### Notification Triggers for Python
Send async email and slack notifications via Python. Get updates/crashlogs from your scripts with ease. 

## Installation
```bash
python -m venv env
source env/bin/activate
pip install notipyer
```

## Email Notifications
Notipyer currently supports Gmail accounts as senders. To allow the library to use your Gmail account, make the following changes:
   
1. Turn on 2-Step authentication. [Ref](https://support.google.com/accounts/answer/185839)
2. Create an app password. [Ref](https://support.google.com/mail/answer/185833)
3. While creating an app password, select app as "Other (Custom name)" and enter a name of your choice. 
4. Use the password obtained from app password for the configuration step below.
5. More information can be obtained on the wiki page [here](https://github.com/chirag-jn/notipyer/wiki/Notifications-via-Email)

### Configuration
```python
from notipyer.email_notify import set_email_config

SENDER_EMAIL = 'myemail@gmail.com'
SENDER_PASS = 'my_app_password'
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

## Slack Notifications
Notipyer currently supports running a single workplace install only. 
   
For setting up token keys for using slack notifications, follow the wiki page [here](https://github.com/chirag-jn/notipyer/wiki/Notifications-via-Slack)
   
### Configuration
```python
from notipyer.slack_notify import set_slack_token_config

# Follow the wiki for getting the bot token
BOT_TOKEN = 'xoxb-12345678990123-1234567890123-abcdefghijklmnopqrstuvwx' 
set_slack_token_config(BOT_TOKEN)
```
### Sending Message
```python
from notipyer.slack_notify import send_message

# the bot should be added to the channel
channel = 'my-channel-name'
message = 'my-message'

set_slack_token_config(SLACK_TOKEN)
send_message(channel, message)
```

## Contact
[Chirag Jain](https://github.com/chirag-jn)