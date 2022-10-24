from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True


class Candidate(BaseModel):
    id: int
    email: str
    pipeline_entered_at: datetime
