class RecipientNotPresentException(Exception):
    def __init__(self):
        message = 'No recipients found.'
        super().__init__(message)


class GmailLoginException(Exception):
    def __init__(self):
        message = 'Either less secure app access is turned off or the Email-Password combination is incorrect.'
        super().__init__(message)
