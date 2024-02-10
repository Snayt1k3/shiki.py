from dataclasses import dataclass
from shikimori.types.user.user import User
from ..general.topics import Linked


@dataclass
class Message:
    id: int
    kind: str
    read: bool
    body: str
    html_body: str
    created_at: str
    linked_id: int
    linked_type: str
    linked: Linked


@dataclass
class MessageInfo(Message):
    sender: User
    to: User
