import logging
from typing import List

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.user.style import Style

logger = logging.getLogger(__name__)


class StylesEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> Style | RequestError:
        response = await self._request.make_request(
            "GET", url=f"{self._base_url}/api/styles/{id}", headers=self.headers
        )

        if not isinstance(response, RequestError):
            return Style(**response)

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def preview(self, css: str) -> Style | RequestError:
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/styles/preview",
            body={"style": {"css": css}},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Style(**response)

        logger.debug(
            f"Bad Request(preview): status - {response.status_code}: info - {str(response)}"
        )

        return response


