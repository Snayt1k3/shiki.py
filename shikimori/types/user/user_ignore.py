from dataclasses import dataclass

@dataclass
class UserIgnore:
    user_id: str
    is_ignored: bool
