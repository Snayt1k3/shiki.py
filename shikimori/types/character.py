from pydantic import BaseModel
from .photo import Photo
from .roles import Character as Seyu
from .animes import Anime
from .manga import Manga

class MangaRole(Manga):
    role: str
    roles: list[str]

class AnimeRole(Anime):
    role: str
    roles: list[str]

class Character(BaseModel):
    id: int
    name: str
    russian: str
    image: Photo
    url: str
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



