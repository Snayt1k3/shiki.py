from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class EpisodeNotification:
    id: int
    anime_id: int
    episode: int
    is_raw: bool
    is_subtitles: bool
    is_fandub: bool
    is_anime365: bool
    topic_id: bool

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            anime_id=data.get("anime_id"),
            episode=data.get("episode"),
            is_raw=data.get("is_raw"),
            is_subtitles=data.get("is_subtitles"),
            is_fandub=data.get("is_fandub"),
            is_anime365=data.get("is_anime365"),
            topic_id=data.get("topic_id"),
        )
