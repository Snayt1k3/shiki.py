import logging
from typing import List

from shikimori.types.animes import (
    Anime,
    AnimeInfo,
    Relation,
)
from shikimori.types.externalLink import ExternalLink
from shikimori.types.franchise import Franchise
from shikimori.types.roles import Role
from shikimori.types.screenshots import ScreenShot
from shikimori.types.topics import Topic
from .base import BaseEndpoint
from ..exceptions import RequestError
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
        genre_v2: str = None,
    ) -> list[Anime] | RequestError:
        """
        List animes.

        :param page: must be a number between 1 and 100000.
        :param limit: Must be a number, 50 - maximum.
        :param order: Must be one of: id, id_desc, ranked, kind, popularity, name, aired_on, episodes, status, random, ranked_random, ranked_shiki, created_at, created_at_desc.
        :param kind: Must be one of: tv, movie, ova, ona, special, tv_special, music, pv, cm, tv_13, tv_24, tv_48.
        :param status: Must be one of: anons, ongoing, released.
        :param season: ex - summer_2017, 2016, 2014_2016, 199x.
        :param score: Must be a number.
        :param duration: Must be one of: S - less than 10, D - less than 30, F - more than 30.
        :param rating: Must be one of: none, g, pg, pg_13, r, r_plus, rx.
        :param genre: List of genre ids separated by comma.
        :param studio: List of studio ids separated by comma.
        :param franchise: List of franchises separated by comma.
        :param censored: Must be one of: true, false.
        :param mylist: Must be one of: planned, watching, rewatching, completed, on_hold, dropped.
        :param ids: List of anime ids separated by comma.
        :param exclude_ids: List of anime ids separated by comma.
        :param search: Search phrase to filter animes by name.
        :param genre_v2: List of genre v2 ids separated by comma.
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes",
            params=filter_none_parameters(
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
                    "genre_v2": genre_v2,
                }
            ),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Anime.from_dict(anime) for anime in response]

        logger.debug(
            f"Bad Request(anime_list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> AnimeInfo | RequestError:
        """
        Show an anime.

        :param id: Must be a Number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return AnimeInfo.from_dict(response)

        logger.debug(
            f"Bad Request(byId): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def roles(self, id: int) -> List[Role] | RequestError:
        """
        List anime roles.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/roles",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Role.from_dict(role) for role in response]

        logger.debug(
            f"Bad Request(roles): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def similar(self, id: int) -> List[Anime] | RequestError:
        """
        List similar animes.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/similar",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Anime.from_dict(anime) for anime in response]

        logger.debug(
            f"Bad Request(similar): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def related(self, id: int) -> List[Relation] | RequestError:
        """
        List related animes.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/related",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Relation.from_dict(relation) for relation in response]

        logger.debug(
            f"Bad Request(related): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def screenshots(self, id: int) -> List[ScreenShot] | RequestError:
        """
        List screenshots anime.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/screenshots",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [ScreenShot.from_dict(s) for s in response]

        logger.debug(
            f"Bad Request(related): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def franchise(self, id: int) -> Franchise | RequestError:
        """
        Show the whole franchise.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/franchise",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Franchise.from_dict(response)

        logger.debug(
            f"Bad Request(franchise): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def externalLinks(self, id: int) -> List[ExternalLink] | RequestError:
        """
        Show the externalLinks of an anime.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/external_links",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [ExternalLink.from_dict(s) for s in response]

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
        """
        list of topics that relate to anime.

        :param id: Must be a number.
        :param page: Must be a number between 1 and 100000.
        :param limit: 30 maximum.
        :param kind: Must be one of: anons, ongoing, released, episode.
        :param episode: Must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/topics",
            headers=self.headers,
            params=filter_none_parameters(
                {"page": page, "limit": limit, "kind": kind, "episode": episode}
            ),
        )

        if not isinstance(response, RequestError):
            return [Topic.from_dict(topic) for topic in response]

        return response
