from dataclasses import dataclass


@dataclass
class Review:
    id: int
    user_id: int
    anime_id: int
    manga_id: int
    body: str
    opinion: str
    is_written_before_release: bool
    created_at: str
    updated_at: str
    comments_count: int
    cached_votes_up: int
    cached_votes_down: int
    changed_at: str
