from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.db.database import Base


class User(Base):
    __tablename__ = "core_user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
