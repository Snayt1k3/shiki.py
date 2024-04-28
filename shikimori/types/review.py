from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


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

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            user_id=data.get("user_id"),
            anime_id=data.get("anime_id"),
            manga_id=data.get("manga_id"),
            body=data.get("body"),
            opinion=data.get("opinion"),
            is_written_before_release=data.get("is_written_before_release"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            comments_count=data.get("comments_count"),
            cached_votes_up=data.get("cached_votes_up"),
            cached_votes_down=data.get("cached_votes_down"),
            changed_at=data.get("changed_at"),
        )
