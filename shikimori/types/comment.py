from dataclasses import dataclass
from shikimori.types.user import User


@dataclass
class Comment:
    id: int
    user_id: int
    commentable_id: int
    commentable_type: str
    body: str
    html_body: str
    created_at: str
    updated_at: str
    is_offtopic: bool
    is_summary: bool
    can_be_edited: bool
    user: User

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            user_id=data.get("user_id"),
            commentable_id=data.get("commentable_id"),
            commentable_type=data.get("commentable_type"),
            body=data.get("body"),
            html_body=data.get("html_body"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            is_offtopic=data.get("is_offtopic"),
            is_summary=data.get("is_summary"),
            can_be_edited=data.get("can_be_edited"),
            user=User.from_dict(data.get("user")),
        )
