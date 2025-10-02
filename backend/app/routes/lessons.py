from fastapi import APIRouter
from app.db import db
from app.schemas import Lesson

router = APIRouter(prefix="/lessons", tags=["Lessons"])

@router.get("/")
def get_lessons():
    lessons = list(db.lessons.find({}, {"_id": 0}))
    return {"lessons": lessons}

@router.post("/")
def add_lesson(lesson: Lesson):
    db.lessons.insert_one(lesson.dict())
    return {"message": "Lesson added successfully"}
