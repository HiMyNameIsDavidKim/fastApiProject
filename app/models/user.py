from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship

class User(BaseModel):
    id = Column(String(20), primary_key=True)
    username = Column(String(20), nullable=False)
    pwd = Column(String(20), nullable=False)
    created_at = Column(String(20))

    rank = Column(String(20))
    point = Column(String(20))

    class Config:
        arbitrary_types_allowed = True