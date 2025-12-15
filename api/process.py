from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class InputPayload(BaseModel):
    text: str

@app.post("/")
def process(payload: InputPayload):
    t = payload.text.strip()
    if not t:
        raise HTTPException(status_code=400, detail="Empty input")
    return {"result": f"Processed response: {t}"}
