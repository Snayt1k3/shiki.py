from dataclasses import dataclass

@dataclass
class Style:
    id: int
    owner_id: int
    owner_type: str
    name: str
    css: str
    compiled_css: None
    created_at: str
    updated_at: str
