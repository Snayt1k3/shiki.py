import logging

from shikimori.enums import (
    OrderEnum,
    GenreEntryTypeEnum,
    UserRateTargetTypeEnum,
    UserRateStatusEnum,
    UserRateOrderInputType,
)
from .base import BaseEndpoint

logger = logging.getLogger(__name__)


class GraphQlEndpoint(BaseEndpoint):
    async def animes(
        self,
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
    ):
        """
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

        pass

    async def characters(
        self, page: int = 1, limit: int = 1, ids: str = None, search: str = None
    ):
        """

        :param page: int
        :param limit: Maximum 50
        :param ids: list of separated ids
        :param search: str
        """
        pass

    async def contests(self, page: int = 1, limit: int = 1, ids: str = None):
        """

        :param page: int
        :param limit: Maximum 10
        :param ids: list of separated ids
        """
        pass

    async def currentUser(self):
        pass

    async def genres(self, entry: GenreEntryTypeEnum):
        pass

    async def mangas(
        self,
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
    ):
        """
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
        pass

    async def people(
        self,
        page: int = 1,
        limit: int = 1,
        ids: str = None,
        search: str = None,
        isSeyu: bool = None,
        isProducer: bool = None,
        isMangaka: bool = None,
    ):
        """

        :param page: int
        :param limit: Maximum 10
        :param ids: List of values separated by comma.
        :param search: str
        :param isSeyu: bool
        :param isProducer: bool
        :param isMangaka: bool
        """
        pass

    async def userRates(
        self,
        userId: int = None,
        page: int = 1,
        limit: int = 1,
        targetType: UserRateTargetTypeEnum = None,
        status: UserRateStatusEnum = None,
        order: UserRateOrderInputType = None,
    ):
        """

        :param userId: ID of current user is used by default
        :param page: int
        :param limit: maximum - 50
        :param targetType: UserRateTargetTypeEnum
        :param status: UserRateStatusEnum
        :param order: UserRateOrderInputType
        """
        pass

    async def users(
        self, page: int = 1, limit: int = 1, ids: str = None, search: str = None
    ):
        """

        :param page: int
        :param limit: maximum - 50
        :param ids: List of values separated by comma.
        :param search: str
        """
        pass
