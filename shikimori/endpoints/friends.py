import logging

from .base import BaseEndpoint
from ..exceptions import RequestError


class FriendEndpoint(BaseEndpoint):
    async def add(self, id: int, access_token: str) -> str | RequestError:
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/friends/{id}",
            headers=self.auth_headers(access_token),
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logging.debug(
            f"Bad Request(add): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: int, access_token) -> str | RequestError:
        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/friends/{id}",
            headers=self.auth_headers(access_token),
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logging.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response
