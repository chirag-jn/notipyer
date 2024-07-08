# Notipyer: Notification Triggers for Python

[![PyPI](https://img.shields.io/pypi/v/notipyer)](https://pypi.org/project/notipyer/)
[![License: AGPL v3](https://img.shields.io/github/license/chirag-jn/notipyer)](https://www.gnu.org/licenses/agpl-3.0)

Notipyer is a versatile Python library for sending asynchronous email and Slack notifications, ensuring you receive updates and crash logs from your scripts effortlessly.

## Table of Contents
- [Installation](#installation)
- [Email Notifications](#email-notifications)
  - [Configuration](#configuration)
  - [Sending Email](#sending-email)
- [Slack Notifications](#slack-notifications)
  - [Configuration](#configuration-1)
  - [Sending Message](#sending-message)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To install Notipyer, use the following commands:

```bash
python -m venv env
source env/bin/activate
pip install notipyer
```

## Email Notifications

### Configuration

Before sending email notifications, configure your Gmail account:

1. **Turn on 2-Step authentication**: Follow the instructions [here](https://support.google.com/accounts/answer/185839).
2. **Create an app password**: Follow the steps [here](https://support.google.com/accounts/answer/185833).

Use the app password in your configuration:

```python
from notipyer.email_notify import set_email_config

SENDER_EMAIL = 'myemail@gmail.com'
SENDER_PASS = 'my_app_password'
SENDER_NAME = 'my name'
set_email_config(SENDER_EMAIL, SENDER_PASS, SENDER_NAME)
```

### Sending Email

Send an email using the configured settings:

```python
from notipyer.email_notify import send_email

subject = 'My Email Subject'
body = 'My Email Body'
reply_to_recipient = 'reply-to-email@domain.com' # Can be None
to_recipients = ['to-email-1@domain.com', 'toemail2@domain.com'] # Can be None
cc_recipients = ['cc-email-1@domain.com', 'cc-email-2@domain.com'] # Can be None
bcc_recipients = ['bcc-email-1@domain.com', 'bcc-email-2@domain.com'] # Can be None
attachment_path = 'path_to_my_file' # Can be None
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
    </p>
  </body>
</html>
""" # Can be None
is_async = True # Sent as an async email only if this parameter is True

send_email(subject, body, to_recipients, reply_to_recipient, cc_recipients, bcc_recipients, attachment_path, html_text, is_async)
```

## Slack Notifications

### Configuration

Set up your Slack bot token:

```python
from notipyer.slack_notify import set_slack_token_config

# Follow the wiki for getting the bot token
BOT_TOKEN = 'xoxb-12345678990123-1234567890123-abcdefghijklmnopqrstuvwx' 
set_slack_token_config(BOT_TOKEN)
```

### Sending Message

Send a message to a Slack channel:

```python
from notipyer.slack_notify import send_message

# the bot should be added to the channel
channel = 'my-channel-name'
message = 'my-message'

set_slack_token_config(SLACK_TOKEN)
send_message(channel, message)
```

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [Chirag Jain](https://github.com/chirag-jn).