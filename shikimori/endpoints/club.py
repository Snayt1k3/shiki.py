import logging
from typing import List

from shikimori.types.animes import Anime
from shikimori.types.club import Logo, Club, ClubImage, ClubInfo, Collection
from shikimori.types.manga import Manga
from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.ranobe import Ranobe
from shikimori.types.roles import Character
from shikimori.types.topics import Forum
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.user import User
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class ClubEndpoint(BaseEndpoint):
    async def list(
        self, page: int = None, limit: int = None, search: str = None
    ) -> List[Club] | RequestError:
        """
        List clubs
        :param page: Must be a number between 1 and 100000.
        :param limit: 30 max
        :param search: string

        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs",
            headers=self.headers,
            query_params=filter_none_parameters(
                {"limit": limit, "page": page, "search": search}
            ),
        )

        if not isinstance(response, RequestError):
            return [
                Club(
                    logo=Logo(**c["logo"]),
                    comment_policy=c["comment_policy"],
                    id=c["id"],
                    name=c["name"],
                    is_censored=c["is_censored"],
                    join_policy=c["join_policy"],
                )
                for c in response
            ]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> ClubInfo | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return ClubInfo(
                id=response["id"],
                name=response["name"],
                is_censored=response["is_censored"],
                logo=Logo(**response["logo"]),
                join_policy=response["join_policy"],
                comment_policy=response["comment_policy"],
                description=response["description"],
                description_html=response["description_html"],
                style_id=response["style_id"],
                topic_id=response["topic_id"],
                thread_id=response["thread_id"],
                user_role=response["user_role"],
                animes=[
                    Anime(
                        id=anime["id"],
                        name=anime["name"],
                        russian=anime["russian"],
                        image=Photo(**anime["image"]),
                        url=anime["url"],
                        kind=anime["kind"],
                        score=anime["score"],
                        status=anime["status"],
                        episodes=anime["episodes"],
                        episodes_aired=anime["episodes_aired"],
                        aired_on=anime["aired_on"],
                        released_on=anime["released_on"],
                    )
                    for anime in response["animes"]
                ],
                mangas=[
                    Manga(
                        id=manga["id"],
                        name=manga["name"],
                        russian=manga["russian"],
                        image=Photo(**manga["image"]),
                        url=manga["url"],
                        kind=manga["kind"],
                        score=manga["score"],
                        status=manga["status"],
                        volumes=manga["volumes"],
                        chapters=manga["chapters"],
                        aired_on=manga["aired_on"],
                        released_on=manga["released_on"],
                    )
                    for manga in response["mangas"]
                ],
                characters=[
                    Character(
                        id=ch["id"],
                        name=ch["name"],
                        russian=ch["russian"],
                        url=ch["url"],
                        image=Photo(**ch["image"]),
                    )
                    for ch in response["characters"]
                ],
                members=[
                    User(
                        id=u["id"],
                        nickname=u["nickname"],
                        avatar=u["avatar"],
                        last_online_at=u["last_online_at"],
                        url=u["url"],
                        image=PhotoExtended(**u["image"]),
                    )
                    for u in response["members"]
                ],
                images=[ClubImage(**image) for image in response["images"]],
            )

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(
        self,
        id: int,
        name: str = None,
        description: str = None,
        display_images: bool | int = None,
        comment_policy: str = None,
        topic_policy: str = None,
        image_upload_policy: str = None,
    ) -> ClubInfo | RequestError:
        """
        requires oauth scope
        :param id: number.
        :param name: string.
        :param description: string.
        :param display_images: Must be one of: true, false, 1, 0.
        :param comment_policy: Must be one of: free, members, admins.
        :param topic_policy: Must be one of: members, admins.
        :param image_upload_policy: Must be one of: members, admins.
        """
        response = await self._request.make_request(
            "PATCH",
            url=f"{self._base_url}/api/clubs/{id}",
            body={
                "club": filter_none_parameters(
                    {
                        "description": description,
                        "name": name,
                        "display_images": display_images,
                        "comment_policy": comment_policy,
                        "topic_policy": topic_policy,
                        "image_upload_policy": image_upload_policy,
                    }
                )
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return ClubInfo(
                id=response["id"],
                name=response["name"],
                is_censored=response["is_censored"],
                logo=Logo(**response["logo"]),
                join_policy=response["join_policy"],
                comment_policy=response["comment_policy"],
                description=response["description"],
                description_html=response["description_html"],
                style_id=response["style_id"],
                topic_id=response["topic_id"],
                thread_id=response["thread_id"],
                user_role=response["user_role"],
                animes=[
                    Anime(
                        id=anime["id"],
                        name=anime["name"],
                        russian=anime["russian"],
                        image=Photo(**anime["image"]),
                        url=anime["url"],
                        kind=anime["kind"],
                        score=anime["score"],
                        status=anime["status"],
                        episodes=anime["episodes"],
                        episodes_aired=anime["episodes_aired"],
                        aired_on=anime["aired_on"],
                        released_on=anime["released_on"],
                    )
                    for anime in response["animes"]
                ],
                mangas=[
                    Manga(
                        id=manga["id"],
                        name=manga["name"],
                        russian=manga["russian"],
                        image=Photo(**manga["image"]),
                        url=manga["url"],
                        kind=manga["kind"],
                        score=manga["score"],
                        status=manga["status"],
                        volumes=manga["volumes"],
                        chapters=manga["chapters"],
                        aired_on=manga["aired_on"],
                        released_on=manga["released_on"],
                    )
                    for manga in response["mangas"]
                ],
                characters=[
                    Character(
                        id=ch["id"],
                        name=ch["name"],
                        russian=ch["russian"],
                        url=ch["url"],
                        image=Photo(**ch["image"]),
                    )
                    for ch in response["characters"]
                ],
                members=[
                    User(
                        id=u["id"],
                        nickname=u["nickname"],
                        avatar=u["avatar"],
                        last_online_at=u["last_online_at"],
                        url=u["url"],
                        image=PhotoExtended(**u["image"]),
                    )
                    for u in response["members"]
                ],
                images=[ClubImage(**image) for image in response["images"]],
            )

        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def animes(
        self, id: int, limit: int = None, page: int = None
    ) -> List[Anime] | RequestError:
        """
        List of club animes
        :param id: must a number
        :param limit: 20 maximum
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/animes",
            headers=self.headers,
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [
                Anime(
                    id=anime["id"],
                    name=anime["name"],
                    russian=anime["russian"],
                    image=Photo(**anime["image"]),
                    url=anime["url"],
                    kind=anime["kind"],
                    score=anime["score"],
                    status=anime["status"],
                    episodes=anime["episodes"],
                    episodes_aired=anime["episodes_aired"],
                    aired_on=anime["aired_on"],
                    released_on=anime["released_on"],
                )
                for anime in response
            ]

        logger.debug(
            f"Bad Request(GetAnimes): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def mangas(
        self, id: int, page: int = None, limit: int = None
    ) -> List[Manga] | RequestError:
        """
        List of club mangas
        :param id: must a number
        :param limit: 20 maximum
        :param page: Must be a number between 1 and 100000.
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/mangas",
            headers=self.headers,
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [
                Manga(
                    id=manga["id"],
                    name=manga["name"],
                    russian=manga["russian"],
                    image=Photo(**manga["image"]),
                    url=manga["url"],
                    kind=manga["kind"],
                    score=manga["score"],
                    status=manga["status"],
                    volumes=manga["volumes"],
                    chapters=manga["chapters"],
                    aired_on=manga["aired_on"],
                    released_on=manga["released_on"],
                )
                for manga in response
            ]

        logger.debug(
            f"Bad Request(GetMangas): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ranobes(
        self, id: int, limit: int = None, page: int = None
    ) -> List[Ranobe] | RequestError:
        """
        List of club Ranobes
        :param id: must a number
        :param limit: 20 maximum
        :param page: Must be a number between 1 and 100000.
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/ranobe",
            headers=self.headers,
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [
                Ranobe(
                    id=ranobe["id"],
                    name=ranobe["name"],
                    russian=ranobe["russian"],
                    image=Photo(**ranobe["image"]),
                    url=ranobe["url"],
                    kind=ranobe["kind"],
                    score=ranobe["score"],
                    status=ranobe["status"],
                    volumes=ranobe["volumes"],
                    chapters=ranobe["chapters"],
                    aired_on=ranobe["aired_on"],
                    released_on=ranobe["released_on"],
                )
                for ranobe in response
            ]

        logger.debug(
            f"Bad Request(GetRanobes): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def characters(
        self, id: int, limit: int = None, page: int = None
    ) -> List[Character] | RequestError:
        """
        List of club Characters
        :param id: must a number
        :param limit: 20 maximum
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/characters",
            headers=self.headers,
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [
                Character(
                    id=s["id"],
                    name=s["name"],
                    russian=s["russian"],
                    url=s["url"],
                    image=Photo(**s["image"]),
                )
                for s in response
            ]

        logger.debug(
            f"Bad Request(GetCharacters): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def collections(
        self, id: int, limit: int = None, page: int = None
    ) -> List[Collection] | RequestError:
        """
        List of club Collections
        :param id: must a number
        :param limit: 4 maximum
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/collections",
            headers=self.headers,
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [
                Collection(
                    body=s["body"],
                    comments_count=s["comments_count"],
                    id=s["id"],
                    linked=s["linked"],
                    linked_id=s["linked_id"],
                    created_at=s["created_at"],
                    episode=s["episode"],
                    event=s["event"],
                    html_body=s["html_body"],
                    html_footer=s["html_footer"],
                    last_comment_viewed=s["last_comment_viewed"],
                    linked_type=s["linked_type"],
                    topic_title=s["topic_title"],
                    type=s["type"],
                    viewed=s["viewed"],
                    forum=Forum(**s.get("forum")),
                    user=User(
                        id=s["user"]["id"],
                        avatar=s["user"]["avatar"],
                        url=s["user"]["url"],
                        last_online_at=s["user"]["last_online_at"],
                        nickname=s["user"]["nickname"],
                        image=PhotoExtended(**s["user"]["image"]),
                    ),
                )
                for s in response
            ]

        logger.debug(
            f"Bad Request(GetCollections): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def clubs(
        self, id: int, limit: int = None, page: int = None
    ) -> List[Club] | RequestError:
        """
        List of club clubs
        :param id: must a number
        :param limit: 30 maximum
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/clubs",
            headers=self.headers,
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [
                Club(
                    logo=Logo(**c["logo"]),
                    comment_policy=c["comment_policy"],
                    id=c["id"],
                    name=c["name"],
                    is_censored=c["is_censored"],
                    join_policy=c["join_policy"],
                )
                for c in response
            ]

        logger.debug(
            f"Bad Request(Clubs): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def members(
        self, id: int, limit: int = None, page: int = None
    ) -> List[User] | RequestError:
        """
        List of club members
        :param id: must a number
        :param limit: 100 maximum
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/members",
            headers=self.headers,
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [User(
                        id=u["id"],
                        nickname=u["nickname"],
                        avatar=u["avatar"],
                        last_online_at=u["last_online_at"],
                        url=u["url"],
                        image=PhotoExtended(**u["image"]),
                    ) for u in response]

        logger.debug(
            f"Bad Request(Members): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def images(
        self, id: int, limit: int = None, page: int = None
    ) -> List[ClubImage] | RequestError:
        """
        List of club Images
        :param id: must a number
        :param limit: 100 maximum
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/images",
            headers=self.headers,
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [ClubImage(**s) for s in response]

        logger.debug(
            f"Bad Request(Images): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def join(self, id: int) -> None | RequestError:
        """requires oauth scope"""
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/clubs/{id}/join",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(Join): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def leave(self, id: int) -> None | RequestError:
        """requires oauth scope !"""
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/clubs/{id}/leave",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(Leave): status - {response.status_code}: info - {str(response)}"
        )

        return response
