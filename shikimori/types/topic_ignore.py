from dataclasses import dataclass


@dataclass
class Topic:
    topic_id: str
    is_ignored: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(topic_id=data.get("topic_id"), is_ignored=data.get("is_ignored"))
