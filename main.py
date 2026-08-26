from fastapi import FastAPI

app = FastAPI(title="AI Study Buddy")


@app.get("/")
def root():
    return {
        "message": "AI Study Buddy API is running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
from fastapi import FastAPI
from pydantic import BaseModel

from ai_service import analyze_answer

app = FastAPI(title="AI Study Buddy")


class AnswerRequest(BaseModel):
    question: str
    answer: str


@app.get("/")
def root():
    return {
        "message": "AI Study Buddy API is running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/analyze")
def analyze(request: AnswerRequest):
    return analyze_answer(
        request.question,
        request.answer
    )
