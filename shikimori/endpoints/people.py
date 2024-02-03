import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.general.photo import Photo
from ..types.general.people import People, Date, Works, Role
from ..types.titles.character import Character
from ..utils.filter import filter_none_parameters
from ..types.titles.animes import Anime
from ..types.titles.manga import Manga


class PeopleEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> People | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/peoples/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return People(
                **response,
                birth_on=Date(**response["birth_on"]),
                deceased_on=Date(**response["deceased_on"]),
                birthday=Date(**response["birthday"]),
                image=Photo(**response["image"]),
                works=[
                    Works(
                        anime=Anime(
                            **work["anime"], image=Photo(**work["anime"]["image"])
                        )
                        if work.get("anime")
                        else None,
                        manga=Manga(
                            **work["manga"], image=Photo(**work["manga"]["image"])
                        )
                        if work.get("manga")
                        else None,
                        role=work["role"],
                    )
                    for work in response["works"]
                ],
                roles=[
                    Role(
                        animes=[
                            Anime(**anime, image=Photo(**anime["image"]))
                            for anime in role["animes"]
                        ],
                        characters=[
                            Character(**ch, image=Photo(**ch["image"]))
                            for ch in role["characters"]
                        ],
                    )
                    for role in response["roles"]
                ],
            )

        logging.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def search(self, id: int, type: str = None) -> list[Character] | RequestError:
        """

        :param id: number
        :param type: Must be one of: seyu, mangaka, producer.
        :return:
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/peoples/{id}",
            query_params=filter_none_parameters({"type": type}),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Character(**ch, image=Photo(**ch["image"])) for ch in response]

        logging.debug(
            f"Bad Request(search): status - {response.status_code}: info - {str(response)}"
        )

        return response
