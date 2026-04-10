import joblib
import string
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="SMS Spam Detector API")

# Load saved model and vectorizer
model = joblib.load("models/naive_bayes_model.pkl")
tfidf  = joblib.load("models/tfidf_vectorizer.pkl")

# Define input format
class Message(BaseModel):
    text: str

# Clean text function (same as notebook)
def clean_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

# Home endpoint
@app.get("/")
def home():
    return {"message": "SMS Spam Detector API is running! 🚀"}

# Prediction endpoint
@app.post("/predict")
def predict(message: Message):
    # Clean the message
    cleaned = clean_text(message.text)
    # Vectorize
    vectorized = tfidf.transform([cleaned]).toarray()
    # Predict
    prediction = model.predict(vectorized)[0]
    result = "spam" if prediction == 1 else "ham"
    return {
        "message": message.text,
        "prediction": result,
        "is_spam": bool(prediction)
    }