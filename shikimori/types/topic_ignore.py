from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class Topic:
    topic_id: str
    is_ignored: bool

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(topic_id=data.get("topic_id"), is_ignored=data.get("is_ignored"))
