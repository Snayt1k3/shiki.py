import logging

from shikimori.types.user_ignore import UserIgnore
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class UserIgnoreEndpoint(BaseEndpoint):
    async def ignore(self, user_id: str | int) -> UserIgnore | RequestError:
        """
        ignore user.

        Requires ignores oauth scope

        :param user_id: must be a number
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/users/{user_id}/ignore",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserIgnore.from_dict(response)

        logger.debug(
            f"Bad Request(ignore): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def unignore(self, user_id: str | int) -> UserIgnore | RequestError:
        """
        unignore user.

        Requires ignores oauth scope

        :param user_id: must be a number
        """

        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/v2/users/{user_id}/ignore",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserIgnore.from_dict(response)

        logger.debug(
            f"Bad Request(unignore): status - {response.status_code}: info - {str(response)}"
        )

        return response
