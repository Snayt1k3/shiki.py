import logging
from typing import List

from shikimori.types.animes import (
    Anime,
    Relation,
    ExternalLink,
)
from shikimori.types.franchise import Franchise, Node, Link
from shikimori.types.genres import Genre
from shikimori.types.manga import Manga
from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.ranobe import Ranobe, RanobeInfo
from shikimori.types.roles import Role, Character
from shikimori.types.topics import Topic, Forum, Linked
from shikimori.types.user import User
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.user_rates import MiniUserRate
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
            return [
                Ranobe(
                    id=s["id"],
                    name=s["name"],
                    russian=s["russian"],
                    image=Photo(**s["image"]),
                    url=s["url"],
                    kind=s["kind"],
                    score=s["score"],
                    status=s["status"],
                    chapters=s["chapters"],
                    volumes=s["volumes"],
                    aired_on=s["aired_on"],
                    released_on=s["released_on"],
                )
                for s in response
            ]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> RanobeInfo | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}api/ranobe/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return RanobeInfo(
                id=response["id"],
                name=response["name"],
                russian=response["russian"],
                image=response["image"],
                url=response["url"],
                kind=response["kind"],
                score=response["score"],
                status=response["status"],
                volumes=response["volumes"],
                chapters=response["chapters"],
                aired_on=response["aired_on"],
                released_on=response["released_on"],
                english=response["english"],
                japanese=response["japanese"],
                synonyms=response["synonyms"],
                license_name_ru=response["license_name_ru"],
                description=response["description"],
                description_html=response["description_html"],
                description_source=response["description_source"],
                franchise=response["franchise"],
                favoured=response["favoured"],
                anons=response["anons"],
                ongoing=response["ongoing"],
                thread_id=response["thread_id"],
                topic_id=response["topic_id"],
                myanimelist_id=response["myanimelist_id"],
                rates_scores_stats=response["rates_scores_stats"],
                rates_statuses_stats=response["rates_statuses_stats"],
                licensors=response["licensors"],
                genres=[Genre(**genre) for genre in response["genres"]],
                user_rate=(
                    MiniUserRate(**response["user_rate"])
                    if response["user_rate"]
                    else None
                ),
            )

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def roles(self, id: int) -> List[Role] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/roles",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                Role(
                    roles=role["roles"],
                    roles_russian=role["roles_russian"],
                    character=(
                        Character(
                            id=role["character"]["id"],
                            name=role["character"]["name"],
                            russian=role["character"]["russian"],
                            url=role["character"]["url"],
                            image=Photo(**role["character"]["image"]),
                        )
                        if role["character"]
                        else None
                    ),
                    person=(
                        Character(
                            id=role["person"]["id"],
                            name=role["person"]["name"],
                            russian=role["person"]["russian"],
                            url=role["person"]["url"],
                            image=Photo(**role["person"]["image"]),
                        )
                        if role["person"]
                        else None
                    ),
                )
                for role in response
            ]

        logger.debug(
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
            return [
                Ranobe(
                    id=s["id"],
                    name=s["name"],
                    russian=s["russian"],
                    image=Photo(**s["image"]),
                    url=s["url"],
                    kind=s["kind"],
                    score=s["score"],
                    status=s["status"],
                    chapters=s["chapters"],
                    volumes=s["volumes"],
                    aired_on=s["aired_on"],
                    released_on=s["released_on"],
                )
                for s in response
            ]

        logger.debug(
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
                    relation=relation["relation"],
                    relation_russian=relation["relation_russian"],
                    anime=(
                        Anime(
                            id=relation["anime"]["id"],
                            name=relation["anime"]["name"],
                            russian=relation["anime"]["russian"],
                            image=Photo(**relation["anime"]["image"]),
                            url=relation["anime"]["url"],
                            kind=relation["anime"]["kind"],
                            score=relation["anime"]["score"],
                            status=relation["anime"]["status"],
                            episodes=relation["anime"]["episodes"],
                            episodes_aired=relation["anime"]["episodes_aired"],
                            aired_on=relation["anime"]["aired_on"],
                            released_on=relation["anime"]["released_on"],
                        )
                        if relation["anime"]
                        else None
                    ),
                    manga=(
                        Manga(
                            id=relation["manga"]["id"],
                            name=relation["manga"]["name"],
                            russian=relation["manga"]["russian"],
                            image=Photo(**relation["manga"]["image"]),
                            url=relation["manga"]["url"],
                            kind=relation["manga"]["kind"],
                            score=relation["manga"]["score"],
                            status=relation["manga"]["status"],
                            chapters=relation["manga"]["chapters"],
                            volumes=relation["manga"]["volumes"],
                            aired_on=relation["manga"]["aired_on"],
                            released_on=relation["manga"]["released_on"],
                        )
                        if relation["manga"]
                        else None
                    ),
                )
                for relation in response
            ]

        logger.debug(
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
                current_id=response["current_id"],
            )

        logger.debug(
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
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/ranobe/{id}/topics",
            headers=self.headers,
            query_params=filter_none_parameters({"page": page, "limit": limit}),
        )

        if not isinstance(response, RequestError):
            return [
                Topic(
                    id=topic["id"],
                    topic_title=topic["topic_title"],
                    body=topic["body"],
                    html_body=topic["html_body"],
                    html_footer=topic["html_footer"],
                    created_at=topic["created_at"],
                    comments_count=topic["comments_count"],
                    type=topic["type"],
                    linked_id=topic["linked_id"],
                    linked_type=topic["linked_type"],
                    viewed=topic["viewed"],
                    last_comment_viewed=topic["last_comment_viewed"],
                    event=topic["event"],
                    episode=topic["episode"],
                    forum=Forum(**topic["forum"]),
                    user=User(
                        id=topic["user"]["id"],
                        nickname=topic["user"]["nickname"],
                        avatar=topic["user"]["avatar"],
                        last_online_at=topic["user"]["last_online_at"],
                        url=topic["user"]["url"],
                        image=PhotoExtended(**topic["user"]["image"]),
                    ),
                    linked=(
                        Linked(
                            name=topic["linked"]["name"],
                            id=topic["linked"]["id"],
                            russian=topic["linked"]["russian"],
                            url=topic["linked"]["url"],
                            kind=topic["linked"]["kind"],
                            score=topic["linked"]["score"],
                            status=topic["linked"]["status"],
                            volumes=topic["linked"]["volumes"],
                            chapters=topic["linked"]["chapters"],
                            aired_on=topic["linked"]["aired_on"],
                            released_on=topic["linked"]["released_on"],
                            image=Photo(**topic["linked"]["image"]),
                        )
                        if topic["linked"]
                        else None
                    ),
                )
                for topic in response
            ]

        logger.debug(
            f"Bad Request(topics): status - {response.status_code}: info - {str(response)}"
        )

        return response
