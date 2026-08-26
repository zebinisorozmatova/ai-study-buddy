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
