from .base import BaseTitle
from shikimori.types.genres import Genre
from dataclasses import dataclass


@dataclass
class Ranobe(BaseTitle):
    volumes: int
    chapters: int


@dataclass
class RanobeInfo(Ranobe):
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