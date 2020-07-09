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


class RailsApiError(TPMainException):
    def __init__(self, message):
        TPMainException.__init__(self, "Bad Rails response with message: " + message)


class PhpApiError(TPMainException):
    def __init__(self, message):
        TPMainException.__init__(self, "Bad Php response with message: " + message)
