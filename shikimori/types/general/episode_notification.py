from dataclasses import dataclass


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
