import logging
from typing import List

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.titles.studios import Studio

logger = logging.getLogger(__name__)


class StudiosEndpoint(BaseEndpoint):
    async def list(self) -> List[Studio] | RequestError:
        response = await self._request.make_request(
            "GET", url=f"{self._base_url}/api/studios", headers=self.headers
        )

        if not isinstance(response, RequestError):
            return [Studio(**s) for s in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response
