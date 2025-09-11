import asyncio
import random
import Trader

MODELS = ["Model_A", "Model_B", "Model_C"]

async def analyse_with_model(news_item, model):
    delay = random.uniform(2, 5)  # simulate AI model processing time
    await asyncio.sleep(delay)
    sentiment = random.choice(["bullish", "bearish", "neutral"])
    print(f"🔎 {model} analysed '{news_item['headline']}' in {delay:.1f}s → {sentiment}")
    return {"model": model, "sentiment": sentiment}

async def analyse_one(news_item):
    print(f"📥 Starting analysis for: {news_item['headline']}") 
    tasks = [analyse_with_model(news_item, m) for m in MODELS]

    for coro in asyncio.as_completed(tasks):  # process models independently
        result = await coro
        # Fire-and-forget trade
        asyncio.create_task(
            Trader.maketrade({
                "id": news_item["id"],
                "headline": news_item["headline"],
                "analyses": [result]
            })
        )
    print(f"✅ Finished analysis for: {news_item['headline']}")

async def analysenews(news):
    for item in news:  # ensure news are processed in order
        await analyse_one(item)
