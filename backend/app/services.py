from sqlalchemy.orm import session

from app.db.models import User


def get_users(db):
    return db.query(User).all()
