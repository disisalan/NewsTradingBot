
import livemint
import mc
import et
import zero

from dotenv import load_dotenv
import os
import psycopg2 
# import json

envfile=".env"
load_dotenv(envfile)

def get_connection():
    """Create and return a PostgreSQL connection"""
    return psycopg2.connect(os.getenv("DATABASE_URL"))
    
def save_news(news_items):
    """Insert a list of news items into the DB (skip duplicates)"""
    conn = get_connection()
    cur = conn.cursor()

    for item in news_items:
        cur.execute(
            """
            INSERT INTO news (date, time, headline, content, source)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (date, time, source) DO NOTHING;
            """,
            (
                item.get("date",'1970-01-01'),
                item.get("time",'12:30:30'),
                item.get("headline",""),
                item.get("content",""),
                item.get("source","Error"),
            ),
        )

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Tried saving {len(news_items)} items (duplicates skipped automatically)")


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
    # with open("news.json", "x") as f:  # "x" mode = create, fail if exists
    #     json.dump(news, f, indent=4)
    save_news(news)
gettingnews()