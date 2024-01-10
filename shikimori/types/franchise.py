from pydantic import BaseModel

class Node(BaseModel):
    id: int
    date: int
    name: str
    image_url: str
    url: str
    year: int | None
    kind: str
    weight: int

class Link(BaseModel):
    id: int
    source_id: int
    target_id: int
    target: int
    weight: int
    relation: str


class Franchise(BaseModel):
    nodes: list[Node]
    links: list[Link]



