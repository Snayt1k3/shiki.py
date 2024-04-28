import logging

from shikimori.types.character import Character, AnimeRole, MangaRole
from shikimori.types.photo import Photo
from shikimori.types.roles import Character as MiniCharacter
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class CharacterEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> Character | RequestError:
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

    async def search(self, search: str) -> list[MiniCharacter] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/characters/search",
            params={"search": search},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [MiniCharacter.from_dict(ch) for ch in response]

        logger.debug(
            f"Bad Request(search): status - {response.status_code}: info - {str(response)}"
        )

        return response
