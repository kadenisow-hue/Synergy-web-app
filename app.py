from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import datetime

app = FastAPI(title="Corporate Task Manager API")

# Схема валидации данных для веб-интерфейса
class TaskSchema(BaseModel):
    id: int
    title: str
    description: str
    status: str
    employee_id: int
    created_at: datetime.date

# Имитация базы данных в оперативной памяти (In-Memory REST API)
tasks_db = [
    {"id": 1, "title": "Разработать модуль ИИ", "description": "Обучить модель классификации", "status": "In Progress", "employee_id": 101, "created_at": datetime.date.today()},
    {"id": 2, "title": "Развернуть веб-сервер", "description": "Настроить конфигурацию IIS/Reverse Proxy", "status": "New", "employee_id": 102, "created_at": datetime.date.today()}
]

@app.get("/api/tasks", response_model=List[TaskSchema])
def get_all_tasks():
    """Веб-метод GET для получения списка всех задач"""
    return tasks_db

@app.post("/api/tasks", response_model=TaskSchema)
def create_task(task: TaskSchema):
    """Веб-метод POST для добавления новой задачи через HTTP-запрос"""
    for t in tasks_db:
        if t["id"] == task.id:
            raise HTTPException(status_code=400, detail="Задача с таким ID уже существует")
    tasks_db.append(task.dict())
    return task
