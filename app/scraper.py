import requests

def scrape_jobs():
    url = "https://remotive.com/api/remote-jobs"
    response = requests.get(url)

    data = response.json()

    jobs = []

    for job in data["jobs"][:20]:
        jobs.append({
            "title": job["title"],
            "company": job["company_name"],
            "link": job["url"]
        })

    return jobs