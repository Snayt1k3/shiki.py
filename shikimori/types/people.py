from dataclasses import dataclass
from .photo import Photo
from shikimori.types.animes import Anime
from shikimori.types.manga import Manga
from shikimori.types.character import Character


@dataclass
class Date:
    day: int
    month: int
    year: int


@dataclass
class Works:
    anime: Anime
    manga: Manga
    role: str


@dataclass
class Role:
    animes: list[Anime]
    characters: list[Character]


@dataclass
class People:
    id: int
    name: str
    russian: str
    image: Photo
    url: str
    japanese: str
    job_title: str
    birth_on: Date
    deceased_on: Date | None
    website: str
    groupped_roles: list[str | int]
    works: list[Works]
    roles: list[Role]
    topic_id: int
    person_favoured: bool
    producer: bool
    producer_favoured: bool
    mangaka: bool
    mangaka_favoured: bool
    seyu: bool
    seyu_favoured: bool
    updated_at: str
    thread_id: int
    birthday: Date
