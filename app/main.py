from fastapi import FastAPI
from pydantic import BaseModel
from app.classifier import Classifier

app = FastAPI(title="AI Support Classifier")
classifier = Classifier()

class TextIn(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI is running! Go to /docs"}

@app.post("/predict")
def predict(data: TextIn):
    label = classifier.classify(data.text)
    return {"text": data.text, "label": label}