from dataclasses import dataclass
from ..user.user import User


@dataclass
class Message:
    id: int
    kind: str
    read: bool
    body: str
    html_body: str
    created_at: str
    linked_id: int
    linked_type: None
    linked: None


@dataclass
class Dialog:
    target_user: User
    message: Message


@dataclass
class MessageInfo(Message):
    sender: User
    to: User
