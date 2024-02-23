from dataclasses import dataclass


@dataclass
class Node:
    id: int
    date: int
    name: str
    image_url: str
    url: str
    year: int | None
    kind: str
    weight: int


@dataclass
class Link:
    id: int
    source_id: int
    source: int
    target_id: int
    target: int
    weight: int
    relation: str


@dataclass
class Franchise:
    nodes: list[Node]
    links: list[Link]
    current_id: int
