import logging
import time

from .exceptions import TooManyRequests
from .request import Request
from shikimori.base import BaseLimiter

logger = logging.getLogger(__name__)

__all__ = ["RequestLimiter"]


class RequestLimiter(BaseLimiter):
    """Limiter for requests"""

    def __init__(self, max_requests_sec: int, max_requests_min: int, request: Request):
        self._max_requests_sec = max_requests_sec
        self._max_requests_min = max_requests_min

        self._current_requests_sec = 0
        self._current_requests_min = 0

        self._request = request
        self._last_request_time_minute = time.time()
        self._last_request_time_second = time.time()

    def _is_limit_exceeded(self):
        current_time = time.time()

        if current_time - self._last_request_time_second >= 1:
            self._current_requests_sec = 0
            self._last_request_time_second = current_time

        if current_time - self._last_request_time_minute >= 60:
            self._current_requests_min = 0
            self._last_request_time_minute = current_time

        return (
            self._current_requests_sec > self._max_requests_sec
            or self._current_requests_min > self._max_requests_min
        )

    async def make_request(self, method: str, **kwargs):
        """
        :param method: one of [GET, POST, PATCH, DELETE]
        :param kwargs: parameters for request
        :return: response or 'RequestError' or Raise 'TooManyRequests'
        """
        if self._is_limit_exceeded():

            logger.error("RATE LIMIT EXCEEDED")
            raise TooManyRequests("Rate limit exceeded")

        self._current_requests_min += 1
        self._current_requests_sec += 1

        logger.info(f"{method} Request to url - {kwargs['url']}")

        return await self._request.make_request(method, **kwargs)
