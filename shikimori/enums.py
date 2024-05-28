import dataclasses
from enum import Enum


class OrderEnum(Enum):
    ID = "id"
    ID_DESC = "id_desc"
    RANKED = "ranked"
    KIND = "kind"
    POPULARITY = "popularity"
    NAME = "name"
    AIRED_ON = "aired_on"
    EPISODES = "episodes"
    STATUS = "status"
    RANDOM = "random"
    RANKED_RANDOM = "ranked_random"
    RANKED_SHIKI = "ranked_shiki"
    CREATED_AT = "created_at"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self):
        return self.value


class GenreEntryTypeEnum(Enum):
    ANIME = "Anime"
    MANGA = "Manga"

    def __str__(self):
        return self.value


class UserRateTargetTypeEnum(Enum):
    ANIME = "Anime"
    MANGA = "Manga"

    def __str__(self):
        return self.value


class UserRateStatusEnum(Enum):
    PLANNED = "planned"
    WATCHING = "watching"
    REWATCHING = "rewatching"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    DROPPED = "dropped"

    def __str__(self):
        return self.value


class UserRateOrderFieldEnum(Enum):
    ID = "id"
    UPDATED_AT = "updated_at"


class SortOrderEnum(Enum):
    ASC = "asc"
    DESC = "desc"


@dataclasses.dataclass
class UserRateOrderInputType:
    field: UserRateOrderFieldEnum
    order: SortOrderEnum
