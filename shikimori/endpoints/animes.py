import logging
from typing import List

from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.topics import Topic, Forum, Linked
from shikimori.types.animes import (
    Anime,
    AnimeInfo,
    GenreExtended,
    Relation,
    ExternalLink,
)
from shikimori.types.franchise import Franchise, Node, Link
from shikimori.types.manga import Manga
from shikimori.types.roles import Role, Character
from shikimori.types.screenshots import ScreenShot
from shikimori.types.studios import Studio
from shikimori.types.videos import Video
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.user import User
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class AnimeEndpoint(BaseEndpoint):
    async def list(
        self,
        page: int = None,
        limit: int = None,
        order: str = None,
        kind: str = None,
        status: str = None,
        season: str = None,
        score: str = None,
        duration: str = None,
        rating: str = None,
        genre: str = None,
        studio: str = None,
        franchise: str = None,
        censored: str = None,
        mylist: str = None,
        ids: str = None,
        exclude_ids: str = None,
        search: str = None,
    ) -> list[Anime] | RequestError:
        """
        :param page: must be a number between 1 and 100000.
        :param limit: Must be a number. 50 - maximum
        :param order: Must be one of: id, id_desc, ranked, kind, popularity, name, aired_on, episodes, status, random, ranked_random, ranked_shiki, created_at, created_at_desc.
        :param kind: Must be one of: tv, movie, ova, ona, special, tv_special, music, pv, cm, tv_13, tv_24, tv_48
        :param status: Must be one of: anons, ongoing, released
        :param season: ex - summer_2017, 2016, 2014_2016, 199x
        :param score: Must be a number.
        :param duration: Must be one of: S - less than 10, D - less than 30, F - more than 30
        :param rating: Must be one of: none, g, pg, pg_13, r, r_plus, rx
        :param genre: List of genre ids separated by comma
        :param studio: List of studio ids separated by comma
        :param franchise: List of franchises separated by comma
        :param censored: Must be one of: true, false.
        :param mylist: Must be one of: planned, watching, rewatching, completed, on_hold, dropped
        :param ids: List of anime ids separated by comma
        :param exclude_ids: List of anime ids separated by comma
        :param search: Search phrase to filter animes by name
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes",
            query_params=filter_none_parameters(
                {
                    "page": page,
                    "limit": limit,
                    "order": order,
                    "kind": kind,
                    "status": status,
                    "season": season,
                    "studio": studio,
                    "score": score,
                    "duration": duration,
                    "rating": rating,
                    "genre": genre,
                    "franchise": franchise,
                    "censored": censored,
                    "mylist": mylist,
                    "ids": ids,
                    "exclude_ids": exclude_ids,
                    "search": search,
                }
            ),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                Anime(**anime, image=Photo(**anime.get("image"))) for anime in response
            ]

        logger.debug(
            f"Bad Request(anime_list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def byId(self, id: int) -> AnimeInfo | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return AnimeInfo(
                **response,
                genres=[GenreExtended(**genre) for genre in response.get("genres")],
                screenshots=[ScreenShot(**s) for s in response.get("screenshots")],
                studios=[Studio(**s) for s in response.get("studios")],
                videos=[Video(**v) for v in response.get("videos")],
            )

        logger.debug(
            f"Bad Request(byId): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def roles(self, id: int) -> List[Role] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/roles",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                Role(
                    **role,
                    character=Character(
                        **role.get("character"),
                        image=Photo(**role["character"]["image"]),
                    ),
                )
                for role in response
            ]

        logger.debug(
            f"Bad Request(roles): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def similar(self, id: int) -> List[Anime] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/similar",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                Anime(**anime, image=Photo(**anime.get("image"))) for anime in response
            ]

        logger.debug(
            f"Bad Request(similar): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def related(self, id: int) -> List[Relation] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/related",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                Relation(
                    **relation,
                    anime=Anime(
                        **relation.get("anime"),
                        image=Photo(**relation["anime"]["image"])
                        if relation.get("anime")
                        else None,
                    ),
                    manga=Manga(
                        **relation.get("manga"),
                        image=Photo(**relation["anime"]["image"])
                        if relation.get("manga")
                        else None,
                    ),
                )
                for relation in response
            ]

        logger.debug(
            f"Bad Request(related): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def screenshots(self, id: int) -> List[ScreenShot] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/screenshots",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [ScreenShot(**s) for s in response]

        logger.debug(
            f"Bad Request(related): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def franchise(self, id: int) -> Franchise | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/franchise",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Franchise(
                nodes=[Node(**node) for node in response.get("nodes")],
                links=[Link(**link) for link in response.get("links")],
            )

        logger.debug(
            f"Bad Request(franchise): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def externalLinks(self, id: int) -> List[ExternalLink] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/external_links",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [ExternalLink(**s) for s in response]

        logger.debug(
            f"Bad Request(externalLinks): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def topics(
        self,
        id: int,
        page: int = None,
        limit: int = None,
        kind: str = None,
        episode: int = None,
    ) -> List[Topic] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/topics",
            headers=self.headers,
            query_params=filter_none_parameters(
                {"page": page, "limit": limit, "kind": kind, "episode": episode}
            ),
        )

        if not isinstance(response, RequestError):
            return [
                Topic(
                    **topic,
                    forum=Forum(**topic.get("forum")),
                    user=User(
                        **topic.get("user"),
                        image=PhotoExtended(**topic["user"]["image"]),
                    ),
                    linked=Linked(
                        **topic["linked"], image=Photo(**topic["linked"]["image"])
                    ),
                )
                for topic in response
            ]

        return response
