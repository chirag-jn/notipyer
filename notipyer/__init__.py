from .credential_handler import credentials

__version__ = '0.3.1'
__name__ = 'Notipyer'
__short_desc__ = 'Notification Triggers for Python'
__url__ = 'https://github.com/chirag-jn/notipyer'


creds = None


def _get_creds():
    global creds
    if creds is None:
        creds = credentials()
    return creds
