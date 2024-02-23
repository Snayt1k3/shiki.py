from dataclasses import dataclass
from .studios import Studio
from .videos import Video
from .screenshots import ScreenShot
from .genres import Genre
from .manga import Manga
from .base import BaseTitle
from .user_rates import MiniUserRate


@dataclass
class GenreExtended(Genre):
    entry_type: str


@dataclass
class Anime(BaseTitle):
    episodes: int
    episodes_aired: int


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


@dataclass
class Relation:
    relation: str
    relation_russian: str
    anime: Anime | None
    manga: Manga | None


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
