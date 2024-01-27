from dataclasses import dataclass


@dataclass
class Topic:
    topic_id: str
    is_ignored: bool
