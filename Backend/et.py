import requests
from datetime import datetime

def et_news():
    url = '''https://etpwaapi.economictimes.com/request?type=articlelist1&path=%2Fmarkets%2Fstocks%2Fnews'''
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    resp = requests.get(url, headers=headers)
    data = resp.json()

    # navigate to news
    search_results = data["searchResult"]
    articlelist = next(item for item in search_results if item.get("name") == "articlelist")
    news_items = articlelist["data"]["news"]

    articles = []
    for item in news_items:
        if "title" not in item:
            continue

        raw_dt = item.get("date", "").strip()
        date_str, time_str = None, None

        if raw_dt:
            try:
                # e.g. "15 Sep 2025, 15:36"
                dt = datetime.strptime(raw_dt, "%d %b %Y, %H:%M")
                date_str = dt.strftime("%Y-%m-%d")
                time_str = dt.strftime("%H:%M:%S")
            except ValueError:
                pass

        articles.append({
            "date": date_str,
            "time": time_str,
            "headline": item.get("title"),
            "content": item.get("synopsis", ""),
            "source":"Economic Times"
        })
    return articles

