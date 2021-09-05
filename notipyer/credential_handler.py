class credentials:
    EMAIL_ID = ''
    EMAIL_PASS = ''
    EMAIL_USER = ''
    SLACK_TOKEN = ''

    def __init__(self):
        pass


def _set_email_credentials(cred_obj, email, password, name):
    cred_obj.EMAIL_ID = email
    cred_obj.EMAIL_PASS = password
    cred_obj.EMAIL_USER = name


def _set_slack_token_credentials(cred_obj, token):
    cred_obj.SLACK_TOKEN = token
