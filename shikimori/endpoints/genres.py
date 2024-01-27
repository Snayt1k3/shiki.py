import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.titles.genres import Genre


class GenreEndpoint(BaseEndpoint):
    async def list(self) -> list[Genre] | RequestError:
        response = await self._request.make_request(
            "GET", url=f"{self._base_url}/api/genres", headers=self._headers()
        )

        if not isinstance(response, RequestError):
            return [Genre(**s) for s in response]

        logging.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response
