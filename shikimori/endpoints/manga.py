import logging
from typing import List

from shikimori.types.animes import (
    Relation,
)
from shikimori.types.externalLink import ExternalLink
from shikimori.types.franchise import Franchise
from shikimori.types.manga import Manga, MangaInfo
from shikimori.types.roles import Role
from shikimori.types.topics import Topic
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class MangaEndpoint(BaseEndpoint):
    async def list(
        self,
        page: int = None,
        limit: int = None,
        order: str = None,
        kind: str = None,
        status: str = None,
        season: str = None,
        score: int = None,
        genre: str = None,
        publisher: str = None,
        franchise: str = None,
        censored: bool = None,
        mylist: str = None,
        ids: str = None,
        exclude_ids: str = None,
        search: str = None,
        genre_v2: str = None,
    ):
        """
        Most of parameters can be grouped in lists of values separated by comma:

        - season=2016,2015 – mangas with season 2016 year or with season 2015 year.

        - kind=manga,one_shot – mangas with kind Manga or with kind One Shot.

        Most of the parameters can be used in the subtraction mode:

        - season=!2016,!2015 – mangas without season 2016 year and without season 2015 year.

        - kind=!manga,!one_shot – mangas without kind Manga and without kind One Shot.

        Most of the parameters can be used in the combined mode:

        - season=2016,!summer_2016 – mangas with season 2016 year and without season summer_2016.

        :param page: Must be a number between 1 and 100000.
        :param limit: 50 maximum.
        :param order: Must be one of: id, id_desc, ranked, kind, popularity, name, aired_on, volumes, chapters, status, random, ranked_random, ranked_shiki, created_at, created_at_desc.
        :param kind: Must be one of: manga, manhwa, manhua, light_novel, novel, one_shot, doujin.
        :param status: Must be one of: anons, ongoing, released, paused, discontinued.
        :param season: summer_2017 spring_2016,fall_2016.
        :param score: must be a number.
        :param genre: List of genre ids separated by comma.
        :param publisher: List of publisher ids separated by comma.
        :param franchise: List of franchises separated by comma.
        :param censored: Set to false to allow hentai, yaoi and yuri.
        :param mylist: Must be one of: planned, watching, rewatching, completed, on_hold, dropped.
        :param ids: List of manga ids separated by comma
        :param exclude_ids: List of manga ids separated by comma
        :param search: Must be a String
        :param genre_v2: List of genre v2 ids separated by comma
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas",
            params=filter_none_parameters(
                {
                    "page": page,
                    "limit": limit,
                    "order": order,
                    "kind": kind,
                    "status": status,
                    "season": season,
                    "score": score,
                    "genre": genre,
                    "publisher": publisher,
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
            return [Manga.from_dict(manga) for manga in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> MangaInfo | RequestError:
        """
        Show a manga.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return MangaInfo.from_dict(response)

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def roles(self, id: int) -> List[Role] | RequestError:
        """
        list roles.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas/{id}/roles",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Role.from_dict(role) for role in response]

        logger.debug(
            f"Bad Request(roles): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def similar(self, id: int) -> List[Manga] | RequestError:
        """
        list similar.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas/{id}/similar",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Manga.from_dict(manga) for manga in response]

        logger.debug(
            f"Bad Request(similar): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def related(self, id: int) -> List[Relation] | RequestError:
        """
        list related.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas/{id}/related",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Relation.from_dict(relation) for relation in response]

        logger.debug(
            f"Bad Request(related): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def franchise(self, id: int) -> Franchise | RequestError:
        """
        list franchises.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas/{id}/franchise",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Franchise.from_dict(response)

        logger.debug(
            f"Bad Request(franchise): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ExternalLinks(self, id: int) -> List[ExternalLink] | RequestError:
        """
        list ExternalLinks.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas/{id}/external_links",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [ExternalLink.from_dict(link) for link in response]

        logger.debug(
            f"Bad Request(externalLinks): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def topics(
        self,
        id: int,
        page: int = None,
        limit: int = None,
    ) -> List[Topic] | RequestError:
        """
        list topics.

        :param id: must be a number
        :param page: Must be a number between 1 and 100000.
        :param limit: 30 maximum
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas/{id}/topics",
            headers=self.headers,
            params=filter_none_parameters({"page": page, "limit": limit}),
        )

        if not isinstance(response, RequestError):
            return [Topic.from_dict(topic) for topic in response]

        return response
