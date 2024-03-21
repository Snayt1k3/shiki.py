from abc import ABC, abstractmethod
from shikimori import RequestError


class BaseRequest(ABC):
    """
    Base class for request
    """

    @abstractmethod
    async def make_request(self, method: str, headers: dict = None, **kwargs) -> RequestError | any:
        """
        :param method: one of [get, post, patch, delete]
        :param headers: headers of request
        :param kwargs: other parameters
        """
        raise NotImplementedError

class BaseLimiter(ABC):
    """
    Interface for request limiter
    """

    @abstractmethod
    async def make_request(self, method: str, **kwargs) -> RequestError | any:
        """
        :param method: one of [get, post, patch, delete]
        :param kwargs: other parameters
        """
        raise NotImplementedError
