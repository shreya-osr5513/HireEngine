import strawberry
from typing import List
from .database import SessionLocal
from .models import Job

@strawberry.type
class JobType:
    title: str
    company: str
    link: str

@strawberry.type
class Query:
    @strawberry.field
    def jobs(self) -> List[JobType]:
        db = SessionLocal()
        jobs = db.query(Job).all()
        return jobs

schema = strawberry.Schema(query=Query)