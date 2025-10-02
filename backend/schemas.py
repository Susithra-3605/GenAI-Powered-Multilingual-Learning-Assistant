from pydantic import BaseModel
from typing import List, Optional

class Lesson(BaseModel):
    id: str
    title: str
    language: str
    content: str
    quiz: Optional[List[str]]

class QuizAnswer(BaseModel):
    question: str
    answer: str

class ChatRequest(BaseModel):
    question: str
    language: str

class PronunciationRequest(BaseModel):
    word: str
    language: str
