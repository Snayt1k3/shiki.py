import logging
from ..types.general.topics import Forum
from .base import BaseEndpoint
from ..exceptions import RequestError


class FavoritesEndpoint(BaseEndpoint):
    async def list(self) -> RequestError | list[Forum]:
        response = await self._request.make_request(
            "GET", url=f"{self._base_url}/api/forums", headers=self._headers()
        )

        if not isinstance(response, RequestError):
            return [Forum(**s) for s in response]

        logging.debug(
            f"Bad Request(add): status - {response.status_code}: info - {str(response)}"
        )

        return response
