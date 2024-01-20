import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
from typing import List
from ..utils.filter import filter_none_parameters
from shikimori.types.general.club import Logo, Club, ClubImage, ClubInfo, Collection
from shikimori.types.titles.animes import Anime
from shikimori.types.titles.manga import Manga
from shikimori.types.general.photo import Photo, PhotoExtended
from shikimori.types.titles.roles import Character
from ..types.user import User
from shikimori.types.titles.ranobe import Ranobe
from shikimori.types.general.topics import Forum


class ClubEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

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
            headers={"User-Agent": self._user_agent},
            query_params=filter_none_parameters(
                {"limit": limit, "page": page, "search": search}
            ),
        )

        if not isinstance(response, RequestError):
            return [Club(**c, logo=Logo(**c["logo"])) for c in response]

        logging.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> ClubInfo | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}",
            headers={"User-Agent": self._user_agent},
        )

        if not isinstance(response, RequestError):
            return ClubInfo(
                **response,
                animes=[
                    Anime(**anime, image=Photo(**anime["image"]))
                    for anime in response["animes"]
                ],
                mangas=[
                    Manga(**manga, image=Photo(**manga["image"]))
                    for manga in response["mangas"]
                ],
                characters=[
                    Character(**ch, image=Photo(**ch["image"]))
                    for ch in response["characters"]
                ],
                members=[
                    User(**u, image=PhotoExtended(**u["image"]))
                    for u in response["members"]
                ],
                images=[ClubImage(**image) for image in response["images"]],
            )

        logging.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(
        self,
        id: int,
        access_token: str,
        name: str = None,
        description: str = None,
        display_images: bool | int = None,
        comment_policy: str = None,
        topic_policy: str = None,
        image_upload_policy: str = None,
    ) -> ClubInfo | RequestError:
        """
        :param id: number.
        :param access_token: auth token
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
            headers={"User-Agent": self._user_agent, "Authorization": f"Bearer {access_token}"},
        )

        if not isinstance(response, RequestError):
            return ClubInfo(
                **response,
                animes=[
                    Anime(**anime, image=Photo(**anime["image"]))
                    for anime in response["animes"]
                ],
                mangas=[
                    Manga(**manga, image=Photo(**manga["image"]))
                    for manga in response["mangas"]
                ],
                characters=[
                    Character(**ch, image=Photo(**ch["image"]))
                    for ch in response["characters"]
                ],
                members=[
                    User(**u, image=PhotoExtended(**u["image"]))
                    for u in response["members"]
                ],
                images=[ClubImage(**image) for image in response["images"]],
            )
        logging.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def Animes(
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
            headers={"User-Agent": self._user_agent},
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [Anime(**anime, image=Photo(**anime["image"])) for anime in response]

        logging.debug(
            f"Bad Request(GetAnimes): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def Mangas(
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
            headers={"User-Agent": self._user_agent},
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [Manga(**manga, image=Photo(**manga["image"])) for manga in response]

        logging.debug(
            f"Bad Request(GetMangas): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def Ranobes(
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
            headers={"User-Agent": self._user_agent},
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [
                Ranobe(**ranobe, image=Photo(**ranobe["image"])) for ranobe in response
            ]

        logging.debug(
            f"Bad Request(GetRanobes): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def Characters(
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
            headers={"User-Agent": self._user_agent},
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [Character(**s, image=Photo(**s["image"])) for s in response]

        logging.debug(
            f"Bad Request(GetCharacters): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def Collections(
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
            headers={"User-Agent": self._user_agent},
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [
                Collection(
                    **s,
                    forum=Forum(**s.get("forum")),
                    user=User(
                        **s.get("user"),
                        image=PhotoExtended(**s["user"]["image"]),
                    ),
                )
                for s in response
            ]

        logging.debug(
            f"Bad Request(GetCollections): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def Clubs(
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
            headers={"User-Agent": self._user_agent},
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [Club(**s, logo=Logo(**s["logo"])) for s in response]

        logging.debug(
            f"Bad Request(Clubs): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def Members(
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
            headers={"User-Agent": self._user_agent},
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [User(**s, image=PhotoExtended(**s["image"])) for s in response]

        logging.debug(
            f"Bad Request(Members): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def Images(
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
            headers={"User-Agent": self._user_agent},
            query_params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [ClubImage(**s) for s in response]

        logging.debug(
            f"Bad Request(Images): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def Join(self, id: int, access_token: str) -> None | RequestError:
        response = (
            await self._request.make_request(
                "POST",
                url=f"{self._base_url}/api/clubs/{id}/join",
                headers={
                    "User-Agent": self._user_agent,
                    "Authorization": f"Bearer {access_token}",
                },
            ),
        )

        if not isinstance(response, RequestError):
            return

        logging.debug(
            f"Bad Request(Join): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def Leave(self, id: int, access_token: str) -> None | RequestError:
        response = (
            await self._request.make_request(
                "POST",
                url=f"{self._base_url}/api/clubs/{id}/leave",
                headers={
                    "User-Agent": self._user_agent,
                    "Authorization": f"Bearer {access_token}",
                },
            ),
        )

        if not isinstance(response, RequestError):
            return

        logging.debug(
            f"Bad Request(Leave): status - {response.status_code}: info - {str(response)}"
        )

        return response

