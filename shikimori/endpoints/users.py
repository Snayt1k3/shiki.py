import logging
from typing import List

from shikimori.types.bans import Ban
from shikimori.types.club import Club
from shikimori.types.message import MessageInfo
from shikimori.types.user import (
    User,
    UserInfo,
    UserInfoInc,
    Rate,
    Favourites,
    UnreadMessages,
    HistoryObj,
)
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class UserEndpoint(BaseEndpoint):
    async def list(
        self, page: int = None, limit: int = None, search: str = None
    ) -> List[User] | RequestError:
        """
        list users.

        :param page: Must be a number between 1 and 100000.
        :param limit: 100 maximum
        :param search: Must be a String
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users",
            params=filter_none_parameters(
                {"search": search, "page": page, "limit": limit}
            ),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [User.from_dict(u) for u in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int, is_nickname: str = None) -> UserInfo | RequestError:
        """
        Show a user.

        :param id: must be a number
        :param is_nickname: 1 if you want to get user by its nickname
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}",
            params=filter_none_parameters({"is_nickname": is_nickname}),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserInfo.from_dict(response)

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def info(self, id: int) -> UserInfoInc | RequestError:
        """
        Show user's brief info.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/info",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return UserInfoInc.from_dict(response)

        logger.debug(
            f"Bad Request(info): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def whoami(self) -> UserInfoInc | RequestError:
        """
        Show current user's brief info
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/whoami",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return UserInfoInc.from_dict(response)

        logger.debug(
            f"Bad Request(whoami): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def signOut(self) -> None | RequestError:
        """
        Sign out the user
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/users/sign_out",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(signOut): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def friends(
        self, page: int = None, limit: int = None
    ) -> List[User] | RequestError:
        """
        Show user's friends.

        :param limit: 100 maximum.
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/friends",
            headers=self.headers,
            json=filter_none_parameters({"page": page, "limit": limit}),
        )
        if not isinstance(response, RequestError):
            return [User.from_dict(u) for u in response]

        logger.debug(
            f"Bad Request(friends): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def clubs(self, id: int) -> List[Club] | RequestError:
        """
        Show user's clubs.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/clubs",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return [Club.from_dict(club) for club in response]

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
        """
        Show user's anime list.

        :param id: must be a number
        :param limit: Must be a number between 1 and 100000
        :param page: 5000 maximum
        :param status: Must be one of: planned, watching, rewatching, completed, on_hold, dropped.
        :param censored: Must be one of: true, false.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/anime_rates",
            params=filter_none_parameters(
                {"limit": limit, "page": page, "status": status, "censored": censored}
            ),
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return [Rate.from_dict(rate) for rate in response]

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
        """
        Show user's manga list.

        :param id: must be a number
        :param limit: Must be a number between 1 and 100000
        :param page: 5000 maximum
        :param censored: Must be one of: true, false.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/manga_rates",
            params=filter_none_parameters(
                {"limit": limit, "page": page, "censored": censored}
            ),
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return [Rate.from_dict(rate) for rate in response]

        logger.debug(
            f"Bad Request(MangaRates): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def favourites(self, id: int) -> Favourites | RequestError:
        """
        Show user's favourites.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/favourites",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return Favourites.from_dict(response)

        logger.debug(
            f"Bad Request(favourites): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def messages(
        self, id: int, page: int = None, limit: int = None, type: str = None
    ) -> List[MessageInfo] | RequestError:
        """
        Show current user's messages.

        :param id: must be a number.
        :param page: Must be a number between 1 and 100000.
        :param limit: 100 maximum
        :param type: Must be one of: inbox, private, sent, news, notifications.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/messages",
            headers=self.headers,
            params=filter_none_parameters({"page": page, "limit": limit, "type": type}),
        )

        if not isinstance(response, RequestError):
            return [MessageInfo.from_dict(msg) for msg in response]

        logger.debug(
            f"Bad Request(messages): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def unread(self, id: int) -> UnreadMessages | RequestError:
        """
        Show current user's unread messages counts.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/unread_messages",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UnreadMessages.from_dict(response)

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
        Show user history.

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
            params=filter_none_parameters(
                {
                    "page": page,
                    "limit": limit,
                    "target_type": target_type,
                    "target_id": target_id,
                }
            ),
        )

        if not isinstance(response, RequestError):
            return [HistoryObj.from_dict(obj) for obj in response]

        logger.debug(
            f"Bad Request(history): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def bans(self, id: int) -> List[Ban] | RequestError:
        """
        Show user's bans.

        :param id: Must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/users/{id}/bans",
            headers=self.headers,
        )
        if not isinstance(response, RequestError):
            return [Ban.from_dict(ban) for ban in response]

        logger.debug(
            f"Bad Request(bans): status - {response.status_code}: info - {str(response)}"
        )

        return response
