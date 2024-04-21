from dataclasses import dataclass
from shikimori.types.user import User
from .message import Message


@dataclass
class Dialog:
    target_user: User
    message: Message

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            target_user=User.from_dict(data.get("target_user")),
            message=Message.from_dict(data.get("message")),
        )
