from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy import Table, MetaData

from app.db.database import Base


class User(Base):
    __tablename__ = "core_user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True, nullable=False)


class Candidate(Base):
    __tablename__ = "candidates_candidate"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    pipeline_entered_at = Column(DateTime)
