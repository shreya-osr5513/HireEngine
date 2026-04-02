# HireEngine: Automated Job Aggregation & Alert System
A production-style backend system that automates job discovery, personalization, and notification using scalable architecture and real-time processing.

---

## Problem Statement:
Job seekers often->
* Manually search across multiple platforms
* Miss time-sensitive opportunities
* Lack personalized filtering

This leads to inefficiency and missed opportunities.

---

## Solution:
HireEngine builds an end-to-end automated pipeline that:

1. Continuously aggregates job listings
2. Stores structured data efficiently
3. Matches jobs with user-defined skills
4. Triggers real-time notifications via email

The system eliminates manual effort and delivers personalized, real-time job discovery.

---

## System Architecture:

```
            ┌──────────────┐
            │  Job Source  │
            │ (Remotive)   │
            └──────┬───────┘
                   │
                   ▼
          ┌──────────────────┐
          │   Scraper Layer  │
          └──────┬───────────┘
                 │
                 ▼
        ┌────────────────────┐
        │   Database Layer   │
        │ (SQLAlchemy ORM)   │
        └──────┬─────────────┘
               │
       ┌───────▼────────┐
       │ Matching Engine│
       └───────┬────────┘
               │
               ▼
     ┌────────────────────┐
     │ Notification Layer │
     │   (Email System)   │
     └───────┬────────────┘
             │
             ▼
        ┌────────────┐
        │   Users    │
        └────────────┘
```

---

## Tech Stack:

| Layer         | Technology                |
| ------------- | ------------------------- |
| Backend       | FastAPI                   |
| Language      | Python                    |
| Database      | SQLite + SQLAlchemy       |
| Scheduler     | APScheduler               |
| APIs          | REST + GraphQL            |
| Scraping      | Requests + BeautifulSoup  |
| Notifications | SMTP (Gmail App Password) |

---

## Core Components:

### 1. Scraper Layer
* Fetches real-time job data from external APIs
* Handles structured parsing and ingestion

---

### 2. Database Layer
* Normalized schema using SQLAlchemy ORM
* Enforces uniqueness constraints to prevent duplicates
* Efficient query handling

---

### 3. Matching Engine
* Performs skill-based keyword matching
* Filters relevant jobs dynamically
* Designed for extensibility (NLP-ready)

---

### 4. Scheduler (Automation Engine)
* Runs asynchronously at fixed intervals
* Ensures continuous data freshness
* Triggers downstream processes without manual input

---

### 5. Notification System
* Sends event-driven email alerts
* Ensures:

  * No duplicate notifications
  * Only newly matched jobs are sent

---

### 6. API Layer
* REST endpoints for standard operations
* GraphQL for flexible querying

```graphql
query {
  jobs {
    title
    company
    link
  }
}
```

---

## Execution Flow:
```
User Registration → Data Ingestion → Storage → Matching → Event Trigger → Notification Delivery
```

---

## Code Structure:
```
app/
├── main.py           # Application bootstrap
├── routes.py         # REST API layer
├── models.py         # ORM models
├── database.py       # DB session management
├── scraper.py        # Data ingestion
├── scheduler.py      # Background processing
├── email_utils.py    # Notification service
├── graphql_api.py    # GraphQL schema
└── ai.py             # Future extensibility
```

---

## Key Engineering Highlights:
* Event-driven architecture (scheduler-triggered workflows)
* Idempotent design (no duplicate jobs or emails)
* Clear separation of concerns across modules
* Extensible matching system (ready for ML/NLP upgrade)
* Hybrid API design (REST + GraphQL)

---

## Scalability Considerations:
* Replace SQLite with PostgreSQL
* Introduce message queue (Kafka / RabbitMQ)
* Use distributed workers for scraping
* Implement caching (Redis)
* Add authentication and rate limiting

---

## Future Enhancements:
* NLP-based semantic job matching
* Multi-source aggregation (Indeed, LinkedIn, Internshala)
* Real-time push notifications (WhatsApp / Telegram)
* Frontend dashboard
* Job expiry and lifecycle management

---

## Author:
Shreya Gupta
GitHub: https://github.com/shreya-osr5513

Live Link: https://hireengine.onrender.com
         : https://hireengine.onrender.com/docs

---

This project demonstrates backend system design, asynchronous processing, API architecture, and real-world automation at scale.
