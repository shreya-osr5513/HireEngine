from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Job, User
from .email_utils import send_email


def job_alert():
    print("Running scheduled job...")

    db: Session = SessionLocal()

    users = db.query(User).all()
    jobs = db.query(Job).all()

    for user in users:
        matched_jobs = []
        already_sent = user.last_sent.split(",") if user.last_sent else []

        for job in jobs:
            if any(word in job.title.lower() for word in user.skill.lower().split()):
                if str(job.id) not in already_sent:
                    matched_jobs.append(job)

        if matched_jobs:
            print(f"📧 Sending email to {user.email}")
            message_lines = []
            for job in matched_jobs[:5]:
                message_lines.append(
                    f"""
🔹 Role: {job.title}
Company: {job.company}
Apply: {job.link}
Deadline: {job.deadline}
-------------------------
"""
                )

            message = "\n".join(message_lines)

            send_email(
                user.email,
                "New Job Alerts Just For You!",
                f"Hey!\n\nHere are jobs matching your skill ({user.skill}):\n\n{message}\n\nGood luck 💪\n ~By Shreya Gupta"
            )

            new_ids = [str(j.id) for j in matched_jobs]
            user.last_sent = ",".join(already_sent + new_ids)

            db.commit()

    db.close()


def start_scheduler():
    scheduler = BackgroundScheduler()

    scheduler.add_job(job_alert, "interval", seconds=30)

    scheduler.start()
    print(" Scheduler started...")