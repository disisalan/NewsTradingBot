import asyncio
import random

async def gettingnews():
    await asyncio.sleep(random.uniform(1, 3))  # simulate fetching time
    news = [
        {"id": 1, "headline": "Stock A surges on earnings"},
        {"id": 2, "headline": "Stock B drops amid scandal"},
        {"id": 3, "headline": "Stock C stable ahead of merger"}
    ]
    print("📰 Scraper: fetched news")
    return news
