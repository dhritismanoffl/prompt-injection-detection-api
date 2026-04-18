from fastapi import FastAPI

from app.api.v1.routes import router as v1_router


app = FastAPI(
    title="Prompt Injection Detection API",
    description="Pre-LLM security API for detecting prompt injection, jailbreak, and data exfiltration attempts.",
    version="1.0.0"
)


# --- API Versioning ---
app.include_router(v1_router, prefix="/api/v1")


# --- Health Check ---
@app.get("/")
def root():
    return {"status": "ok"}