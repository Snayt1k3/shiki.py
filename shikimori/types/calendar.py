from dataclasses import dataclass
from shikimori.types.animes import Anime


@dataclass
class Calendar:
    next_episode: int
    next_episode_at: str
    duration: int
    anime: Anime
