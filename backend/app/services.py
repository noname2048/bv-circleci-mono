from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.models import User, Candidate


async def get_users(db: AsyncSession):
    result = (await db.scalars(select(User).order_by(User.id))).all()
    return result


async def get_recently_updated_candidates(db: AsyncSession):
    result = (
        await db.scalars(
            select(Candidate)
            .filter(Candidate.pipeline_entered_at >= datetime(2022, 9, 1))
            .order_by(Candidate.pipeline_entered_at)
        )
    ).all()

    return result
