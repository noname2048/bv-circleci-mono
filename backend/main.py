# std
from datetime import datetime, timedelta, timezone

# 3rd
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

# app
from app.schemas import User
from app.services import get_users
from app.db.database import get_db, database


app = FastAPI()

kst = timezone(timedelta(hours=9))


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


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
