from pydantic import BaseModel
from photo import Photo
from studios import Studio
from videos import Video
from screenshots import ScreenShot
from genres import Genre
from manga import Manga

class GenreExtended(Genre):
    entry_type: str

class Anime(BaseModel):
    id: int
    name: str
    russian: str
    image: Photo
    url: str
    kind: str
    score: str
    status: str
    episodes: int
    episodes_aired: int
    aired_on: str
    released_on: str

class AnimeInfo(Anime):
    english: list[str] | list[None]
    japanese: list[str] | list[None]
    synonyms: list[str] | list[None]
    license_name_ru: str | None
    description_source: str | None
    franchise: str | None
    anons: bool
    ongoing: bool
    favoured: bool
    thread_id: int
    topic_id: int
    myanimelist_id: int
    rates_score_stats: list[dict]
    rates_statuses_stats: list[dict]
    updated_at: str
    next_episode_at: str | None
    fansubbers: list[dict]
    licensors: list[dict]
    genres: list[GenreExtended]
    studios: list[Studio]
    videos: list[Video]
    screenshots: list[ScreenShot]


class Relation(BaseModel):
    relation: str
    relation_russian: str
    anime: Anime | None
    manga: Manga | None

class ExternalLink(BaseModel):
    id: int
    kind: str
    url: str
    source: str
    entry_id: int
    entry_type: str
    created_at: str
    updated_at: str

