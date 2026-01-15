from fastapi import FastAPI
from pydantic import BaseModel
from ppt_generator import create_ppt

app = FastAPI()

class PPTRequest(BaseModel):
    topic: str
    purpose: str
    slides: int
    tone: str

@app.get("/")
def root():
    return {"status": "Mangekyo PPTGan backend running"}

@app.post("/generate-ppt")
def generate_ppt(data: PPTRequest):
    file_path = create_ppt(
        topic=data.topic,
        purpose=data.purpose,
        slides=data.slides,
        tone=data.tone
    )
    return {
        "message": "PPT generated successfully",
        "file": file_path
    }
