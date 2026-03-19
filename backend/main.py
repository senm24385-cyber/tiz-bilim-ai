from fastapi import FastAPI
from pydantic import BaseModel
from ai_teacher import teacher_response

app = FastAPI()

class Chat(BaseModel):
    user_id: str
    message: str
    learning_score: int = 50
    weak_topics: list = []

@app.post("/chat")
def chat(data: Chat):
    result = teacher_response(
        data.user_id,
        data.message,
        data.learning_score,
        data.weak_topics
    )
    return result

@app.get("/")
def root():
    return {"status": "Tiz Bilim AI running"}
