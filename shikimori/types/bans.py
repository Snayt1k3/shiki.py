from dataclasses import dataclass
from shikimori.types.user import User


@dataclass
class Comment:  # todo перенести в comment.py
    id: int
    commentable_id: int
    commentable_type: str
    body: str
    user_id: int
    created_at: str
    updated_at: str
    is_offtopic: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=int(data.get("id")),
            commentable_id=data.get("commentable_id"),
            commentable_type=data.get("commentable_type"),
            body=data.get("body"),
            user_id=data.get("user_id"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            is_offtopic=data.get("is_offtopic"),
        )


@dataclass
class Ban:
    id: int
    user_id: int
    comment: Comment
    moderator_id: int
    reason: str
    created_at: str
    duration_minutes: int
    user: User
    moderator: User

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            user_id=data.get("user_id"),
            comment=Comment.from_dict(data.get("comment")),
            moderator_id=data.get("moderator_id"),
            reason=data.get("reason"),
            created_at=data.get("created_at"),
            duration_minutes=data.get("duration_minutes"),
            user=User.from_dict(data.get("user")),
            moderator=User.from_dict(data.get("moderator")),
        )
