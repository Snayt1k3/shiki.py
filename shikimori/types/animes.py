from dataclasses import dataclass

from .base import BaseTitle
from .manga import Manga
from .photo import Photo
from .screenshots import ScreenShot
from .studios import Studio
from .user_rates import MiniUserRate
from .videos import Video
from ..utils.filter import handle_none_data
from .genres import GenreExtended


@dataclass
class Anime(BaseTitle):
    episodes: int
    episodes_aired: int

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            image=Photo.from_dict(data.get("image")),
            url=data.get("url"),
            kind=data.get("kind"),
            score=data.get("score"),
            status=data.get("status"),
            episodes=data.get("episodes"),
            episodes_aired=data.get("episodes_aired"),
            aired_on=data.get("aired_on"),
            released_on=data.get("released_on"),
        )


@dataclass
class AnimeInfo(Anime):
    english: list[str] | list[None]
    japanese: list[str] | list[None]
    synonyms: list[str] | list[None]
    license_name_ru: str | None
    duration: int
    description: str
    description_html: str
    description_source: str | None
    franchise: str | None
    anons: bool
    ongoing: bool
    favoured: bool
    thread_id: int
    rating: str
    topic_id: int
    myanimelist_id: int
    rates_scores_stats: list[dict]
    rates_statuses_stats: list[dict]
    updated_at: str
    next_episode_at: str | None
    fansubbers: list[dict]
    fandubbers: list[dict]
    licensors: list[dict]
    genres: list[GenreExtended]
    studios: list[Studio]
    videos: list[Video]
    screenshots: list[ScreenShot]
    user_rate: MiniUserRate

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            image=data.get("image"),
            url=data.get("url"),
            kind=data.get("kind"),
            score=data.get("score"),
            status=data.get("status"),
            episodes=data.get("episodes"),
            episodes_aired=data.get("episodes_aired"),
            aired_on=data.get("aired_on"),
            released_on=data.get("released_on"),
            rating=data.get("rating"),
            english=data.get("english"),
            japanese=data.get("japanese"),
            synonyms=data.get("synonyms"),
            license_name_ru=data.get("license_name_ru"),
            duration=data.get("duration"),
            description=data.get("description"),
            description_html=data.get("description_html"),
            description_source=data.get("description_source"),
            franchise=data.get("franchise"),
            favoured=data.get("favoured"),
            anons=data.get("anons"),
            ongoing=data.get("ongoing"),
            thread_id=data.get("thread_id"),
            topic_id=data.get("topic_id"),
            myanimelist_id=data.get("myanimelist_id"),
            rates_scores_stats=data.get("rates_scores_stats"),
            rates_statuses_stats=data.get("rates_statuses_stats"),
            updated_at=data.get("updated_at"),
            next_episode_at=data.get("next_episode_at"),
            fansubbers=data.get("fansubbers"),
            fandubbers=data.get("fandubbers"),
            licensors=data.get("licensors"),
            genres=[GenreExtended.from_dict(genre) for genre in data.get("genres", [])],
            screenshots=[ScreenShot.from_dict(s) for s in data.get("screenshots", [])],
            studios=[Studio.from_dict(s) for s in data.get("studios", [])],
            videos=[Video.from_dict(v) for v in data.get("videos", [])],
            user_rate=(
                MiniUserRate.from_dict(data.get("user_rate"))
                if data.get("user_rate")
                else None
            ),
        )


@dataclass
class Relation:
    relation: str
    relation_russian: str
    anime: Anime | None
    manga: Manga | None

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            relation=data.get("relation"),
            relation_russian=data.get("relation_russian"),
            anime=Anime.from_dict(anime) if (anime := data.get("anime")) else None,
            manga=Manga.from_dict(manga) if (manga := data.get("manga")) else None,
        )


@dataclass
class ExternalLink:
    id: int
    kind: str
    url: str
    source: str
    entry_id: int
    entry_type: str
    created_at: str
    updated_at: str
    imported_at: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            kind=data.get("kind"),
            url=data.get("url"),
            source=data.get("source"),
            entry_id=data.get("entry_id"),
            entry_type=data.get("entry_type"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            imported_at=data.get("imported_at"),
        )
