import logging

from .base import BaseEndpoint
from shikimori.types.user.user_ignore import UserIgnore
from ..exceptions import RequestError


class UserIgnoreEndpoint(BaseEndpoint):
    async def ignore(self, user_id: str | int) -> UserIgnore | RequestError:
        """
        ignore user.

        Requires oauth scope
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/users/{user_id}/ignore",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserIgnore(**response)

        logging.debug(
            f"Bad Request(ignore): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def unignore(self, user_id: str | int) -> UserIgnore | RequestError:
        """
        unignore user

        Requires oauth scope
        """

        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/v2/users/{user_id}/ignore",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserIgnore(**response)

        logging.debug(
            f"Bad Request(unignore): status - {response.status_code}: info - {str(response)}"
        )

        return response
