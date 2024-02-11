import asyncio
import logging
import time

from .exceptions import TooManyRequests
from .request import Request

logger = logging.getLogger(__name__)


class RequestLimiter:
    """Limiter for requests"""

    def __init__(self, max_requests: int, interval: int, request: Request, REQUEST_WAITING: bool):
        self._max_requests = max_requests
        self._request_waiting = REQUEST_WAITING
        self._interval = interval
        self._current_requests = 0
        self._request = request
        self._last_request_time = time.time()

    def _reset(self):
        self._current_requests = 0
        self._last_request_time = time.time()

    def _is_limit_exceeded(self):
        current_time = time.time()
        time_since_last_request = current_time - self._last_request_time

        if time_since_last_request > self._interval:
            self._reset()

        return self._current_requests >= self._max_requests

    async def make_request(self, method: str, **kwargs):
        """
        :param method: one of [GET, POST, PUT, PATCH, DELETE]
        :param kwargs: parameters for request
        :return: response or 'RequestError' or Raise 'TooManyRequests'
        """
        if self._is_limit_exceeded():

            await asyncio.sleep(self._interval)

            if not self._request_waiting:
                logger.error("RATE LIMIT EXCEEDED")
                raise TooManyRequests("Rate limit exceeded")

        self._current_requests += 1
        self._last_request_time = time.time()

        logger.info(f"{method} Request to url - {kwargs['url']}")

        return await self._request.make_request(method, **kwargs)
