from dataclasses import dataclass
from shikimori.types.animes import Anime
from shikimori.utils.filter import handle_none_data


@dataclass
class Calendar:
    next_episode: int
    next_episode_at: str
    duration: int
    anime: Anime

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            next_episode=int(data.get("next_episode")),
            next_episode_at=data.get("next_episode_at"),
            duration=data.get("duration"),
            anime=Anime.from_dict(data.get("anime")),
        )
