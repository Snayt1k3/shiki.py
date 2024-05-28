from dataclasses import dataclass
from shikimori.types.photo import PhotoExtended, Photo
from shikimori.types.animes import Anime
from typing import Any

from .manga import Manga
from shikimori.constants import SHIKIMORI_URL
from ..utils.filter import handle_none_data


@dataclass
class User:
    id: int
    nickname: str
    image: PhotoExtended
    avatar: str
    last_online_at: str
    url: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            nickname=data.get("nickname"),
            image=PhotoExtended.from_dict(data.get("image")),
            avatar=data.get("avatar"),
            last_online_at=data.get("last_online_at"),
            url=data.get("url"),
        )


@dataclass
class ValueObj:
    name: Any
    value: Any

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(name=data["name"], value=data["value"])


@dataclass
class UserTitle:
    id: int
    grouped_id: str
    name: str
    size: int
    type: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            grouped_id=data.get("grouped_id"),
            name=data.get("name"),
            size=data.get("size"),
            type=data.get("type"),
        )


@dataclass
class Statuses:
    animes: list[UserTitle]
    manga: list[UserTitle]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            animes=[
                UserTitle.from_dict(anime_data) for anime_data in data.get("anime", [])
            ],
            manga=[
                UserTitle.from_dict(manga_data) for manga_data in data.get("manga", [])
            ],
        )


@dataclass
class Obj:
    anime: list[ValueObj]
    manga: list[ValueObj]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            anime=[ValueObj.from_dict(obj_data) for obj_data in data.get("anime", [])],
            manga=[ValueObj.from_dict(obj_data) for obj_data in data.get("manga", [])],
        )


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

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            statuses=Statuses.from_dict(data.get("statuses")),
            full_statuses=Statuses.from_dict(data.get("full_statuses")),
            scores=Obj.from_dict(data.get("scores")),
            types=Obj.from_dict(data.get("types")),
            ratings=Obj.from_dict(data.get("ratings")),
            has_anime=data.get("has_anime?"),
            has_manga=data.get("has_manga?"),
            genres=data.get("genres", []),
            studios=data.get("studios", []),
            publishers=data.get("publishers", []),
            activity=[
                ValueObj.from_dict(obj_data) for obj_data in data.get("activity", [])
            ],
        )


@dataclass
class UserInfoInc(User):
    name: str | None
    sex: str | None
    full_years: int | None
    birth_on: Any | None
    locale: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            sex=data.get("sex"),
            full_years=data.get("full_years"),
            birth_on=data.get("birth_on"),
            locale=data.get("locale"),
            id=data.get("id"),
            nickname=data.get("nickname"),
            image=PhotoExtended.from_dict(data.get("image")),
            avatar=data.get("avatar"),
            last_online_at=data.get("last_online_at"),
            url=data.get("url"),
        )

    @property
    def avatar_url(self) -> str:
        return f"{SHIKIMORI_URL}{self.avatar_url}"


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

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            sex=data.get("sex"),
            full_years=data.get("full_years"),
            last_online=data.get("last_online"),
            website=data.get("website"),
            location=data.get("location"),
            banned=data.get("banned"),
            about=data.get("about"),
            about_html=data.get("about_html"),
            common_info=data.get("common_info", []),
            show_comments=data.get("show_comments"),
            in_friends=data.get("in_friends"),
            is_ignored=data.get("is_ignored"),
            stats=Stats.from_dict(data.get("stats")),
            style_id=data.get("style_id"),
            id=data["id"],
            nickname=data["nickname"],
            image=PhotoExtended.from_dict(data.get("image")),
            avatar=data["avatar"],
            last_online_at=data["last_online_at"],
            url=data["url"],
        )


@dataclass
class Rate:
    anime: Anime | None
    manga: Manga | None
    user: User
    id: int
    score: int
    status: str
    text: str
    episodes: int
    chapters: int
    volumes: int
    text_html: str
    rewatches: int

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            anime=Anime.from_dict(data.get("anime")) if data.get("anime") else None,
            manga=Manga.from_dict(data.get("manga")) if data.get("manga") else None,
            user=User.from_dict(data["user"]),
            id=data["id"],
            score=data["score"],
            status=data["status"],
            text=data["text"],
            episodes=data["episodes"],
            chapters=data["chapters"],
            volumes=data["volumes"],
            text_html=data["text_html"],
            rewatches=data["rewatches"],
        )


@dataclass
class FavouritesObj:
    id: int
    name: str
    russian: str
    image: str
    url: None

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            russian=data["russian"],
            image=data["image"],
            url=None,
        )


@dataclass
class Favourites:
    animes: list[FavouritesObj]
    mangas: list[FavouritesObj]
    ranobe: list[FavouritesObj]
    characters: list[FavouritesObj]
    mangakas: list[FavouritesObj]
    seyu: list[FavouritesObj]
    producers: list[FavouritesObj]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            animes=[
                FavouritesObj.from_dict(obj_data) for obj_data in data.get("animes", [])
            ],
            mangas=[
                FavouritesObj.from_dict(obj_data) for obj_data in data.get("mangas", [])
            ],
            ranobe=[
                FavouritesObj.from_dict(obj_data) for obj_data in data.get("ranobe", [])
            ],
            characters=[
                FavouritesObj.from_dict(obj_data)
                for obj_data in data.get("characters", [])
            ],
            mangakas=[
                FavouritesObj.from_dict(obj_data)
                for obj_data in data.get("mangakas", [])
            ],
            seyu=[
                FavouritesObj.from_dict(obj_data) for obj_data in data.get("seyu", [])
            ],
            producers=[
                FavouritesObj.from_dict(obj_data)
                for obj_data in data.get("producers", [])
            ],
        )


@dataclass
class UnreadMessages:
    messages: int
    news: int
    notifications: int

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            messages=data.get("messages"),
            news=data.get("news"),
            notifications=data.get("notifications"),
        )


@dataclass
class TitleHistory:
    id: int
    name: str
    russian: str
    image: Photo
    url: str
    kind: str
    score: str
    status: str
    aired_on: str
    released_on: str
    volumes: int | None
    chapters: int | None
    episodes: int | None
    episodes_aired: int | None

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            volumes=data.get("volumes"),
            chapters=data.get("chapters"),
            episodes=data.get("episodes"),
            episodes_aired=data.get("episodes_aired"),
            id=data["id"],
            name=data["name"],
            russian=data["russian"],
            image=Photo.from_dict(data["image"]),
            url=data["url"],
            kind=data["kind"],
            score=data["score"],
            status=data["status"],
            aired_on=data["aired_on"],
            released_on=data["released_on"],
        )


@dataclass
class HistoryObj:
    id: int
    description: str
    target: TitleHistory | None

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            description=data["description"],
            target=(
                TitleHistory.from_dict(data.get("target"))
                if data.get("target")
                else None
            ),
        )
