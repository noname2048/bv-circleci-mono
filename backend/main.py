from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from .schemas import User
from .services import get_users
from .db.models import get_db


app = FastAPI()

kst = timezone(timedelta(hours=9))


class IndexResponse(BaseModel):
    server_time: datetime = Field(datetime(2022, 1, 1, tzinfo=kst))


@app.get("/", status_code=200, tags=["index"], response_model=IndexResponse)
async def index():
    now = datetime.now(kst)
    return IndexResponse(server_time=datetime.now(kst).replace(microsecond=0))


@app.get("/users", response_model=list[User])
async def list_user(db: Session = Depends(get_db)):
    users = get_users(db)
    return users


if __name__ == "__main__":
    import os
    from pathlib import Path

    Path(__file__).resolve().parents[1]
    import uvicorn

    uvicorn.run("main:app", reload=True)
