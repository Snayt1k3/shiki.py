import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.general.topics import Forum

logger = logging.getLogger(__name__)


class ForumEndpoint(BaseEndpoint):
    async def list(self) -> RequestError | list[Forum]:
        response = await self._request.make_request(
            "GET", url=f"{self._base_url}/api/forums", headers=self.headers
        )

        if not isinstance(response, RequestError):
            return [Forum(**s) for s in response]

        logger.debug(
            f"Bad Request(add): status - {response.status_code}: info - {str(response)}"
        )

        return response
