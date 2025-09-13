import requests
from bs4 import BeautifulSoup
import json
import re

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
        "headline": item.get("name"),
        "link": item.get("url"),
        "description": None
    }
    for item in data.get("itemListElement", [])
]

# --- STEP 2: Descriptions from <ul id="cagetory">
news_list = soup.find("ul", {"id": "cagetory"})
descriptions = []
if news_list:
    for li in news_list.find_all("li", id=re.compile(r"^newslist-\d+$")):
        desc_tag = li.find("p")
        descriptions.append(desc_tag.get_text(strip=True) if desc_tag else None)

# --- STEP 3: Merge (zip ensures pairwise match, rest stays None if mismatch)
for news, desc in zip(news_items, descriptions):
    news["description"] = desc

# --- STEP 4: Print final results
for news in news_items:
    print(news)
print(len(news_items))