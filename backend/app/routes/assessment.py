from fastapi import APIRouter
from app.schemas import PronunciationRequest
from app.utils import cultural_example

router = APIRouter(prefix="/assessment", tags=["Assessment"])

@router.post("/pronunciation")
def assess_pronunciation(request: PronunciationRequest):
    # Placeholder since real speech recognition is done in mobile app
    return {
        "word": request.word,
        "language": request.language,
        "score": 85,
        "feedback": "Good attempt!"
    }

@router.get("/cultural-example/{language}")
def get_example(language: str):
    return {"example": cultural_example(language)}
