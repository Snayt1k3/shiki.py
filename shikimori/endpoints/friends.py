import logging

from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class FriendEndpoint(BaseEndpoint):
    async def add(self, id: int) -> str | RequestError:
        """
        Create a friend.

        Requires friends oauth scope.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/friends/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logger.debug(
            f"Bad Request(add): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: int) -> str | RequestError:
        """
        Destroy a friend.

        Requires friends oauth scope.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/friends/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logger.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response
