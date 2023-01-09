from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    pwd: str
    created_at: str

    rank: str
    point: str

    class Config:
        orm_mode = True

class UserList(User):
    users: List[User] = []