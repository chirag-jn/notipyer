from credentials import *
from notipyer.email_notify import send_email, set_email_config

set_email_config(
    username, password, name, smtp_host="smtp-relay.gmail.com", smtp_port=587
)

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

print(target_email)

print(
    send_email(
        subject="my_subject",
        message="my_content",
        to_addr=[target_email],
        reply_to_addr="chiragjn120@gmail.com",
        attachment_path="credentials.py.sample",
        is_async=True,
        html_text=html,
    )
)
print("Email Sent")
