from pydantic import BaseModel
from ..user.user import User

class Message(BaseModel):
    id: int
    kind: str
    read: bool
    body: str
    html_body: str
    created_at: str
    linked_id: int
    linked_type: None
    linked: None


class Dialog(BaseModel):
    target_user: User
    message: Message



class MessageInfo(Message):
    sender: User
    to: User


