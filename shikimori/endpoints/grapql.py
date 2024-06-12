import logging

from shikimori.enums import (
    OrderEnum,
    GenreEntryTypeEnum,
    UserRateTargetTypeEnum,
    UserRateStatusEnum,
    UserRateOrderInputType,
)
from shikimori.exceptions import RequestError
from .base import BaseEndpoint

logger = logging.getLogger(__name__)


class GraphQlEndpoint(BaseEndpoint):
    async def animes(
        self,
        fields: str,
        page: int = 1,
        limit: int = 1,
        order: OrderEnum = None,
        kind: str = None,
        status: str = None,
        season: str = None,
        score: int = None,
        duration: int = None,
        rating: str = None,
        genre: str = None,
        studio: str = None,
        franchise: str = None,
        censored=True,
        mylist: str = None,
        ids: str = None,
        excludeIds: str = None,
        search: str = None,
    ) -> dict | RequestError:
        """

        :param fields: e.g. '{ anime { id name } }'  (check more in doc https://shikimori.one/api/doc/graphql )
        :param kind: List of values separated by comma. Add ! before value to apply negative filter. values: tv, movie, ova, ona, special, tv_special, music, pv, cm, tv_13, tv_24, tv_48
        :param status: List of values separated by comma. Add ! before value to apply negative filter.
        :param season: List of values separated by comma. Add ! before value to apply negative filter. Examples: summer_2017, 2016, 2014_2016, 199x
        :param score: Minimal anime score
        :param duration: List of values separated by comma. Add ! before value to apply negative filter. Examples: S - Less than 10 minutes, D - Less than 30 minutes, F - More than 30 minutes
        :param rating: List of values separated by comma. Add ! before value to apply negative filter. Examples: none - No rating, g - G - All ages, pg - PG - Children, pg_13 - PG-13 - Teens 13 or older, r - R - 17+ recommended (violence & profanity), r_plus - R+ - Mild Nudity (may also contain violence & profanity), rx - Rx - Hentai (extreme sexual content/nudity)
        :param genre: List of comma separated genre ids
        :param studio: List of comma separated studio ids
        :param franchise: List of comma separated franchises
        :param censored: Set to false to allow hentai, yaoi and yuri
        :param mylist: List of values separated by comma. Add ! before value to apply negative filter. Examples: planned - Planned to Watch, watching - Watching, rewatching - Rewatching, completed - Completed, on_hold - On Hold, dropped - Dropped
        :param ids: List of comma separated ids
        :param excludeIds: List of comma separated ids
        :param search: must be a string
        :param order: OrderEnum
        :param page: must be a number
        :param limit: Maximum 50
        """

        query = (
            """query($page: PositiveInt, $limit: PositiveInt, $order: OrderEnum, $kind: AnimeKindString, $status: AnimeStatusString, $season: SeasonString, $score: Int, $duration: DurationString, $rating: RatingString, $genre: String, $studio: String, $franchise: String, $censored: Boolean, $mylist: MylistString, $ids: String, $excludeIds: String, $search: String){
        animes(
            page: $page,
            limit: $limit,
            order: $order,
            kind: $kind,
            status: $status,
            season: $season,
            score: $score,
            duration: $duration,
            rating: $rating,
            genre: $genre,
            studio: $studio,
            franchise: $franchise,
            censored: $censored,
            mylist: $mylist,
            ids: $ids,
            excludeIds: $excludeIds,
            search: $search
        )"""
            + fields
            + "}"
        )

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/graphql",
            json={
                "query": query,
                "variables": {
                    "page": page,
                    "limit": limit,
                    "order": order.value if order else None,
                    "kind": kind,
                    "status": status,
                    "season": season,
                    "score": score,
                    "duration": duration,
                    "rating": rating,
                    "genre": genre,
                    "studio": studio,
                    "franchise": franchise,
                    "censored": censored,
                    "mylist": mylist,
                    "ids": ids,
                    "excludeIds": excludeIds,
                    "search": search,
                },
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(animes graphql): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def characters(
        self,
        fields: str,
        page: int = 1,
        limit: int = 1,
        ids: str = None,
        search: str = None,
    ) -> dict | RequestError:
        """

        :param fields: e.g. '{ anime { id name } }'  (check more in doc https://shikimori.one/api/doc/graphql )
        :param page: int
        :param limit: Maximum 50
        :param ids: list of separated ids
        :param search: str
        """

        query = (
            """
        query($page: PositiveInt, $limit: PositiveInt, $ids: [ID!], $search: String) {
          characters(
            page: $page,
            limit: $limit,
            ids: $ids,
            search: $search
          )
        """
            + fields
            + "}"
        )
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/graphql",
            json={
                "query": query,
                "variables": {
                    "page": page,
                    "limit": limit,
                    "ids": ids,
                    "search": search,
                },
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(characters graphql): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def contests(
        self, fields: str, page: int = 1, limit: int = 1, ids: str = None
    ) -> dict | RequestError:
        """
        :param fields: e.g. '{ anime { id name } }'  (check more in doc https://shikimori.one/api/doc/graphql )
        :param page: int
        :param limit: Maximum 10
        :param ids: list of separated ids
        """

        query = (
            """
        query($page: PositiveInt, $limit: PositiveInt, $ids: [ID!]) {
          contests(
            page: $page,
            limit: $limit,
            ids: $ids
            )
            """
            + fields
            + "}"
        )

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/graphql",
            json={
                "query": query,
                "variables": {
                    "page": page,
                    "limit": limit,
                    "ids": ids,
                },
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(contests graphql): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def currentUser(
        self,
        fields: str,
    ) -> dict | RequestError:
        """
        :param fields: e.g. '{ anime { id name } }'  (check more in doc https://shikimori.one/api/doc/graphql )
        """
        query = (
            """
        query {}
        """
            + fields
        )
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/graphql",
            json={
                "query": query,
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(currentUser graphql): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def genres(
        self, fields: str, entry: GenreEntryTypeEnum
    ) -> dict | RequestError:
        """
        :param fields: e.g. '{ anime { id name } }'  (check more in doc https://shikimori.one/api/doc/graphql )
        :param entry: GenreEntryTypeEnum
        """

        query = (
            """
        query ($entryType: GenreEntryTypeEnum!) {
          genres(entryType: $entryType)        
        """
            + fields
            + "}"
        )

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/graphql",
            json={
                "query": query,
                "variables": {
                    "entryType": str(entry),
                },
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(genres graphql): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def mangas(
        self,
        fields: str,
        page: int = 1,
        limit: int = 1,
        order: OrderEnum = None,
        kind: str = None,
        status: str = None,
        season: str = None,
        score: int = None,
        genre: str = None,
        publisher: str = None,
        franchise: str = None,
        censored=True,
        mylist: str = None,
        ids: str = None,
        excludeIds: str = None,
        search: str = None,
    ) -> dict | RequestError:
        """
        :param fields: e.g. '{ anime { id name } }'  (check more in doc https://shikimori.one/api/doc/graphql )
        :param publisher: List of comma separated publisher ids
        :param kind: List of values separated by comma. Add ! before value to apply negative filter. values: tv, movie, ova, ona, special, tv_special, music, pv, cm, tv_13, tv_24, tv_48
        :param status: List of values separated by comma. Add ! before value to apply negative filter.
        :param season: List of values separated by comma. Add ! before value to apply negative filter. Examples: summer_2017, 2016, 2014_2016, 199x
        :param score: Minimal anime score
        :param genre: List of comma separated genre ids
        :param franchise: List of comma separated franchises
        :param censored: Set to false to allow hentai, yaoi and yuri
        :param mylist: List of values separated by comma. Add ! before value to apply negative filter. Examples: planned - Planned to Watch, watching - Watching, rewatching - Rewatching, completed - Completed, on_hold - On Hold, dropped - Dropped
        :param ids: List of comma separated ids
        :param excludeIds: List of comma separated ids
        :param search: must be a string
        :param order: OrderEnum
        :param page: must be a number
        :param limit: Maximum 50
        """

        query = (
            """
        query ($page: PositiveInt, $limit: PositiveInt, $order: OrderEnum, $kind: MangaKindString, $status: MangaStatusString, $season: SeasonString, $score: Int, $genre: String, $publisher: String, $franchise: String, $censored: Boolean, $mylist: MylistString, $ids: String, $excludeIds: String, $search: String) {
          mangas(
            page: $page,
            limit: $limit,
            order: $order,
            kind: $kind,
            status: $status,
            season: $season,
            score: $score,
            genre: $genre,
            publisher: $publisher,
            franchise: $franchise,
            censored: $censored,
            mylist: $mylist,
            ids: $ids,
            excludeIds: $excludeIds,
            search: $search
          )
        """
            + fields
            + "}"
        )

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/graphql",
            json={
                "query": query,
                "variables": {
                    "page": page,
                    "limit": limit,
                    "order": order.value if order else None,
                    "kind": kind,
                    "status": status,
                    "season": season,
                    "score": score,
                    "genre": genre,
                    "franchise": franchise,
                    "censored": censored,
                    "mylist": mylist,
                    "ids": ids,
                    "excludeIds": excludeIds,
                    "search": search,
                    "publisher": publisher,
                },
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(mangas graphql): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def people(
        self,
        fields: str,
        page: int = 1,
        limit: int = 1,
        ids: str = None,
        search: str = None,
        isSeyu: bool = None,
        isProducer: bool = None,
        isMangaka: bool = None,
    ) -> dict | RequestError:
        """
        :param fields: e.g. '{ anime { id name } }'  (check more in doc https://shikimori.one/api/doc/graphql )
        :param page: int
        :param limit: Maximum 10
        :param ids: List of values separated by comma.
        :param search: str
        :param isSeyu: bool
        :param isProducer: bool
        :param isMangaka: bool
        """

        query = (
            """
        query ($page: PositiveInt, $limit: PositiveInt, $ids: [ID!], $search: String, $isSeyu: Boolean, $isProducer: Boolean, $isMangaka: Boolean) {
          people(
            page: $page,
            limit: $limit,
            ids: $ids,
            search: $search,
            isSeyu: $isSeyu,
            isProducer: $isProducer,
            isMangaka: $isMangaka
          )
        """
            + fields
            + "}"
        )
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/graphql",
            json={
                "query": query,
                "variables": {
                    "page": page,
                    "limit": limit,
                    "search": search,
                    "isSeyu": isSeyu,
                    "isProducer": isProducer,
                    "isMangaka": isMangaka,
                    "ids": ids,
                },
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(people graphql): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def userRates(
        self,
        fields: str,
        userId: int = None,
        page: int = 1,
        limit: int = 1,
        targetType: UserRateTargetTypeEnum = None,
        status: UserRateStatusEnum = None,
        order: UserRateOrderInputType = None,
    ) -> dict | RequestError:
        """
        :param fields: e.g. '{ anime { id name } }'  (check more in doc https://shikimori.one/api/doc/graphql )
        :param userId: ID of current user is used by default
        :param page: int
        :param limit: maximum - 50
        :param targetType: UserRateTargetTypeEnum
        :param status: UserRateStatusEnum
        :param order: UserRateOrderInputType
        """

        query = (
            """
        query ($page: PositiveInt, $limit: PositiveInt, $userId: ID, $targetType: UserRateTargetTypeEnum!, $status: UserRateStatusEnum, $order: UserRateOrderInputType) {
          userRates(
            page: $page,
            limit: $limit,
            userId: $userId,
            targetType: $targetType,
            status: $status,
            order: $order
          ) 
        """
            + fields
            + "}"
        )

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/graphql",
            json={
                "query": query,
                "variables": {
                    "page": page,
                    "limit": limit,
                    "status": status.value if status else None,
                    "userId": userId,
                    "targetType": targetType.value if targetType else None,
                    "order": (
                        {"field": order.field, "order": order.order} if order else None
                    ),
                },
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(userRates graphql): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def users(
        self,
        fields: str,
        page: int = 1,
        limit: int = 1,
        ids: str = None,
        search: str = None,
    ) -> dict | RequestError:
        """
        :param fields: e.g. '{ anime { id name } }'  (check more in doc https://shikimori.one/api/doc/graphql )
        :param page: int
        :param limit: maximum - 50
        :param ids: List of values separated by comma.
        :param search: str
        """

        query = (
            """
        query ($page: PositiveInt, $limit: PositiveInt, $ids: [ID!], $search: String) {
          users(
            page: $page,
            limit: $limit,
            ids: $ids,
            search: $search
          )
        """
            + fields
            + "}"
        )
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/graphql",
            json={
                "query": query,
                "variables": {
                    "page": page,
                    "limit": limit,
                    "search": search,
                    "ids": ids,
                },
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(users graphql): status - {response.status_code}: info - {str(response)}"
        )

        return response
