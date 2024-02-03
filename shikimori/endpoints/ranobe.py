import logging
from typing import List

from .base import BaseEndpoint
from ..utils.filter import filter_none_parameters
from ..exceptions import RequestError
from ..types.titles.ranobe import Ranobe, RanobeInfo
from ..types.titles.manga import Manga
from ..types.general.photo import Photo, PhotoExtended
from ..types.titles.genres import Genre
from ..types.titles.roles import Role, Character
from shikimori.types.titles.franchise import Franchise, Node, Link
from shikimori.types.general.topics import Topic, Forum, Linked
from ..types.user.user import User
from shikimori.types.titles.animes import (
    Anime,
    Relation,
    ExternalLink,
)


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

        - season=2016,!summer_2016 – ranobe with season 2016 year and without season summer_2016
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
        :param ids: List of ranobe ids separated by comma
        :param exclude_ids: List of ranobe ids separated by comma
        :param search: Must be a String
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe",
            query_params=filter_none_parameters(
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
            return [Ranobe(**s, image=Photo(**s["image"])) for s in response]

        logging.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> List[RanobeInfo] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}api/ranobe/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                RanobeInfo(
                    **s,
                    image=Photo(**s["image"]),
                    genres=[Genre(**g["genres"]) for g in s["genres"]],
                )
                for s in response
            ]

    async def roles(self, id: int) -> List[Role] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/roles",
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

        logging.debug(
            f"Bad Request(roles): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def similar(self, id: int) -> List[Ranobe] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/similar",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Ranobe(**s, image=Photo(**s["image"])) for s in response]

        logging.debug(
            f"Bad Request(similar): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def related(self, id: int) -> List[Relation] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/related",
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

        logging.debug(
            f"Bad Request(related): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def franchise(self, id: int) -> Franchise | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/franchise",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Franchise(
                nodes=[Node(**node) for node in response.get("nodes")],
                links=[Link(**link) for link in response.get("links")],
            )

        logging.debug(
            f"Bad Request(franchise): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ExternalLinks(self, id: int) -> List[ExternalLink] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/external_links",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [ExternalLink(**s) for s in response]

        logging.debug(
            f"Bad Request(externalLinks): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def topics(
        self,
        id: int,
        page: int = None,
        limit: int = None,
    ) -> List[Topic] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/topics",
            headers=self.headers,
            query_params=filter_none_parameters(
                {"page": page, "limit": limit}
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
