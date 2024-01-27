from dataclasses import dataclass
from shikimori.types.user import User

@dataclass
class Comment:
    id: int
    commentable_id: int
    commentable_type: str
    body: str
    user_id: int
    created_at: str
    updated_at: str
    is_offtopic: bool

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
