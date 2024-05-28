import logging
from typing import List

from shikimori.types.calendar import Calendar
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class CalendarEndpoint(BaseEndpoint):
    async def list(self, censored: bool = None) -> List[Calendar] | RequestError:
        """
        Show a calendar.

        :param censored: Set to false to allow hentai, yaoi and yuri
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/calendar",
            headers=self.headers,
            params=filter_none_parameters({"censored": censored}),
        )

        if not isinstance(response, RequestError):
            return [Calendar.from_dict(calendar) for calendar in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response
