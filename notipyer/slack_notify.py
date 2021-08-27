from .credential_handler import _set_slack_token_credentials
from .utils.async_decorator import Async
from slack import WebClient
from notipyer import _get_creds

slack_creds = _get_creds()
slack_client = None


def set_slack_token_config(slack_token):
    global slack_creds
    _set_slack_token_credentials(slack_creds, slack_token)


def _get_slack_client():
    global slack_creds, slack_client
    if slack_client is None:
        slack_client = WebClient(token=slack_creds.SLACK_TOKEN)
    return slack_client


@Async
def send_message(channel, text):
    _get_slack_client().chat_postMessage(
        channel=channel,
        text=text
    )
