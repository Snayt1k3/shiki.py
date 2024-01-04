import time
from .exceptions import TooManyRequests
from .request import Request


class RequestLimiter:
    """Limiter for requests"""
    def __init__(self, max_requests: int, interval: int, request: Request):
        self.max_requests = max_requests
        self.interval = interval
        self.current_requests = 0
        self.request = request
        self.last_request_time = time.time()

    def _reset(self):
        self.current_requests = 0
        self.last_request_time = time.time()

    def _is_limit_exceeded(self):
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time

        if time_since_last_request > self.interval:
            self._reset()

        return self.current_requests >= self.max_requests

    async def make_request(self, method: str, **kwargs):
        """
        :param method: one of [GET, POST, PUT, PATCH, DELETE]
        :param kwargs: parameters for request
        :return: response or Raise 'TooManyRequests'
        """
        if self._is_limit_exceeded():
            raise TooManyRequests("Rate limit exceeded")

        self.current_requests += 1
        self.last_request_time = time.time()

        return await self.request.make_request(method, **kwargs)
