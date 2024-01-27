from dataclasses import dataclass

@dataclass
class AbuseRequest:
    kind: str
    value: bool
    affected_ids: list[int]
