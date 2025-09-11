
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import Scraper
import Analyse
import Trader
app = FastAPI()

# GET route
@app.post("/routine")
async def routine():
    news= await Scraper.gettingnews()
    anaslysis= await Analyse.analysenews(news)
    signal= await Trader.maketrade(anaslysis)
    return {"msg":"routine Completed"}


