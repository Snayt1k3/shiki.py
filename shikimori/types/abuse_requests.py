from dataclasses import dataclass


@dataclass
class AbuseRequest:
    kind: str
    value: bool
    affected_ids: list[int]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            kind=data.get("kind"),
            value=data.get("value"),
            affected_ids=data.get("affected_ids"),
        )
