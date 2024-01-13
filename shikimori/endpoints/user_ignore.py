from .base import BaseEndpoint
from ..types.user_ignore import UserIgnore
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter


class UserIgnoreEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def ignore(
        self, user_id: str | int, access_token: str
    ) -> UserIgnore | RequestError:
        """
        ignore user.

        Requires oauth scope
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/users/{user_id}/ignore",
            headers={
                "User-Agent": self._user_agent,
                "Authorization": f"Bearer {access_token}",
            },
        )

        if not isinstance(response, RequestError):
            return UserIgnore(**response)

        return response

    async def unignore(
        self, user_id: str | int, access_token: str
    ) -> UserIgnore | RequestError:
        """
        unignore user

        Requires oauth scope
        """

        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/v2/users/{user_id}/ignore",
            headers={
                "User-Agent": self._user_agent,
                "Authorization": f"Bearer {access_token}",
            },
        )

        if not isinstance(response, RequestError):
            return UserIgnore(**response)

        return response
