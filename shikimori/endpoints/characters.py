from .base import BaseEndpoint
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
from typing import List
from ..utils.filter import filter_none_parameters
from ..types.photo import Photo
from ..types.roles import Character as Seyu
from ..types.character import Character, AnimeRole, MangaRole


class CharacterEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def ById(self, id: int) -> List[Character] | RequestError:
        response = await self._request.make_request("GET", url=f"{self._base_url}/api/characters/{id}",
                                                    headers={"User-Agent": self._user_agent})

        if not isinstance(response, RequestError):
            return [
                Character(**ch, image=Photo(**ch["image"]),
                          seyu=[Seyu(**s, image=Photo(**s["image"])) for s in ch["seyu"]],
                          animes=[AnimeRole(**an, image=Photo(**an["image"])) for an in ch["animes"]],
                          mangas=[MangaRole(**mn, image=Photo(**mn["image"])) for mn in ch["mangas"]])
                for ch in response
            ]

        return response

