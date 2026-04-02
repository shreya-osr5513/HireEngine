from fastapi import FastAPI
from .database import Base, engine
from .routes import router
from strawberry.fastapi import GraphQLRouter
from .graphql_api import schema
from .scheduler import start_scheduler

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.on_event("startup")
def start_background_tasks():
    print("🚀 Starting scheduler...")
    start_scheduler()