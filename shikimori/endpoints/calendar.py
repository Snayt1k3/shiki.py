import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
from typing import List
from ..utils.filter import filter_none_parameters
from shikimori.types.titles.animes import Anime
from shikimori.types.general.photo import Photo
from shikimori.types.general.calendar import Calendar


class CalendarEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def list(self, censored: bool = None) -> List[Calendar] | RequestError:
        """
        Show a calendar
        :param censored: Set to false to allow hentai, yaoi and yuri
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/calendar",
            headers={"User-Agent": self._user_agent},
            query_params=filter_none_parameters({"censored": censored}),
        )

        if not isinstance(response, RequestError):
            return [
                Calendar(
                    **b,
                    anime=Anime(**b.get("anime"), image=Photo(**b["anime"]["image"])),
                )
                for b in response
            ]

        logging.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response
