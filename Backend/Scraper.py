import asyncio
import random
import livemint
import mc
import et
import zero
import json

def gettingnews():
    # await asyncio.sleep(random.uniform(1, 3))  # simulate fetching time
    news=[]
    print("📰 Scraper: Trying Livemint")
    mint=livemint.livemint_news()
    print(f"GOt {len(mint)} from livemint")
    print("📰 Scraper: Trying Money Control")
    money=mc.mc_news()
    print(f"GOt {len(money)} from Money Control")
    print("📰 Scraper: Trying Economic Times")
    times=et.et_news()
    print(f"GOt {len(times)} from Money Control")
    print("📰 Scraper: Trying Zerodha Pulse")
    z=zero.zero_news()
    print(f"GOt {len(z)} from Zerodha Pulse")
    news=mint+money+times+z
    print(len(news),"GOt news")
    with open("news.txt", "w", encoding="utf-8") as f:
        json.dump(news, f, indent=4, ensure_ascii=False)   # indent=4 makes it pretty
gettingnews()