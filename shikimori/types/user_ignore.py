from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class UserIgnore:
    user_id: str
    is_ignored: bool

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(user_id=data.get("user_id"), is_ignored=data.get("is_ignored"))
