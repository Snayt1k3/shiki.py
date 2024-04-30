import logging
from typing import List

from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class StatsEndpoint(BaseEndpoint):
    async def list(self) -> List[int] | RequestError:
        """
        Users having at least 1 completed animes and active during last month
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/stats/active_users",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response
