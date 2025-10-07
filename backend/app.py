import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

AI_URL = os.getenv("AI_URL", "http://ai-service:9000")
app = FastAPI(title="Backend Service", version="1.0.0")


class TextIn(BaseModel):
    text: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/api/hello")
async def hello():
    return {"message": "Hello, this is Priacc Innovations!"}


@app.post("/api/sentiment")
async def sentiment(payload: TextIn):
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.post(f"{AI_URL}/predict", json=payload.model_dump())
            r.raise_for_status()
            return r.json()
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"AI call failed: {e}")
