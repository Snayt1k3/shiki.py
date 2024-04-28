import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from shikimori.types.genres import Genre

logger = logging.getLogger(__name__)


class GenreEndpoint(BaseEndpoint):
    async def list(self) -> list[Genre] | RequestError:
        response = await self._request.make_request(
            "GET", url=f"{self._base_url}/api/genres", headers=self.headers
        )

        if not isinstance(response, RequestError):
            return [Genre.from_dict(s) for s in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response
