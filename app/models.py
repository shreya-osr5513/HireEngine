from sqlalchemy import Column, Integer, String, UniqueConstraint
from .database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String, index=True)
    link = Column(String)

    # optional (if later you add parsing)
    deadline = Column(String, default="Not specified")

    __table_args__ = (
        UniqueConstraint('title', 'company', name='unique_job'),
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    skill = Column(String)

    # prevents duplicate emails
    last_sent = Column(String, default="")