import logging

from shikimori.types.constants import (
    SmileConstant,
    ClubConstant,
    AnimeConstant,
    MangaConstant,
    UserRateConstant,
)
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class ConstantsEndpoint(BaseEndpoint):
    async def animes(self) -> AnimeConstant | RequestError:
        response = await self._request.make_request(
            "GET",
            headers=self.headers,
            url=f"{self._base_url}/api/constants/anime",
        )

        if not isinstance(response, RequestError):
            return AnimeConstant.from_dict(response)

        logger.debug(
            f"Bad Request(animes): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def mangas(self) -> MangaConstant | RequestError:
        response = await self._request.make_request(
            "GET",
            headers=self.headers,
            url=f"{self._base_url}/api/constants/manga",
        )

        if not isinstance(response, RequestError):
            return MangaConstant.from_dict(response)

        logger.debug(
            f"Bad Request(manga): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def user_rates(self) -> UserRateConstant | RequestError:
        response = await self._request.make_request(
            "GET",
            headers=self.headers,
            url=f"{self._base_url}/api/constants/manga",
        )

        if not isinstance(response, RequestError):
            return UserRateConstant.from_dict(response)

        logger.debug(
            f"Bad Request(user_rate): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def clubs(self) -> ClubConstant | RequestError:
        response = await self._request.make_request(
            "GET",
            headers=self.headers,
            url=f"{self._base_url}/api/constants/manga",
        )

        if not isinstance(response, RequestError):
            return ClubConstant.from_dict(response)

        logger.debug(
            f"Bad Request(club): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def smileys(self) -> list[SmileConstant] | RequestError:
        response = await self._request.make_request(
            "GET",
            headers=self.headers,
            url=f"{self._base_url}/api/constants/smileys",
        )

        if not isinstance(response, RequestError):
            return [SmileConstant.from_dict(s) for s in response]

        logger.debug(
            f"Bad Request(smileys): status - {response.status_code}: info - {str(response)}"
        )

        return response
