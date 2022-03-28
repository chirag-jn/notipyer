from credentials import *
from notipyer.email_notify import send_email, set_email_config

set_email_config(username, password, name)

html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
    </p>
  </body>
</html>
"""

print(send_email("my_subject", "my_content", [target_email], attachment_path='credentials.py.sample', is_async=True, html_text=html))
print('Email Sent')
