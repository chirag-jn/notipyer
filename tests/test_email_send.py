from credentials import *
from notipyer.email_notify import send_email, set_email_config

set_email_config(username, password, name)

send_email("my_subject", "my_content", [target_email])