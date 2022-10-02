from sqlalchemy.orm import session
from sqlalchemy.future import select

from app.db.models import User


async def get_users(db):
    result = (await db.scalars(select(User).order_by(User.id))).all()
    return result
