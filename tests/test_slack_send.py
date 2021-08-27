from credentials import *

from notipyer.slack_notify import set_slack_token_config, send_message

set_slack_token_config(slack_token)
send_message("random", "my message")
