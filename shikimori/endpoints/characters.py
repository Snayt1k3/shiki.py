import logging

from shikimori.types.character import Character, CharacterBrief
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class CharacterEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> Character | RequestError:
        """
        Show a character.

        :param id: must be a number.
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/characters/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Character.from_dict(response)

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def search(self, search: str) -> list[CharacterBrief] | RequestError:
        """
        Search characters.

        :param search: Must be a String.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/characters/search",
            params={"search": search},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [CharacterBrief.from_dict(ch) for ch in response]

        logger.debug(
            f"Bad Request(search): status - {response.status_code}: info - {str(response)}"
        )

        return response
