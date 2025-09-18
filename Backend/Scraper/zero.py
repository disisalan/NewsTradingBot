import requests
from bs4 import BeautifulSoup
from datetime import datetime

def zero_news():
    url = "https://pulse.zerodha.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }

    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    articles = []
    for li in soup.select("ul#news li.box.item"):
        title = li.select_one("h2.title")
        desc = li.select_one("div.desc")
        date_tag = li.select_one("span.date")
        feed = li.select_one("span.feed")

        raw_dt = date_tag.get("title") if date_tag else None
        date_str, time_str = None, None

        if raw_dt:
            dt = None
            # Try both known formats
            for fmt in ("%b %d, %Y %I:%M %p", "%I:%M %p, %d %b %Y"):
                try:
                    dt = datetime.strptime(raw_dt, fmt)
                    break
                except ValueError:
                    continue

            if dt:
                date_str = dt.strftime("%Y-%m-%d")
                time_str = dt.strftime("%H:%M:%S")

        articles.append({
            "date": date_str,
            "time": time_str,
            "headline": title.get_text(strip=True) if title else None,
            "content": desc.get_text(strip=True) if desc else None,
            "source": "Pulse Zerodha"
        })

        if len(articles) == 30:
            break

    return articles

