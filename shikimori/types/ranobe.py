from shikimori.types.genres import Genre
from shikimori.types.photo import Photo
from shikimori.types.user_rates import UserRate
from dataclasses import dataclass

from ..utils.filter import handle_none_data


@dataclass
class Ranobe:
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
class RanobeInfo:
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
    english: list[str]
    japanese: list[str]
    synonyms: list[str]
    license_name_ru: str
    description: str
    description_html: str
    description_source: str | None
    franchise: str
    favoured: bool
    anons: bool
    ongoing: bool
    thread_id: int
    topic_id: int
    myanimelist_id: int
    rates_scores_stats: list[dict]
    rates_statuses_stats: list[dict]
    licensors: list[str]
    genres: list[Genre]
    user_rate: dict | None

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            english=data.get("english", []),
            japanese=data.get("japanese", []),
            synonyms=data.get("synonyms", []),
            license_name_ru=data.get("license_name_ru"),
            description=data.get("description"),
            description_html=data.get("description_html"),
            description_source=data.get("description_source"),
            franchise=data.get("franchise"),
            favoured=data.get("favoured"),
            anons=data.get("anons"),
            ongoing=data.get("ongoing"),
            thread_id=data.get("thread_id"),
            topic_id=data.get("topic_id"),
            myanimelist_id=data.get("myanimelist_id"),
            rates_scores_stats=data.get("rates_scores_stats", []),
            rates_statuses_stats=data.get("rates_statuses_stats", []),
            licensors=data.get("licensors", []),
            genres=[
                Genre.from_dict(genre_data) for genre_data in data.get("genres", [])
            ],
            user_rate=(
                UserRate.from_dict(data.get("user_rate"))
                if data.get("user_rate")
                else None
            ),
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
