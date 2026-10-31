from fastapi import FastAPI
from .classifier import Classifier

app = FastAPI()
classifier = Classifier()

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/predict")
def predict(text:str):
    label = classifier.predict(text)
    return {"text":text, "label":label}