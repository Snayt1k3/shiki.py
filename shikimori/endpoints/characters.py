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
            return Character(
                id=response["id"],
                altname=response["altname"],
                description=response["description"],
                description_html=response["description_html"],
                description_source=response["description_source"],
                favoured=response["favoured"],
                japanese=response["japanese"],
                name=response["name"],
                russian=response["russian"],
                thread_id=response["thread_id"],
                topic_id=response["topic_id"],
                updated_at=response["updated_at"],
                url=response["url"],
                image=Photo(**response["image"]),
                seyu=[
                    MiniCharacter(
                        image=Photo(**s["image"]),
                        id=s["id"],
                        name=s["name"],
                        russian=s["russian"],
                        url=s["url"],
                    )
                    for s in response["seyu"]
                ],
                animes=[
                    AnimeRole(
                        id=an["id"],
                        name=an["name"],
                        russian=an["russian"],
                        image=Photo(**an["image"]),
                        url=an["url"],
                        kind=an["kind"],
                        score=an["score"],
                        status=an["status"],
                        episodes=an["episodes"],
                        episodes_aired=an["episodes_aired"],
                        aired_on=an["aired_on"],
                        released_on=an["released_on"],
                        role=an["role"],
                        roles=an["roles"],
                    )
                    for an in response["animes"]
                ],
                mangas=[
                    MangaRole(
                        id=mn["id"],
                        name=mn["name"],
                        russian=mn["russian"],
                        image=Photo(**mn["image"]),
                        url=mn["url"],
                        kind=mn["kind"],
                        score=mn["score"],
                        status=mn["status"],
                        chapters=mn["chapters"],
                        volumes=mn["volumes"],
                        aired_on=mn["aired_on"],
                        released_on=mn["released_on"],
                        role=mn["role"],
                        roles=mn["roles"],
                    )
                    for mn in response["mangas"]
                ],
            )

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def search(self, search: str) -> list[MiniCharacter] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/characters/search",
            query_params={"search": search},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                MiniCharacter(
                    image=Photo(**s["image"]),
                    id=s["id"],
                    name=s["name"],
                    russian=s["russian"],
                    url=s["url"],
                )
                for s in response
            ]

        logger.debug(
            f"Bad Request(search): status - {response.status_code}: info - {str(response)}"
        )

        return response
