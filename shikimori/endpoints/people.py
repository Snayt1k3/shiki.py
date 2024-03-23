import logging

from shikimori.types.animes import Anime
from shikimori.types.manga import Manga
from shikimori.types.people import People, Date, Works, Role
from shikimori.types.photo import Photo
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.base import BaseCharacter
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class PeopleEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> People | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/peoples/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return People(
                id=response["id"],
                website=response["website"],
                url=response["url"],
                updated_at=response["url"],
                russian=response["russian"],
                groupped_roles=response["groupped_roles"],
                mangaka_favoured=response["mangaka_favoured"],
                mangaka=response["mangaka"],
                thread_id=response["thread_id"],
                name=response["name"],
                japanese=response["japanese"],
                seyu_favoured=response["seyu_favoured"],
                person_favoured=response["person_favoured"],
                producer_favoured=response["producer_favoured"],
                seyu=response["seyu"],
                job_title=response["job_title"],
                producer=response["producer"],
                topic_id=response["topic_id"],
                birth_on=Date(**response["birth_on"]),
                deceased_on=Date(**response["deceased_on"]),
                birthday=Date(**response["birthday"]),
                image=Photo(**response["image"]),
                works=[
                    Works(
                        anime=(
                            Anime(
                                id=work["anime"]["id"],
                                name=work["anime"]["name"],
                                russian=work["anime"]["russian"],
                                image=Photo(**work["anime"]["image"]),
                                url=work["anime"]["url"],
                                kind=work["anime"]["kind"],
                                score=work["anime"]["score"],
                                status=work["anime"]["status"],
                                episodes=work["anime"]["episodes"],
                                episodes_aired=work["anime"]["episodes_aired"],
                                aired_on=work["anime"]["aired_on"],
                                released_on=work["anime"]["released_on"],
                            )
                            if work.get("anime")
                            else None
                        ),
                        manga=(
                            Manga(
                                id=work["manga"]["id"],
                                name=work["manga"]["name"],
                                russian=work["manga"]["russian"],
                                image=Photo(**work["manga"]["image"]),
                                url=work["manga"]["url"],
                                kind=work["manga"]["kind"],
                                score=work["manga"]["score"],
                                status=work["manga"]["status"],
                                chapters=work["manga"]["chapters"],
                                volumes=work["manga"]["volumes"],
                                aired_on=work["manga"]["aired_on"],
                                released_on=work["manga"]["released_on"],
                            )
                            if work.get("manga")
                            else None
                        ),
                        role=work["role"],
                    )
                    for work in response["works"]
                ],
                roles=[
                    Role(
                        animes=[
                            Anime(
                                id=anime["id"],
                                name=anime["name"],
                                russian=anime["russian"],
                                image=Photo(**anime["image"]),
                                url=anime["url"],
                                kind=anime["kind"],
                                score=anime["score"],
                                status=anime["status"],
                                episodes=anime["episodes"],
                                episodes_aired=anime["episodes_aired"],
                                aired_on=anime["aired_on"],
                                released_on=anime["released_on"],
                            )
                            for anime in role["animes"]
                        ],
                        characters=[
                            BaseCharacter(
                                image=Photo(**s["image"]),
                                id=s["id"],
                                name=s["name"],
                                russian=s["russian"],
                                url=s["url"],
                            )
                            for s in role["characters"]
                        ],
                    )
                    for role in response["roles"]
                ],
            )

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def search(
        self, id: int, type: str = None
    ) -> list[BaseCharacter] | RequestError:
        """

        :param id: number
        :param type: Must be one of: seyu, mangaka, producer.
        :return:
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/peoples/{id}",
            params=filter_none_parameters({"type": type}),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                BaseCharacter(
                    id=ch["id"],
                    russian=ch["russian"],
                    url=ch["url"],
                    name=ch["name"],
                    image=Photo(**ch["image"]),
                )
                for ch in response
            ]

        logger.debug(
            f"Bad Request(search): status - {response.status_code}: info - {str(response)}"
        )

        return response
