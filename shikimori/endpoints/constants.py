import logging
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
from ..types.general.constants import (
    SmileConstant,
    ClubConstant,
    AnimeConstant,
    MangaConstant,
    UserRateConstant,
)


class ConstantsEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def animes(self) -> AnimeConstant | RequestError:
        response = await self._request.make_request(
            "GET",
            headers=self.base_headers(),
            url=f"{self._base_url}/api/constants/anime",
        )

        if not isinstance(response, RequestError):
            return AnimeConstant(**response)

        logging.debug(
            f"Bad Request(animes): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def mangas(self) -> MangaConstant | RequestError:
        response = await self._request.make_request(
            "GET",
            headers=self.base_headers(),
            url=f"{self._base_url}/api/constants/manga",
        )

        if not isinstance(response, RequestError):
            return MangaConstant(**response)

        logging.debug(
            f"Bad Request(manga): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def UserRates(self) -> UserRateConstant | RequestError:
        response = await self._request.make_request(
            "GET",
            headers=self.base_headers(),
            url=f"{self._base_url}/api/constants/manga",
        )

        if not isinstance(response, RequestError):
            return UserRateConstant(**response)

        logging.debug(
            f"Bad Request(user_rate): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def clubs(self) -> ClubConstant | RequestError:
        response = await self._request.make_request(
            "GET",
            headers=self.base_headers(),
            url=f"{self._base_url}/api/constants/manga",
        )

        if not isinstance(response, RequestError):
            return ClubConstant(**response)

        logging.debug(
            f"Bad Request(club): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def smileys(self) -> list[SmileConstant] | RequestError:
        response = await self._request.make_request(
            "GET",
            headers=self.base_headers(),
            url=f"{self._base_url}/api/constants/smileys",
        )

        if not isinstance(response, RequestError):
            return [SmileConstant(**s) for s in response]

        logging.debug(
            f"Bad Request(smileys): status - {response.status_code}: info - {str(response)}"
        )

        return response
