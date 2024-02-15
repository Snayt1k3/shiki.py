
__all__ = ["TooManyRequests", "RequestError"]

class TooManyRequests(Exception):
    pass


class RequestError(Exception):
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code
