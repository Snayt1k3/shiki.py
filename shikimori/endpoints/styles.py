import logging

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

    async def create(
        self, css: str, name: str, owner_id: int, owner_type: str
    ) -> Style | RequestError:
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/styles",
            body={
                "style": {
                    "css": css,
                    "name": name,
                    "owner_id": owner_id,
                    "owner_type": owner_type,
                }
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Style(**response)

        logger.debug(
            f"Bad Request(create): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(
        self, id: int, css: str = None, name: str = None
    ) -> Style | RequestError:
        response = await self._request.make_request(
            "PATCH",
            url=f"{self._base_url}/api/styles/{id}",
            body={
                "style": {
                    "css": css,
                    "name": name,
                }
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Style(**response)

        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )

        return response
