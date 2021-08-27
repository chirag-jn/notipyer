from notipyer import __url__ as url


class RecipientNotPresentException(Exception):
    def __init__(self):
        message = 'No recipients found.'
        super().__init__(message)


class GmailLoginException(Exception):
    def __init__(self):
        message = "The App password doesn't work." \
                 f" Please refer README at {url}"
        super().__init__(message)


class SlackApiException(Exception):
    def __init__(self, e):
        message = "The Slack trigger for the bot failed" \
                 f" with the error: {e.response}"
        super().__init__(message)
