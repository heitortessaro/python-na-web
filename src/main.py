from fastapi import FastAPI
from .model import Task
from sqlmodel import Session, select
from .db import create_db_and_tables, engine

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/tasks/")
async def list_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        return tasks


@app.post("/tasks/")
async def create_task(task: Task):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
