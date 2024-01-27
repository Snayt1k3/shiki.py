from dataclasses import dataclass
from ..user.user import User


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
