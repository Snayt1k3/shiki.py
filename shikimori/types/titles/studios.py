from dataclasses import dataclass


@dataclass
class Studio:
    id: int
    name: str
    filtered_name: str
    real: bool
    image: str
