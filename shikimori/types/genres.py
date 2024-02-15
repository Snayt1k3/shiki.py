from dataclasses import dataclass


@dataclass
class Genre:
    id: int
    name: str
    russian: str
    kind: str
