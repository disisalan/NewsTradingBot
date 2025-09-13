import requests
from bs4 import BeautifulSoup

url = "https://pulse.zerodha.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")

articles = []
for li in soup.select("ul#news li.box.item"):
    title = li.select_one("h2.title")
    desc = li.select_one("div.desc")
    date = li.select_one("span.date")
    feed = li.select_one("span.feed")

    articles.append({
        "title": title.get_text(strip=True) if title else None,
        "desc": desc.get_text(strip=True) if desc else None,
        "date": date.get("title") if date else None,
        "feed": feed.get_text(strip=True).lstrip("— ") if feed else None
    })
print(articles[:5])
