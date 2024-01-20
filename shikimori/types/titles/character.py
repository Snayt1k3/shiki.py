from pydantic import BaseModel
from shikimori.types.general.photo import Photo
from shikimori.types.titles.roles import Character as Seyu
from .base import BaseRole, BaseCharacter

class MangaRole(BaseRole):
    pass

class AnimeRole(BaseRole):
    pass

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



