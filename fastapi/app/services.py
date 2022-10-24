from datetime import datetime, timedelta
from dateutil import tz

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.models import User, Candidate


kst = tz.gettz("Asia/Seoul")


async def get_users(db: AsyncSession):
    result = (await db.scalars(select(User).order_by(User.id))).all()
    return result


async def get_recently_updated_candidates(db: AsyncSession):
    result = (
        await db.scalars(
            select(Candidate)
            .filter(
                Candidate.pipeline_entered_at
                >= (datetime.now(tz=kst) - timedelta(days=7))
            )
            .order_by(Candidate.pipeline_entered_at)
        )
    ).all()

    return result
