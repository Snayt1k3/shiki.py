import logging
from typing import List

from shikimori.types.animes import Anime
from shikimori.types.club import Club, ClubImage, ClubInfo, Collection
from shikimori.types.manga import Manga
from shikimori.types.ranobe import Ranobe
from shikimori.types.character import CharacterBrief
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
        List clubs.

        :param page: Must be a number between 1 and 100000.
        :param limit: 30 max.
        :param search: string.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs",
            headers=self.headers,
            params=filter_none_parameters(
                {"limit": limit, "page": page, "search": search}
            ),
        )

        if not isinstance(response, RequestError):
            return [Club.from_dict(club) for club in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> ClubInfo | RequestError:
        """
        Show a club.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return ClubInfo.from_dict(response)

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
        Update a club.

        Requires clubs oauth scope.

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
            json={
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
            return ClubInfo.from_dict(response)

        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def animes(
        self, id: int, limit: int = None, page: int = None
    ) -> List[Anime] | RequestError:
        """
        List of club animes.

        :param id: must a number.
        :param limit: 20 maximum.
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/animes",
            headers=self.headers,
            params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [Anime.from_dict(anime) for anime in response]

        logger.debug(
            f"Bad Request(GetAnimes): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def mangas(
        self, id: int, page: int = None, limit: int = None
    ) -> List[Manga] | RequestError:
        """
        List of club mangas.

        :param id: must a number.
        :param limit: 20 maximum.
        :param page: Must be a number between 1 and 100000.
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/mangas",
            headers=self.headers,
            params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [Manga.from_dict(manga) for manga in response]

        logger.debug(
            f"Bad Request(GetMangas): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ranobes(
        self, id: int, limit: int = None, page: int = None
    ) -> List[Ranobe] | RequestError:
        """
        List of club Ranobes

        :param id: must a number.
        :param limit: 20 maximum.
        :param page: Must be a number between 1 and 100000.
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/ranobe",
            headers=self.headers,
            params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [Ranobe.from_dict(ranobe) for ranobe in response]

        logger.debug(
            f"Bad Request(GetRanobes): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def characters(
        self, id: int, limit: int = None, page: int = None
    ) -> List[CharacterBrief] | RequestError:
        """
        List of club Characters.

        :param id: must a number.
        :param limit: 20 maximum.
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/characters",
            headers=self.headers,
            params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [CharacterBrief.from_dict(ch) for ch in response]

        logger.debug(
            f"Bad Request(GetCharacters): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def collections(
        self, id: int, limit: int = None, page: int = None
    ) -> List[Collection] | RequestError:
        """
        List of club Collections.

        :param id: must a number.
        :param limit: 4 maximum.
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/collections",
            headers=self.headers,
            params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [Collection.from_dict(coll) for coll in response]

        logger.debug(
            f"Bad Request(GetCollections): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def clubs(
        self, id: int, limit: int = None, page: int = None
    ) -> List[Club] | RequestError:
        """
        List of club clubs.

        :param id: must a number.
        :param limit: 30 maximum.
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/clubs",
            headers=self.headers,
            params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [Club.from_dict(c) for c in response]

        logger.debug(
            f"Bad Request(Clubs): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def members(
        self, id: int, limit: int = None, page: int = None
    ) -> List[User] | RequestError:
        """
        List of club members.

        :param id: must a number.
        :param limit: 100 maximum.
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/members",
            headers=self.headers,
            params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [User.from_dict(u) for u in response]

        logger.debug(
            f"Bad Request(Members): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def images(
        self, id: int, limit: int = None, page: int = None
    ) -> List[ClubImage] | RequestError:
        """
        List of club Images.

        :param id: must a number.
        :param limit: 100 maximum.
        :param page: Must be a number between 1 and 100000.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/clubs/{id}/images",
            headers=self.headers,
            params=filter_none_parameters({"limit": limit, "page": page}),
        )

        if not isinstance(response, RequestError):
            return [ClubImage.from_dict(s) for s in response]

        logger.debug(
            f"Bad Request(Images): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def join(self, id: int) -> None | RequestError:
        """
        Join a club.

        Requires clubs oauth scope.

        :param id: must be a number.
        """
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
        """
        Leave a club.

        Requires clubs oauth scope.

        :param id: must be a number.
        """
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
