from dataclasses import dataclass
from shikimori.types.animes import Anime
from shikimori.types.character import Character
from shikimori.types.manga import Manga
from .photo import Photo
from ..utils.filter import handle_none_data


@dataclass
class Date:
    day: int = None
    month: int = None
    year: int = None

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(day=data.get("day"), month=data.get("month"), year=data.get("year"))


@dataclass
class Works:
    anime: Anime | None
    manga: Manga | None
    role: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            anime=Anime.from_dict(data.get("anime")),
            manga=Manga.from_dict(data.get("manga")),
            role=data.get("role"),
        )


@dataclass
class Role:
    animes: list[Anime]
    characters: list[Character]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            animes=[
                Anime.from_dict(anime_data) for anime_data in data.get("animes", [])
            ],
            characters=[
                Character.from_dict(char_data)
                for char_data in data.get("characters", [])
            ],
        )


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
    deceased_on: Date
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

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            image=Photo.from_dict(data.get("image")),
            url=data.get("url"),
            japanese=data.get("japanese"),
            job_title=data.get("job_title"),
            birth_on=Date.from_dict(data.get("birth_on")),
            deceased_on=Date.from_dict(data.get("deceased_on")),
            website=data.get("website"),
            groupped_roles=data.get("groupped_roles", []),
            works=[Works.from_dict(works_data) for works_data in data.get("works", [])],
            roles=[Role.from_dict(role_data) for role_data in data.get("roles", [])],
            topic_id=data.get("topic_id"),
            person_favoured=data.get("person_favoured"),
            producer=data.get("producer"),
            producer_favoured=data.get("producer_favoured"),
            mangaka=data.get("mangaka"),
            mangaka_favoured=data.get("mangaka_favoured"),
            seyu=data.get("seyu"),
            seyu_favoured=data.get("seyu_favoured"),
            updated_at=data.get("updated_at"),
            thread_id=data.get("thread_id"),
            birthday=Date.from_dict(data.get("birthday")),
        )
