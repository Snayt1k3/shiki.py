from pydantic import BaseModel
from shikimori.types.user import User


class Comment(BaseModel):
    id: int
    commentable_id: int
    commentable_type: str
    body: str
    user_id: int
    created_at: str
    updated_at: str
    is_offtopic: bool


class Ban(BaseModel):
    id: int
    user_id: int
    comment: Comment
    moderator_id: int
    reason: str
    created_at: str
    duration_minutes: int
    user: User
    moderator: User
