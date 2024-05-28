import logging

from shikimori.types.style import Style
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class StylesEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> Style | RequestError:
        """
        Show a style.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET", url=f"{self._base_url}/api/styles/{id}", headers=self.headers
        )

        if not isinstance(response, RequestError):
            return Style.from_dict(response)

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def preview(self, css: str) -> Style | RequestError:
        """
        Preview a style.

        :param css: Must be a String
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/styles/preview",
            json={"style": {"css": css}},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Style.from_dict(response)

        logger.debug(
            f"Bad Request(preview): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def create(
        self, css: str, name: str, owner_id: int, owner_type: str
    ) -> Style | RequestError:
        """
        Create a style.

        :param css: Must be a String
        :param name: Must be a String
        :param owner_id: Must be a number.
        :param owner_type: Must be one of: User, Club.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/styles",
            json={
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
            return Style.from_dict(response)

        logger.debug(
            f"Bad Request(create): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(
        self, id: int, css: str = None, name: str = None
    ) -> Style | RequestError:
        """
        Update a style.

        :param id: Must be a number
        :param css: Must be a String
        :param name: Must be a String
        """
        response = await self._request.make_request(
            "PATCH",
            url=f"{self._base_url}/api/styles/{id}",
            json={
                "style": {
                    "css": css,
                    "name": name,
                }
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Style.from_dict(response)

        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )

        return response
