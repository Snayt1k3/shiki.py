from dataclasses import dataclass
from shikimori.types.user import User
from .message import Message


@dataclass
class Dialog:
    target_user: User
    message: Message
