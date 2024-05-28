import logging

from shikimori.types.people import People
from .base import BaseEndpoint
from ..exceptions import RequestError
from shikimori.types.character import CharacterBrief
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class PeopleEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> People | RequestError:
        """
        Show a person.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/peoples/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return People.from_dict(response)

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def search(
        self, id: int, type: str = None
    ) -> list[CharacterBrief] | RequestError:
        """
        Search people.

        :param id: must be a number.
        :param type: Must be one of: seyu, mangaka, producer.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/peoples/{id}",
            params=filter_none_parameters({"type": type}),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [CharacterBrief.from_dict(ch) for ch in response]

        logger.debug(
            f"Bad Request(search): status - {response.status_code}: info - {str(response)}"
        )

        return response
