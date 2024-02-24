from dataclasses import dataclass
from shikimori.types.roles import Character as Seyu
from .base import BaseRole, BaseCharacter, BaseTitle


@dataclass
class MangaRole(BaseRole, BaseTitle):
    volumes: int
    chapters: int


@dataclass
class AnimeRole(BaseRole, BaseTitle):
    episodes: int
    episodes_aired: int


@dataclass
class Character(BaseCharacter):
    altname: str
    japanese: str
    description: str
    description_html: str
    description_source: str
    favoured: bool
    thread_id: int
    topic_id: int
    updated_at: str
    seyu: list[Seyu]
    animes: list[AnimeRole]
    mangas: list[MangaRole]
