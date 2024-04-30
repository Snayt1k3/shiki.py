import logging
import aiohttp
from .base import BaseRequest
from .exceptions import RequestError

logger = logging.getLogger(__name__)

__all__ = ["Request"]


class Request(BaseRequest):
    """class for send requests"""

    def __init__(self, token: str = None):
        self._token = token

    def set_token(self, token: str) -> None:
        self._token = token

    async def _request(self, method: str, headers: dict = None, **kwargs):
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
