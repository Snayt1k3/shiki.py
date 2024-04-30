from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


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

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            owner_id=data.get("owner_id"),
            owner_type=data.get("owner_type"),
            name=data.get("name"),
            css=data.get("css"),
            compiled_css=None,
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )
