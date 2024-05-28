from dataclasses import dataclass
from shikimori.types.user import User
from shikimori.types.topics import Linked
from shikimori.utils.filter import handle_none_data


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

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            kind=data.get("kind"),
            read=data.get("read"),
            body=data.get("body"),
            html_body=data.get("html_body"),
            created_at=data.get("created_at"),
            linked_id=data.get("linked_id"),
            linked_type=data.get("linked_type"),
            linked=Linked.from_dict(data.get("linked")) if data.get("linked") else None,
        )


@dataclass
class MessageInfo:
    id: int
    kind: str
    read: bool
    body: str
    html_body: str
    created_at: str
    linked_id: int | None
    linked_type: str | None
    linked: Linked | None
    sender: User
    to: User

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            kind=data.get("kind"),
            read=data.get("read"),
            body=data.get("body"),
            html_body=data.get("html_body"),
            created_at=data.get("created_at"),
            linked_id=data.get("linked_id"),
            linked_type=data.get("linked_type"),
            linked=Linked.from_dict(data.get("linked")) if data.get("linked") else None,
            sender=User.from_dict(data.get("from")),
            to=User.from_dict(data.get("to")),
        )
