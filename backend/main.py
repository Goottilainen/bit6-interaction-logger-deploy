from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import InteractionLog

app = FastAPI(
    title="BIT6 Interaction Logger",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


class InputPayload(BaseModel):
    text: str

class OutputPayload(BaseModel):
    result: str


@app.get("/health")
def system_health():
    return {"status": "running"}

@app.post("/process", response_model=OutputPayload)
def process_input(payload: InputPayload):
    clean_text = payload.text.strip()

    if not clean_text:
        raise HTTPException(status_code=400, detail="Input text is empty")

    # Simulated AI logic (simple + intentional)
    generated_result = f"Processed response: {clean_text}"

    db: Session = SessionLocal()
    try:
        record = InteractionLog(
            user_input=clean_text,
            system_output=generated_result
        )
        db.add(record)
        db.commit()
    finally:
        db.close()

    return {"result": generated_result}
