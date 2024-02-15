from dataclasses import dataclass
from shikimori.types.photo import PhotoExtended
from shikimori.types.animes import Anime
from typing import Any
from .user_rates import UserRateResponse
from shikimori.types.base import BaseTitle


@dataclass
class User:
    id: int
    nickname: str
    image: PhotoExtended
    avatar: str
    last_online_at: str
    url: str


@dataclass
class ValueObj:
    name: Any
    value: Any


@dataclass
class UserTitle:
    id: int
    grouped_id: str
    name: str
    size: int
    type: str


@dataclass
class Statuses:
    animes: list[UserTitle]
    manga: list[UserTitle]


@dataclass
class Obj:
    anime: list[ValueObj]
    manga: list[ValueObj]


@dataclass
class Stats:
    statuses: Statuses
    full_statuses: Statuses
    scores: Obj
    types: Obj
    ratings: Obj
    has_anime: bool
    has_manga: bool
    genres: list
    studios: list
    studios: list
    publishers: list
    activity: list[ValueObj]


@dataclass
class UserInfoInc(User):
    name: str | None
    sex: str | None
    full_years: int | None
    birth_on: Any | None
    locale: str


@dataclass
class UserInfo(User):
    name: str | None
    sex: str | None
    full_years: int | None
    last_online: str
    website: str
    location: str | None
    banned: bool
    about: str
    about_html: str
    common_info: list[str]
    show_comments: bool
    in_friends: bool | None
    is_ignored: bool
    stats: Stats
    style_id: int


@dataclass
class Rate(UserRateResponse):
    anime: Anime
    manga: None
    user: User


@dataclass
class FavouritesObj:
    id: int
    name: str
    russian: str
    image: str
    url: None


@dataclass
class Favourites:
    animes: list[FavouritesObj]
    mangas: list[FavouritesObj]
    ranobe: list[FavouritesObj]
    characters: list[FavouritesObj]
    mangakas: list[FavouritesObj]
    seyu: list[FavouritesObj]
    producers: list[FavouritesObj]


@dataclass
class UnreadMessages:
    message: int
    news: int
    notifications: int


@dataclass
class TitleHistory(BaseTitle):
    volumes: int | None
    chapters: int | None
    episodes: int | None
    episodes_aired: int | None


@dataclass
class HistoryObj:
    id: int
    description: str
    target: TitleHistory | None
