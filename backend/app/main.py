from fastapi import FastAPI
from app.routes import lessons, chat, assessment

app = FastAPI(title="Multilingual Learning Assistant")

# Include routers
app.include_router(lessons.router)
app.include_router(chat.router)
app.include_router(assessment.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Multilingual Learning Assistant"}
