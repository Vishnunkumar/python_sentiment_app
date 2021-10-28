from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

app = FastAPI()

class Text(BaseModel):
    input_text: str

@app.get("/")
def home(request: Request):
    return "App is working"

@app.post("/sentiment/")
async def get_sentiment(text: Text):
    try:
        text_dict = text.dict()
        sentence = text_dict['input_text']
        vs = analyzer.polarity_scores(sentence)

        return str(vs['compound'])

    except Exception as e2:
        return str(e2)
