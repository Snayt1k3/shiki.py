from dataclasses import dataclass


@dataclass
class ScreenShot:
    preview: str
    original: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(preview=data.get("preview"), original=data.get("original"))
