import logging
import aiohttp
from .base import BaseRequest
from .exceptions import RequestError
from typing import Any

logger = logging.getLogger(__name__)

__all__ = ["Request"]


class Request(BaseRequest):
    """
    A class for sending HTTP requests.

    This class extends the functionality of the BaseRequest class
    to provide methods for sending various types of HTTP requests.
    """

    def __init__(self, token: str = None):
        self._token = token

    def set_token(self, token: str) -> None:
        self._token = token

    async def _request(
        self, method: str, headers: dict = None, **kwargs
    ) -> Any | RequestError:
        """
        Sends an HTTP request with the specified method.

        :param method: The HTTP method (e.g., 'GET', 'POST', 'DELETE').
        :param headers: A dictionary of HTTP headers to be included in the request. Defaults to None.
        :param **kwargs: Additional keyword arguments to be passed to the underlying request function.

        Returns:
            Union[Any, RequestError]: The response object corresponding to the HTTP request, or a RequestError if an error occurs.

        """
        try:
            if self._token:
                headers["Authorization"] = f"Bearer {self._token}"

            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.request(method, **kwargs) as response:
                    response.raise_for_status()
                    return await response.json()

        except aiohttp.ClientResponseError as exc:
            logger.debug(f"Error occurred with {method} request - {exc}")
            return RequestError(exc.message, exc.status)

    async def make_request(self, method: str, **kwargs):
        methods = ["GET", "POST", "PATCH", "DELETE"]

        if method not in methods:
            raise ValueError(f"Method {method} is not allowed")

        return await self._request(method, **kwargs)
