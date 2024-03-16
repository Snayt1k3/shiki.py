import logging
from typing import List

from .base import BaseEndpoint
from ..exceptions import RequestError
from shikimori.types.bans import Ban, Comment
from shikimori.types.club import Club, Logo
from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.topics import Linked
from shikimori.types.animes import Anime
from shikimori.types.message import MessageInfo
from shikimori.types.user import (
    User,
    UserTitle,
    UserInfo,
    Statuses,
    Stats,
    Obj,
    ValueObj,
    UserInfoInc,
    Rate,
    FavouritesObj,
    Favourites,
    UnreadMessages,
    TitleHistory,
    HistoryObj,
)
from ..types.manga import Manga
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class UserEndpoint(BaseEndpoint):
    async def list(
        self, page: int = None, limit: int = None, search: str = None
    ) -> List[User] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users",
            query_params=filter_none_parameters(
                {"search": search, "page": page, "limit": limit}
            ),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                User(
                    id=u["id"],
                    nickname=u["nickname"],
                    avatar=u["avatar"],
                    last_online_at=u["last_online_at"],
                    url=u["url"],
                    image=PhotoExtended(**u["image"]),
                )
                for u in response
            ]

        logger.debug(
            f"Bad Request(create): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int, is_nickname: str = None) -> UserInfo | RequestError:
        """

        :param id: num
        :param is_nickname: 1 if you want to get user by its nickname
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}",
            query_params=filter_none_parameters({"is_nickname": is_nickname}),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserInfo(
                id=response["id"],
                avatar=response["avatar"],
                about_html=response["about_html"],
                about=response["about"],
                last_online_at=response["last_online_at"],
                nickname=response["nickname"],
                name=response["name"],
                location=response["location"],
                full_years=response["full_years"],
                is_ignored=response["is_ignored"],
                in_friends=response["in_friends"],
                style_id=response["style_id"],
                common_info=response["common_info"],
                last_online=response["last_online"],
                banned=response["banned"],
                website=response["website"],
                show_comments=response["show_comments"],
                sex=response["sex"],
                url=response["show_comments"],
                image=PhotoExtended(**response["image"]),
                stats=Stats(
                    genres=response["stats"]["genres"],
                    studios=response["stats"]["studios"],
                    publishers=response["stats"]["publishers"],
                    statuses=Statuses(
                        animes=[
                            UserTitle(**a)
                            for a in response["stats"]["statuses"].get("anime", [])
                        ],
                        manga=[
                            UserTitle(**a)
                            for a in response["stats"]["statuses"].get("manga", [])
                        ],
                    ),
                    full_statuses=Statuses(
                        animes=[
                            UserTitle(**a)
                            for a in response["stats"]["full_statuses"].get("anime", [])
                        ],
                        manga=[
                            UserTitle(**a)
                            for a in response["stats"]["full_statuses"].get("manga", [])
                        ],
                    ),
                    scores=Obj(
                        anime=[
                            ValueObj(**a)
                            for a in response["stats"]["scores"].get("anime", [])
                        ],
                        manga=[
                            ValueObj(**a)
                            for a in response["stats"]["scores"].get("manga", [])
                        ],
                    ),
                    types=Obj(
                        anime=[
                            ValueObj(**a)
                            for a in response["stats"]["types"].get("anime", [])
                        ],
                        manga=[
                            ValueObj(**a)
                            for a in response["stats"]["types"].get("manga", [])
                        ],
                    ),
                    ratings=Obj(
                        anime=[
                            ValueObj(**a)
                            for a in response["stats"]["ratings"].get("anime", [])
                        ],
                        manga=[
                            ValueObj(**a)
                            for a in response["stats"]["ratings"].get("manga", [])
                        ],
                    ),
                    activity=[ValueObj(**a) for a in response["stats"]["activity"]],
                    has_anime=response["stats"]["has_anime?"],
                    has_manga=response["stats"]["has_manga?"],
                ),
            )

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def info(self, id: int) -> User | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/info",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return UserInfoInc(
                sex=response["sex"],
                full_years=response["full_years"],
                avatar=response["avatar"],
                id=response["id"],
                birth_on=response["birth_on"],
                last_online_at=response["last_online_at"],
                locale=response["locale"],
                url=response["url"],
                name=response["name"],
                nickname=response["name"],
                image=PhotoExtended(**response["image"]),
            )

        logger.debug(
            f"Bad Request(info): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def whoami(self) -> User | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/whoami",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return UserInfoInc(
                sex=response["sex"],
                full_years=response["full_years"],
                avatar=response["avatar"],
                id=response["id"],
                birth_on=response["birth_on"],
                last_online_at=response["last_online_at"],
                locale=response["locale"],
                url=response["url"],
                name=response["name"],
                nickname=response["name"],
                image=PhotoExtended(**response["image"]),
            )

        logger.debug(
            f"Bad Request(whoami): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def signOut(self) -> User | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/whoami",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return UserInfoInc(
                sex=response["sex"],
                full_years=response["full_years"],
                avatar=response["avatar"],
                id=response["id"],
                birth_on=response["birth_on"],
                last_online_at=response["last_online_at"],
                locale=response["locale"],
                url=response["url"],
                name=response["name"],
                nickname=response["name"],
                image=PhotoExtended(**response["image"]),
            )

        logger.debug(
            f"Bad Request(whoami): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def friends(self) -> List[User] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/friends",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return [
                User(
                    id=u["id"],
                    nickname=u["nickname"],
                    avatar=u["avatar"],
                    last_online_at=u["last_online_at"],
                    url=u["url"],
                    image=PhotoExtended(**u["image"]),
                )
                for u in response
            ]

        logger.debug(
            f"Bad Request(friends): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def clubs(self, id: int) -> List[Club] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/clubs",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return [
                Club(
                    logo=Logo(**club["logo"]),
                    comment_policy=club["comment_policy"],
                    id=club["id"],
                    name=club["name"],
                    is_censored=club["is_censored"],
                    join_policy=club["join_policy"],
                )
                for club in response
            ]

        logger.debug(
            f"Bad Request(clubs): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def animeRates(
        self,
        id: int,
        limit: int = None,
        page: int = None,
        status: str = None,
        censored: bool = None,
    ) -> List[Rate] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/anime_rates",
            query_params=filter_none_parameters(
                {"limit": limit, "page": page, "status": status, "censored": censored}
            ),
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return [
                Rate(
                    id=a["id"],
                    chapters=a["chapters"],
                    episodes=a["episodes"],
                    manga=None,
                    rewatches=a["rewatches"],
                    status=a["status"],
                    score=a["score"],
                    text=a["text"],
                    text_html=a["text_html"],
                    volumes=a["volumes"],
                    user=User(
                        id=a["user"]["id"],
                        nickname=a["user"]["nickname"],
                        avatar=a["user"]["avatar"],
                        last_online_at=a["user"]["last_online_at"],
                        url=a["user"]["url"],
                        image=PhotoExtended(**a["user"]["image"]),
                    ),
                    anime=Anime(
                        id=a["anime"]["id"],
                        name=a["anime"]["name"],
                        russian=a["anime"]["russian"],
                        image=Photo(**a["anime"]["image"]),
                        url=a["anime"]["url"],
                        kind=a["anime"]["kind"],
                        score=a["anime"]["score"],
                        status=a["anime"]["status"],
                        episodes=a["anime"]["episodes"],
                        episodes_aired=a["anime"]["episodes_aired"],
                        aired_on=a["anime"]["aired_on"],
                        released_on=a["anime"]["released_on"],
                    ),
                )
                for a in response
            ]

        logger.debug(
            f"Bad Request(animeRates): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def mangaRates(
        self,
        id: int,
        limit: int = None,
        page: int = None,
        censored: bool = None,
    ) -> List[Rate] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/manga_rates",
            query_params=filter_none_parameters(
                {"limit": limit, "page": page, "censored": censored}
            ),
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return [
                Rate(
                    id=a["id"],
                    chapters=a["chapters"],
                    episodes=a["episodes"],
                    rewatches=a["rewatches"],
                    status=a["status"],
                    score=a["score"],
                    text=a["text"],
                    anime=None,
                    text_html=a["text_html"],
                    volumes=a["volumes"],
                    user=User(
                        id=a["user"]["id"],
                        nickname=a["user"]["nickname"],
                        avatar=a["user"]["avatar"],
                        last_online_at=a["user"]["last_online_at"],
                        url=a["user"]["url"],
                        image=PhotoExtended(**a["user"]["image"]),
                    ),
                    manga=Manga(
                        id=a["manga"]["id"],
                        name=a["manga"]["name"],
                        russian=a["manga"]["russian"],
                        image=Photo(**a["manga"]["image"]),
                        url=a["manga"]["url"],
                        kind=a["manga"]["kind"],
                        score=a["manga"]["score"],
                        status=a["manga"]["status"],
                        volumes=a["manga"]["volumes"],
                        chapters=a["manga"]["chapters"],
                        aired_on=a["manga"]["aired_on"],
                        released_on=a["manga"]["released_on"],
                    ),
                )
                for a in response
            ]

        logger.debug(
            f"Bad Request(MangaRates): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def favourites(self, id: int) -> Favourites | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/favourites",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return Favourites(
                animes=[FavouritesObj(**a) for a in response["animes"]],
                characters=[FavouritesObj(**a) for a in response["characters"]],
                producers=[FavouritesObj(**a) for a in response["producers"]],
                mangakas=[FavouritesObj(**a) for a in response["mangakas"]],
                mangas=[FavouritesObj(**a) for a in response["mangas"]],
                seyu=[FavouritesObj(**a) for a in response["seyu"]],
                ranobe=[FavouritesObj(**a) for a in response["ranobe"]],
            )

        logger.debug(
            f"Bad Request(favourites): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def messages(
        self, id: int, page: int = None, limit: int = None, type: str = None
    ) -> List[MessageInfo] | RequestError:
        """
        :param id: user id
        :param page: Must be a number between 1 and 100000.
        :param limit: 100 maximum
        :param type: Must be one of: inbox, private, sent, news, notifications.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/messages",
            headers=self.headers,
            query_params=filter_none_parameters(
                {"page": page, "limit": limit, "type": type}
            ),
        )

        if not isinstance(response, RequestError):
            return [
                MessageInfo(
                    id=s["id"],
                    kind=s["kind"],
                    body=s["body"],
                    html_body=s["html_body"],
                    created_at=s["created_at"],
                    linked_id=s["linked_id"],
                    linked_type=s["linked_type"],
                    read=s["read"],
                    linked=(
                        Linked(
                            name=s["linked"]["name"],
                            id=s["linked"]["id"],
                            russian=s["linked"]["russian"],
                            url=s["linked"]["url"],
                            kind=s["linked"]["kind"],
                            score=s["linked"]["score"],
                            status=s["linked"]["status"],
                            episodes=s["linked"]["episodes"],
                            episodes_aired=s["linked"]["episodes_aired"],
                            aired_on=s["linked"]["aired_on"],
                            released_on=s["linked"]["released_on"],
                            image=Photo(**s["linked"]["image"]),
                        )
                        if s["linked"]
                        else None
                    ),
                    to=User(
                        id=s["to"]["id"],
                        avatar=s["to"]["avatar"],
                        image=PhotoExtended(**s["to"]["image"]),
                        last_online_at=s["to"]["last_online_at"],
                        nickname=s["to"]["nickname"],
                        url=s["to"]["url"],
                    ),
                    sender=User(
                        id=s["from"]["id"],
                        avatar=s["from"]["avatar"],
                        image=PhotoExtended(**s["from"]["image"]),
                        last_online_at=s["from"]["last_online_at"],
                        nickname=s["from"]["nickname"],
                        url=s["from"]["url"],
                    ),
                )
                for s in response
            ]

        logger.debug(
            f"Bad Request(messages): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def unread(self, id: int) -> UnreadMessages | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/unread_messages",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UnreadMessages(**response)

        logger.debug(
            f"Bad Request(unread): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def history(
        self,
        id: int,
        page: int = None,
        limit: int = None,
        target_type: str = None,
        target_id: int = None,
    ) -> List[HistoryObj] | RequestError:
        """

        :param id: Must be a number.
        :param page: Must be a number between 1 and 100000.
        :param limit: 100 maximum
        :param target_type: Must be one of: Anime, Manga.
        :param target_id: Must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/history",
            headers=self.headers,
            query_params=filter_none_parameters(
                {
                    "page": page,
                    "limit": limit,
                    "target_type": target_type,
                    "target_id": target_id,
                }
            ),
        )

        if not isinstance(response, RequestError):
            return [
                HistoryObj(
                    id=obj["id"],
                    description=obj["description"],
                    target=(
                        TitleHistory(
                            id=obj["target"]["id"],
                            name=obj["target"]["name"],
                            russian=obj["target"]["russian"],
                            image=Photo(**obj["target"]["image"]),
                            url=obj["target"]["url"],
                            kind=obj["target"]["kind"],
                            score=obj["target"]["score"],
                            status=obj["target"]["status"],
                            episodes=obj["target"].get("episodes"),
                            volumes=obj["target"].get("volumes"),
                            chapters=obj["target"].get("chapters"),
                            episodes_aired=obj["target"].get("episodes_aired"),
                            aired_on=obj["target"]["aired_on"],
                            released_on=obj["target"]["released_on"],
                        )
                        if obj["target"]
                        else None
                    ),
                )
                for obj in response
            ]

        logger.debug(
            f"Bad Request(history): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def bans(self, id: int) -> List[Ban] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/bans",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return [
                Ban(
                    id=b["id"],
                    created_at=b["created_at"],
                    duration_minutes=b["duration_minutes"],
                    moderator_id=b["moderator_id"],
                    reason=b["reason"],
                    user_id=b["user_id"],
                    comment=Comment(**b["comment"]),
                    user=User(
                        id=b["user"]["id"],
                        avatar=b["user"]["avatar"],
                        image=PhotoExtended(**b["user"]["image"]),
                        last_online_at=b["user"]["last_online_at"],
                        nickname=b["user"]["nickname"],
                        url=b["user"]["url"],
                    ),
                    moderator=User(
                        id=b["moderator"]["id"],
                        avatar=b["moderator"]["avatar"],
                        image=PhotoExtended(**b["moderator"]["image"]),
                        last_online_at=b["moderator"]["last_online_at"],
                        nickname=b["moderator"]["nickname"],
                        url=b["moderator"]["url"],
                    ),
                )
                for b in response
            ]

        logger.debug(
            f"Bad Request(bans): status - {response.status_code}: info - {str(response)}"
        )

        return response
