from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="AI Service", version="1.0.0")

# Tiny sentiment lexicon for demo purposes
POSITIVE = {"good", "great", "awesome", "nice", "love", "happy", "fantastic", "cool", "excellent"}
NEGATIVE = {"bad", "terrible", "awful", "hate", "sad", "angry", "horrible", "worst"}


class TextIn(BaseModel):
    text: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(payload: TextIn):
    if not payload.text:
        raise HTTPException(status_code=400, detail="Text must not be empty")

    words = {w.strip(".,!?").lower() for w in payload.text.split()}
    score = sum(1 for w in words if w in POSITIVE) - sum(1 for w in words if w in NEGATIVE)
    label = "positive" if score > 0 else ("negative" if score < 0 else "neutral")

    return {"label": label, "score": score}
