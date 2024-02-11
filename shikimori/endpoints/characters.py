import logging
from typing import List

from shikimori.types.general.photo import Photo
from shikimori.types.titles.character import Character, AnimeRole, MangaRole
from shikimori.types.titles.roles import Character as Ch
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class CharacterEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> List[Character] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/characters/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                Character(
                    **ch,
                    image=Photo(**ch["image"]),
                    seyu=[Ch(**s, image=Photo(**s["image"])) for s in ch["seyu"]],
                    animes=[
                        AnimeRole(**an, image=Photo(**an["image"]))
                        for an in ch["animes"]
                    ],
                    mangas=[
                        MangaRole(**mn, image=Photo(**mn["image"]))
                        for mn in ch["mangas"]
                    ],
                )
                for ch in response
            ]

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def search(self, search: str) -> list[Ch] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/characters/search",
            query_params={"search": search},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Ch(**ch, image=Photo(**ch["image"])) for ch in response]

        logger.debug(
            f"Bad Request(search): status - {response.status_code}: info - {str(response)}"
        )

        return response
