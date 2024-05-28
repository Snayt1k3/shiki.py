from dataclasses import dataclass

from ..utils.filter import handle_none_data


@dataclass
class ExternalLink:
    id: int
    kind: str
    url: str
    source: str
    entry_id: int
    entry_type: str
    created_at: str
    updated_at: str
    imported_at: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            kind=data.get("kind"),
            url=data.get("url"),
            source=data.get("source"),
            entry_id=data.get("entry_id"),
            entry_type=data.get("entry_type"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            imported_at=data.get("imported_at"),
        )
