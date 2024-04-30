from abc import ABC

from shikimori.base import BaseLimiter


class BaseEndpoint(ABC):
    def __init__(self, base_url: str, request: BaseLimiter, user_agent: str):
        self._base_url = base_url
        self._request = request
        self._user_agent = user_agent

    @property
    def headers(self) -> dict:
        return {"User-Agent": self._user_agent}
