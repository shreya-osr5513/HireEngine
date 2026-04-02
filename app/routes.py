from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Job
from .scraper import scrape_jobs
from .ai import recommend_jobs, analyze_job
from .models import User

router = APIRouter()
# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home route
@router.get("/")
def home():
    return {"message": "Backend is running 🚀"}

# Get all jobs
@router.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    return [
        {
            "title": job.title,
            "company": job.company,
            "link": job.link
        }
        for job in jobs
    ]

# Scrape and store jobs 
@router.get("/scrape")
def scrape_and_store(db: Session = Depends(get_db)):
    jobs = scrape_jobs()
    count = 0

    for j in jobs:
        exists = db.query(Job).filter_by(
            title=j["title"],
            company=j["company"]
        ).first()

        if not exists:
            job = Job(
                title=j["title"],
                company=j["company"],
                link=j["link"]
            )
            db.add(job)
            count += 1

    db.commit()

    return {"message": "Jobs stored", "new_jobs_added": count}

# AI Recommendation
@router.get("/recommend")
def recommend(skill: str, db: Session = Depends(get_db)):
    jobs = db.query(Job).all()

    recommended = recommend_jobs(jobs, skill)

    return [
        {
            "title": job.title,
            "company": job.company,
            "link": job.link
        }
        for job in recommended
    ]

# AI Analysis (Agent-like behavior)
@router.get("/analyze")
def analyze(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()

    return [analyze_job(job) for job in jobs[:5]]

# register emails
from pydantic import BaseModel
class UserCreate(BaseModel):
    email: str
    skill: str
@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(email=user.email, skill=user.skill)
    db.add(new_user)
    db.commit()
    return {"message": "User registered"}