from dataclasses import dataclass
from shikimori.utils.filter import handle_none_data


@dataclass
class AbuseRequest:
    kind: str
    value: bool
    affected_ids: list[int]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            kind=data.get("kind"),
            value=data.get("value"),
            affected_ids=data.get("affected_ids"),
        )
