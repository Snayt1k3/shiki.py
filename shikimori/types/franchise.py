from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


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

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            date=data.get("date"),
            name=data.get("name"),
            image_url=data.get("image_url"),
            url=data.get("url"),
            year=data.get("year") if data.get("year") is not None else None,
            kind=data.get("kind"),
            weight=data.get("weight"),
        )


@dataclass
class Link:
    id: int
    source_id: int
    source: int
    target_id: int
    target: int
    weight: int
    relation: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            source_id=data.get("source_id"),
            source=data.get("source"),
            target_id=data.get("target_id"),
            target=data.get("target"),
            weight=data.get("weight"),
            relation=data.get("relation"),
        )


@dataclass
class Franchise:
    nodes: list[Node]
    links: list[Link]
    current_id: int

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            nodes=[Node.from_dict(node_data) for node_data in data.get("nodes", [])],
            links=[Link.from_dict(link_data) for link_data in data.get("links", [])],
            current_id=data.get("current_id"),
        )
