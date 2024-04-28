from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class Achievement:
    id: int
    neko_id: str
    level: int
    progress: int
    user_id: int
    created_at: str
    updated_at: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            neko_id=data.get("neko_id"),
            level=data.get("level"),
            progress=data.get("progress"),
            user_id=data.get("user_id"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )
