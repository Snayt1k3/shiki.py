from dataclasses import dataclass


@dataclass
class UserIgnore:
    user_id: str
    is_ignored: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(user_id=data.get("user_id"), is_ignored=data.get("is_ignored"))
