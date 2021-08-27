from notipyer.slack_notify import set_slack_token_config, send_message

SLACK_TOKEN = 'xoxb-12345678990123-1234567890123-abcdefghijklmnopqrstuvwx'

channel = 'my-channel-name'
message = 'my-message'

set_slack_token_config(SLACK_TOKEN)
send_message(channel, message)
