from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .utils import TextPreprocessor
from .model import SentimentModel

app = FastAPI(title="Indo Sentiment API")

# Inisialisasi komponen
preprocessor = TextPreprocessor()
model = SentimentModel()

class RequestData(BaseModel):
    text: str

class ResponseData(BaseModel):
    original_text: str
    cleaned_text: str
    label: str
    confidence: float

@app.post("/predict", response_model=ResponseData)
async def get_prediction(data: RequestData):
    if not data.text:
        raise HTTPException(status_code=400, detail="Teks tidak boleh kosong")
    
    # 1. Preprocessing
    cleaned = preprocessor.clean_text(data.text)
    
    # 2. Inisiasi Prediksi
    prediction = model.predict(cleaned)
    
    return {
        "original_text": data.text,
        "cleaned_text": cleaned,
        "label": prediction['label'],
        "confidence": round(prediction['score'], 4)
    }

@app.get("/")
def home():
    return {"message": "IndoBERT Sentiment Analysis API is running!"}