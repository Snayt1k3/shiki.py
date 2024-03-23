import logging
from typing import List

from shikimori.types.topics import Topic, Forum, Linked
from shikimori.types.animes import (
    Anime,
    Relation,
    ExternalLink,
)
from shikimori.types.franchise import Franchise, Node, Link
from .base import BaseEndpoint
from ..exceptions import RequestError
from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.genres import Genre
from shikimori.types.manga import Manga, MangaInfo
from shikimori.types.roles import Role, Character
from shikimori.types.user import User
from shikimori.types.user_rates import MiniUserRate
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
            return [
                Manga(
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

    async def ById(self, id: int) -> MangaInfo | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}api/mangas/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return MangaInfo(
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
                user_rate=MiniUserRate(**response["user_rate"])
                if response["user_rate"]
                else None,
            )

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def roles(self, id: int) -> List[Role] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas/{id}/roles",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                Role(
                    roles=role["roles"],
                    roles_russian=role["roles_russian"],
                    character=Character(
                        id=role["character"]["id"],
                        name=role["character"]["name"],
                        russian=role["character"]["russian"],
                        url=role["character"]["url"],
                        image=Photo(**role["character"]["image"]),
                    )
                    if role["character"]
                    else None,
                    person=Character(
                        id=role["person"]["id"],
                        name=role["person"]["name"],
                        russian=role["person"]["russian"],
                        url=role["person"]["url"],
                        image=Photo(**role["person"]["image"]),
                    )
                    if role["person"]
                    else None,
                )
                for role in response
            ]

        logger.debug(
            f"Bad Request(roles): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def similar(self, id: int) -> List[Manga] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas/{id}/similar",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                Manga(
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
            url=f"{self._base_url}/api/mangas/{id}/related",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                Relation(
                    relation=relation["relation"],
                    relation_russian=relation["relation_russian"],
                    anime=Anime(
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
                    else None,
                    manga=Manga(
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
                    ) if relation["manga"] else None,
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
            url=f"{self._base_url}/api/mangas/{id}/franchise",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Franchise(
                nodes=[Node(**node) for node in response.get("nodes")],
                links=[Link(**link) for link in response.get("links")],
                current_id=response["current_id"]
            )

        logger.debug(
            f"Bad Request(franchise): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ExternalLinks(self, id: int) -> List[ExternalLink] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/mangas/{id}/external_links",
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
            url=f"{self._base_url}/api/mangas/{id}/topics",
            headers=self.headers,
            params=filter_none_parameters(
                {"page": page, "limit": limit, "kind": kind, "episode": episode}
            ),
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
                    linked=Linked(
                        name=topic["linked"]["name"],
                        id=topic["linked"]["id"],
                        russian=topic["linked"]["russian"],
                        url=topic["linked"]["url"],
                        kind=topic["linked"]["kind"],
                        score=topic["linked"]["score"],
                        status=topic["linked"]["status"],
                        chapters=topic["linked"]["chapters"],
                        volumes=topic["linked"]["volumes"],
                        aired_on=topic["linked"]["aired_on"],
                        released_on=topic["linked"]["released_on"],
                        image=Photo(**topic["linked"]["image"])
                    ) if topic["linked"] else None,
                )
                for topic in response
            ]

        return response
