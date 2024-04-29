import logging
from typing import List

from shikimori.types.studios import Studio
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class StudiosEndpoint(BaseEndpoint):
    async def list(self) -> List[Studio] | RequestError:
        """
        List studios
        """
        response = await self._request.make_request(
            "GET", url=f"{self._base_url}/api/studios", headers=self.headers
        )

        if not isinstance(response, RequestError):
            return [Studio.from_dict(studio) for studio in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response
