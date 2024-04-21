from dataclasses import dataclass
from shikimori.types.animes import Anime


@dataclass
class Calendar:
    next_episode: int
    next_episode_at: str
    duration: int
    anime: Anime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            next_episode=int(data.get("next_episode")),
            next_episode_at=data.get("next_episode_at"),
            duration=data.get("duration"),
            anime=Anime.from_dict(data.get("anime")),
        )
