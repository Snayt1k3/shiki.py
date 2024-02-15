from dataclasses import dataclass


@dataclass
class Achievement:
    id: int
    neko_id: str
    level: int
    progress: int
    user_id: int
    created_at: str
    updated_at: str
