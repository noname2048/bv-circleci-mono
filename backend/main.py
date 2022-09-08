from datetime import datetime, timedelta, timezone

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

kst = timezone(timedelta(hours=9))


class IndexResponse(BaseModel):
    server_time: datetime = Field(datetime(2022, 1, 1, tzinfo=kst))


@app.get("/", status_code=200, tags=["index"], response_model=IndexResponse)
def index():
    now = datetime.now(kst)
    return IndexResponse(server_time=datetime.now(kst).replace(microsecond=0))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
