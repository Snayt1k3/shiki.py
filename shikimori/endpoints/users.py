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
            return [User(**u, image=PhotoExtended(**u["image"])) for u in response]

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
                **response,
                image=PhotoExtended(**response["image"]),
                stats=Stats(
                    **response["stats"],
                    statuses=Statuses(
                        animes=[
                            UserTitle(**a)
                            for a in response["stats"]["statuses"]["anime"]
                        ],
                        manga=[
                            UserTitle(**a)
                            for a in response["stats"]["statuses"]["manga"]
                        ],
                    ),
                    full_statuses=Statuses(
                        animes=[
                            UserTitle(**a)
                            for a in response["stats"]["full_statuses"]["anime"]
                        ],
                        manga=[
                            UserTitle(**a)
                            for a in response["stats"]["full_statuses"]["manga"]
                        ],
                    ),
                    scores=Obj(
                        anime=[
                            ValueObj(**a) for a in response["stats"]["scores"]["anime"]
                        ],
                        manga=[
                            ValueObj(**a) for a in response["stats"]["scores"]["manga"]
                        ],
                    ),
                    types=Obj(
                        anime=[
                            ValueObj(**a) for a in response["stats"]["types"]["anime"]
                        ],
                        manga=[
                            ValueObj(**a) for a in response["stats"]["types"]["manga"]
                        ],
                    ),
                    ratings=Obj(
                        anime=[
                            ValueObj(**a) for a in response["stats"]["ratings"]["anime"]
                        ],
                        manga=[
                            ValueObj(**a) for a in response["stats"]["ratings"]["manga"]
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
            return UserInfoInc(**response, image=PhotoExtended(**response["image"]))

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
            return UserInfoInc(**response, image=PhotoExtended(**response["image"]))

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
            return UserInfoInc(**response, image=PhotoExtended(**response["image"]))

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
                User(**user, image=PhotoExtended(**user["image"])) for user in response
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
            return [Club(**club, logo=Logo(**club["logo"])) for club in response]

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
                    **a,
                    user=User(**a["user"], image=PhotoExtended(**a["user"]["image"])),
                    anime=Anime(**a["anime"], image=Photo(**a["anime"]["image"])),
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
                    **a,
                    user=User(**a["user"], image=PhotoExtended(**a["user"]["image"])),
                    anime=Anime(**a["manga"], image=Photo(**a["manga"]["image"])),
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
                animes=[FavouritesObj(**a) for a in response["anime"]],
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
                    **r,
                    to=User(**r["to"], image=PhotoExtended(**r["to"]["image"])),
                    sender=User(**r["from"], image=PhotoExtended(**r["from"]["image"])),
                    linked=Linked(**r["linked"], image=Photo(**r["linked"]["image"])),
                )
                for r in response
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
                    **obj,
                    target=TitleHistory(
                        **obj["target"], image=Photo(**obj["target"]["image"])
                    )
                    if obj["target"]
                    else None,
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
                    **obj,
                    comment=Comment(**obj["comment"]),
                    user=User(
                        **obj["user"], image=PhotoExtended(**obj["user"]["image"])
                    ),
                    moderator=User(
                        **obj["moderator"],
                        image=PhotoExtended(**obj["moderator"]["image"]),
                    ),
                )
                for obj in response
            ]

        logger.debug(
            f"Bad Request(bans): status - {response.status_code}: info - {str(response)}"
        )

        return response
