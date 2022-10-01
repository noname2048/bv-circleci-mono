from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.settings import settings

Base = declarative_base()
engine = create_async_engine(settings.db_url, echo=True)
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()
