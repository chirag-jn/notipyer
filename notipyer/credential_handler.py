class credentials:
    EMAIL_ID = ''
    EMAIL_PASS = ''

    def __init__(self):
        pass


def _set_email_credentials(cred_obj, email, password):
    cred_obj.EMAIL_ID = email
    cred_obj.EMAIL_PASS = password
