# std
from datetime import datetime, timedelta, timezone

# 3rd
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# app
from app.schemas import User, Candidate
from app.services import get_users, get_recently_updated_candidates
from app.db.database import get_db


app = FastAPI()

kst = timezone(timedelta(hours=9))


class IndexResponse(BaseModel):
    server_time: datetime = Field(datetime(2022, 1, 1, tzinfo=kst))


@app.get("/", status_code=200, tags=["index"], response_model=IndexResponse)
async def index():
    now = datetime.now(kst)
    return IndexResponse(server_time=datetime.now(kst).replace(microsecond=0))


@app.get("/users", response_model=list[User])
async def list_user(db: AsyncSession = Depends(get_db)):
    users = await get_users(db)
    return users


@app.get("/candidates")  # , response_model=list[Candidate])
async def list_candidate(db: AsyncSession = Depends(get_db)):
    candidates = await get_recently_updated_candidates(db)
    return candidates


if __name__ == "__main__":
    import os
    from pathlib import Path

    Path(__file__).resolve().parents[1]
    import uvicorn

    uvicorn.run("main:app", reload=True)
