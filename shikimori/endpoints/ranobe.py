import logging
from typing import List

from shikimori.types.animes import (
    Relation,
)
from shikimori.types.externalLink import ExternalLink
from shikimori.types.franchise import Franchise
from shikimori.types.ranobe import Ranobe, RanobeInfo
from shikimori.types.roles import Role
from shikimori.types.topics import Topic
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class RanobeEndpoint(BaseEndpoint):
    async def list(
        self,
        page: int = None,
        limit: int = None,
        order: str = None,
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
    ) -> List[Ranobe] | RequestError:
        """
        Most of parameters can be grouped in lists of values separated by comma:

        - season=2016,2015 – ranobe with season 2016 year or with season 2015 year

        Most of the parameters can be used in the subtraction mode:

        - season=!2016,!2015 – ranobe without season 2016 year and without season 2015 year

        Most of the parameters can be used in the combined mode:

        - season=2016,!summer_2016 – ranobe with season 2016 year and without season summer_2016.

        :param page: Must be a number between 1 and 100000.
        :param limit: 50 maximum.
        :param order: Must be one of: id, id_desc, ranked, kind, popularity, name, aired_on, volumes, chapters, status, random, ranked_random, ranked_shiki, created_at, created_at_desc.
        :param status: Must be one of: anons, ongoing, released, paused, discontinued.
        :param season: summer_2017 spring_2016,fall_2016.
        :param score: must be a number.
        :param genre: List of genre ids separated by comma.
        :param publisher: List of publisher ids separated by comma.
        :param franchise: List of franchises separated by comma.
        :param censored: Set to false to allow hentai, yaoi and yuri.
        :param mylist: Must be one of: planned, watching, rewatching, completed, on_hold, dropped.
        :param ids: List of ranobe ids separated by comma.
        :param exclude_ids: List of ranobe ids separated by comma.
        :param search: Must be a String.
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe",
            params=filter_none_parameters(
                {
                    "page": page,
                    "limit": limit,
                    "order": order,
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
                }
            ),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Ranobe.from_dict(ranobe) for ranobe in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> RanobeInfo | RequestError:
        """
        Show a ranobe.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return RanobeInfo.from_dict(response)

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
            url=f"{self._base_url}/api/ranobe/{id}/roles",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Role.from_dict(role) for role in response]

        logger.debug(
            f"Bad Request(roles): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def similar(self, id: int) -> List[Ranobe] | RequestError:
        """
        list similar.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/similar",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Ranobe.from_dict(ranobe) for ranobe in response]

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
            url=f"{self._base_url}/api/ranobe/{id}/related",
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
        list franchise.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/franchise",
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
            url=f"{self._base_url}/api/ranobe/{id}/external_links",
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
        list ExternalLinks.

        :param limit: 30 maximum.
        :param page: Must be a number between 1 and 100000.
        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/topics",
            headers=self.headers,
            params=filter_none_parameters({"page": page, "limit": limit}),
        )

        if not isinstance(response, RequestError):
            return [Topic.from_dict(topic) for topic in response]

        logger.debug(
            f"Bad Request(topics): status - {response.status_code}: info - {str(response)}"
        )

        return response
