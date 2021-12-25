from .credential_handler import _set_slack_token_credentials
from .async_decorator import Async
from .errors import SlackApiException
from slack import WebClient
from slack.errors import SlackApiError
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
    try:
        _get_slack_client().chat_postMessage(
            channel=channel,
            text=text
        )
    except SlackApiError as e:
        raise SlackApiException(e)
