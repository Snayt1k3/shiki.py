from dataclasses import dataclass
from shikimori.types.user import User
from shikimori.types.topics import Linked


@dataclass
class Message:
    id: int
    kind: str
    read: bool
    body: str
    html_body: str
    created_at: str
    linked_id: int | None
    linked_type: str | None
    linked: Linked | None


@dataclass
class MessageInfo(Message):
    sender: User
    to: User
