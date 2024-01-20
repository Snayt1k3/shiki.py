from pydantic import BaseModel
from shikimori.types.titles.manga import Manga
from shikimori.types.titles.animes import Anime
from shikimori.types.titles.roles import Character
from shikimori.types.user import User
from .photo import ClubImage
from .topics import Topic

class Logo(BaseModel):
    original: str
    main: str
    x96: str
    x73: str
    x48: str


class Club(BaseModel):
    id: int
    name: str
    logo: Logo
    is_censored: str
    join_policy: str
    comment_policy: str


class ClubInfo(Club):
    description: str
    description_html: str
    mangas: list[Manga]
    characters: list[Character]
    thread_id: int
    topic_id: int
    user_role: str
    style_id: int
    members: list[User]
    animes: list[Anime]
    images: list[ClubImage]

class Collection(Topic):
    pass
