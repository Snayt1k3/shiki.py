from dataclasses import dataclass
from shikimori.types.animes import Anime


@dataclass
class Calendar:
    next_episode: int
    duration: int
    anime: Anime
    url: str
    kind: str
    score: str
    status: str
    episodes: int
    episodes_aired: int
    aired_on: str | None
    released_on: str | None
