class TPMainException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


class NotFound(TPMainException):
    def __init__(self, message):
        TPMainException.__init__(self, message)


class InvalidParameter(TPMainException):
    def __init__(self, message):
        TPMainException.__init__(self, message)
