from fastapi import APIRouter
from app.model_manager import qa_pipeline, translate
from app.schemas import ChatRequest

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
def chat_with_ai(request: ChatRequest):
    try:
        answer = qa_pipeline({
            "question": request.question,
            "context": "This is a general knowledge and educational assistant."
        })
        translated_answer = translate(answer['answer'], request.language)
        return {"answer": translated_answer}
    except Exception as e:
        return {"error": str(e)}
