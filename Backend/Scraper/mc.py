import requests
from bs4 import BeautifulSoup, Comment
import json, re
from datetime import datetime

def mc_news():
    url = "https://www.moneycontrol.com/news/business/stocks/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # --- STEP 1: JSON-LD (headlines, links)
    ld_json_blocks = soup.find_all("script", {"type": "application/ld+json"})
    if not ld_json_blocks:
        raise ValueError("No JSON-LD found")

    ld_json = ld_json_blocks[-1]
    data = json.loads(ld_json.string)

    news_items = [
        {
            "date": None,
            "time": None,
            "headline": item.get("name"),
            "content": None
        }
        for item in data.get("itemListElement", [])
    ]

    # --- STEP 2: Descriptions + Dates from <ul id="cagetory">
    news_list = soup.find("ul", {"id": "cagetory"})
    descriptions, dates, times = [], [], []
    if news_list:
        for li in news_list.find_all("li", id=re.compile(r"^newslist-\d+$")):
            # Description
            desc_tag = li.find("p")
            descriptions.append(desc_tag.get_text(strip=True) if desc_tag else None)

            # Date/Time (inside comment span)
            dt_str = None
            comments = li.find_all(string=lambda text: isinstance(text, Comment))
            for c in comments:
                if "IST" in c:
                    dt_str = re.sub(r"</?span>", "", c).strip()
                    break

            if dt_str:
                try:
                    # Parse raw string into datetime object
                    dt = datetime.strptime(dt_str, "%B %d, %Y %I:%M %p IST")
                    dates.append(dt.strftime("%Y-%m-%d"))
                    times.append(dt.strftime("%H:%M:%S"))
                except ValueError:
                    dates.append(None)
                    times.append(None)
            else:
                dates.append(None)
                times.append(None)

    # --- STEP 3: Merge everything
    for news, desc, d, t in zip(news_items, descriptions, dates, times):
        news["content"] = desc
        news["date"] = d
        news["time"] = t
        news["source"] = "Money Control"

    return news_items
