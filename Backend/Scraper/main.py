
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import Backend.Scraper.Scraper as Scraper
import Backend.Scraper.Analyse as Analyse
import Trader
app = FastAPI()

# GET route
@app.post("/routine")
async def routine():
    news= await Scraper.gettingnews()
    return {"msg":"routine Completed"}


