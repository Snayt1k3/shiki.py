from dataclasses import dataclass
from .photo import Photo
from ..utils.filter import handle_none_data


@dataclass
class MangaRole:
    role: str
    roles: list[str]
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
    volumes: int
    chapters: int

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            role=data.get("role"),
            roles=data.get("roles", []),
            volumes=data.get("volumes"),
            chapters=data.get("chapters"),
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            image=Photo.from_dict(data.get("image")),
            url=data.get("url"),
            kind=data.get("kind"),
            score=data.get("score"),
            status=data.get("status"),
            aired_on=data.get("aired_on"),
            released_on=data.get("released_on"),
        )


@dataclass
class AnimeRole:
    role: str
    roles: list[str]
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
    episodes: int
    episodes_aired: int

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            role=data.get("role"),
            roles=data.get("roles", []),
            episodes=data.get("episodes"),
            episodes_aired=data.get("episodes_aired"),
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            image=Photo.from_dict(data.get("image")),
            url=data.get("url"),
            kind=data.get("kind"),
            score=data.get("score"),
            status=data.get("status"),
            aired_on=data.get("aired_on"),
            released_on=data.get("released_on"),
        )


@dataclass
class CharacterBrief:
    id: int
    name: str
    russian: str
    image: Photo
    url: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            image=Photo.from_dict(data.get("image")),
            url=data.get("url"),
        )


@dataclass
class Character:
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
    seyu: list[CharacterBrief]
    animes: list[AnimeRole]
    mangas: list[MangaRole]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            altname=data.get("altname"),
            japanese=data.get("japanese"),
            description=data.get("description"),
            description_html=data.get("description_html"),
            description_source=data.get("description_source"),
            favoured=data.get("favoured"),
            thread_id=data.get("thread_id"),
            topic_id=data.get("topic_id"),
            updated_at=data.get("updated_at"),
            seyu=[
                CharacterBrief.from_dict(seyu_data)
                for seyu_data in data.get("seyu", [])
            ],
            animes=[
                AnimeRole.from_dict(anime_data) for anime_data in data.get("animes", [])
            ],
            mangas=[
                MangaRole.from_dict(manga_data) for manga_data in data.get("mangas", [])
            ],
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            image=Photo.from_dict(data.get("image")),
            url=data.get("url"),
        )
