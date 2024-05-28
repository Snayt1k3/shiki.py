__all__ = ["TooManyRequests", "RequestError"]


class TooManyRequests(Exception):
    """
    is a custom exception class used to represent the HTTP status code 429,
    which indicates that the client has sent too many requests in a given amount of time.
    """

    pass


class RequestError(Exception):
    """
    Custom exception class for handling errors that occur during HTTP requests.

    :param message: A string describing the error.
    :param status_code: (int, optional): The HTTP status code associated with the error. Defaults to None.
    """

    def __init__(self, message, status_code=None):
        """
        Initializes a new instance of the RequestError class.

        :param message: A string describing the error.
        :param status_code: (int, optional): The HTTP status code associated with the error. Defaults to None.
        """
        super().__init__(message)
        self.status_code = status_code
