from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class InputPayload(BaseModel):
    text: str

@app.post("/api/process")
def process(payload: InputPayload):
    clean_text = payload.text.strip()

    if not clean_text:
        raise HTTPException(status_code=400, detail="Empty input")

    return {
        "result": f"Processed response: {clean_text}"
    }
