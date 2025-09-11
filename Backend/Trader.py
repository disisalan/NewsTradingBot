import asyncio
import random

async def maketrade(signal):
    model = signal["analyses"][0]["model"]
    sentiment = signal["analyses"][0]["sentiment"]

    delay = random.uniform(1, 4)  # trade placement time
    await asyncio.sleep(delay)
    print(f"🚀 Trade placed for '{signal['headline']}' "
          f"by {model} → {sentiment}")

    # Fire-and-forget monitor
    asyncio.create_task(monitor_trade(signal))

async def monitor_trade(signal):
    model = signal["analyses"][0]["model"]

    delay = random.uniform(3, 7)  # trade monitoring time
    await asyncio.sleep(delay)
    outcome = random.choice(["+10%", "-5%", "breakeven"])

    print(f"📊 Trade closed for '{signal['headline']}' "
          f"by {model} → {outcome}")
