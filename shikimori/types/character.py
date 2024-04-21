from dataclasses import dataclass
from shikimori.types.roles import Character as Seyu
from .base import BaseRole, BaseCharacter, BaseTitle
from .photo import Photo


@dataclass
class MangaRole(BaseRole, BaseTitle):
    volumes: int
    chapters: int

    @classmethod
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
class AnimeRole(BaseRole, BaseTitle):
    episodes: int
    episodes_aired: int

    @classmethod
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

    @classmethod
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
            seyu=[Seyu.from_dict(seyu_data) for seyu_data in data.get("seyu", [])],
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
