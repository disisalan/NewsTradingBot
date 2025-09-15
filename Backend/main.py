
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
    return {"msg":"routine Completed"}


