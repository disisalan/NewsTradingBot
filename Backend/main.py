
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import Scraper
import Analyse
import Trader
app = FastAPI()

# GET route
@app.post("/routine")
def routine():
    news=Scraper.gettingnews()
    anaslysis=Analyse.analysenews(news)
    Trader.maketrade(anaslysis)
    return {"msg":"routine Completed"}


