from pydantic import BaseModel


class AbuseRequest(BaseModel):
    kind: str
    value: bool
    affected_ids: list[int]
