from pydantic import BaseModel


class AbuseRequest(BaseModel):
    kind: str | None = None
    value: bool | None = None
    affected_ids: list[int] | None = None
