from dataclasses import dataclass
from shikimori.types.user import User
from shikimori.utils.filter import handle_none_data
from shikimori.types.comment import CommentBrief


@dataclass
class Ban:
    id: int
    user_id: int
    comment: CommentBrief
    moderator_id: int
    reason: str
    created_at: str
    duration_minutes: int
    user: User
    moderator: User

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            user_id=data.get("user_id"),
            comment=CommentBrief.from_dict(data.get("comment")),
            moderator_id=data.get("moderator_id"),
            reason=data.get("reason"),
            created_at=data.get("created_at"),
            duration_minutes=data.get("duration_minutes"),
            user=User.from_dict(data.get("user")),
            moderator=User.from_dict(data.get("moderator")),
        )
