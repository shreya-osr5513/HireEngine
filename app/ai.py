def score_job(job, user_skill):
    score = 0

    user_skill = user_skill.lower()
    title = job.title.lower()
    company = job.company.lower()

    if user_skill in title:
        score += 3

    for word in user_skill.split():
        if word in title:
            score += 2
        if word in company:
            score += 1

    return score


def recommend_jobs(jobs, user_skill):
    scored_jobs = []

    for job in jobs:
        score = score_job(job, user_skill)
        scored_jobs.append((job, score))

    scored_jobs.sort(key=lambda x: x[1], reverse=True)

    result = [job for job, score in scored_jobs if score > 0]

    if not result:
        return [job for job, _ in scored_jobs[:5]]

    return result


def analyze_job(job):
    return {
        "title": job.title,
        "company": job.company,
        "category": "Backend" if "engineer" in job.title.lower() else "General",
        "insight": "High demand role"
    }