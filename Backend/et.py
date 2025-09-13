import requests
import bs4 

url = '''https://etpwaapi.economictimes.com/request?type=articlelist1&path=%2Fmarkets%2Fstocks%2Fnews'''
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://m.economictimes.com/"
}


resp = requests.get(url, headers=headers)
data = resp.json()   # directly JSON

# navigate to news
search_results = data["searchResult"]
articlelist = next(item for item in search_results if item.get("name") == "articlelist")
news_items = articlelist["data"]["news"]

# extract clean fields
articles = [
    {
        "title": item.get("title"),
        "synopsis": item.get("synopsis", ""),
        "date": item.get("date", "")
    }
    for item in news_items if "title" in item
]
print(len(articles))
for a in articles:
    print(a)
    print("_"*78)