from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class UserRateBrief:
    id: int
    score: int
    status: str
    rewatches: int
    episodes: int
    volumes: int
    chapters: int
    text: str
    text_html: str
    created_at: str
    updated_at: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            score=data.get("score"),
            status=data.get("status"),
            rewatches=data.get("rewatches"),
            episodes=data.get("episodes"),
            volumes=data.get("volumes"),
            chapters=data.get("chapters"),
            text=data.get("text"),
            text_html=data.get("text_html"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )


@dataclass
class UserRate:
    id: int
    user_id: int
    target_id: int
    target_type: str
    score: int
    status: str
    rewatches: int
    episodes: int
    volumes: int
    chapters: int
    text: str
    text_html: str
    created_at: str
    updated_at: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            user_id=data.get("user_id"),
            id=data.get("id"),
            target_id=data.get("target_id"),
            target_type=data.get("target_type"),
            score=data.get("score"),
            status=data.get("status"),
            rewatches=data.get("rewatches"),
            episodes=data.get("episodes"),
            volumes=data.get("volumes"),
            chapters=data.get("chapters"),
            text=data.get("text"),
            text_html=data.get("text_html"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )
