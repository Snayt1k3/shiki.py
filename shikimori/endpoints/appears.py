import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters


class AppearsEndpoint(BaseEndpoint):
    async def Read(self, ids: str = None) -> None | RequestError:
        """
        Mark comments or topics as read
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/appears",
            headers=self._headers(),
            body=filter_none_parameters({"ids": ids}),
        )

        if not isinstance(response, RequestError):
            return

        logging.debug(
            f"Bad Request(mark): status - {response.status_code}: info - {str(response)}"
        )

        return response
