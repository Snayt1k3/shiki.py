import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters


class FavoritesEndpoint(BaseEndpoint):
    async def add(
        self, id: int, linked_type: str, access_token: str, kind: str = None
    ) -> str | RequestError:
        """
        requires oauth scope
        :param id:
        :param linked_type: Must be one of: Anime, Manga, Ranobe, Person, Character
        :param kind: Must be one of: common, seyu, mangaka, producer, person
        :return:
        """
        url = f"{self._base_url}/api/favorites/{linked_type}/{id}"

        if kind:
            url += f"/{kind}"

        response = await self._request.make_request(
            "POST", url=url, headers=self._headers()
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logging.debug(
            f"Bad Request(add): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: int, linked_type: str) -> str | RequestError:
        """
        requires oauth scope
        :param id: number
        :param linked_type: Must be one of: Anime, Manga, Ranobe, Person, Character
        """
        url = f"{self._base_url}/api/favorites/{linked_type}/{id}"

        response = await self._request.make_request(
            "DELETE", url=url, headers=self._headers()
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logging.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def reorder(self, id: int, new_index: int = None) -> None | RequestError:
        """
        requires oauth scope
        :param id: number.
        :param new_index: number.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/favorites/{id}",
            headers=self._headers(),
            body=filter_none_parameters({"new_index": new_index}),
        )

        if not isinstance(response, RequestError):
            return

        logging.debug(
            f"Bad Request(reorder): status - {response.status_code}: info - {str(response)}"
        )

        return response
