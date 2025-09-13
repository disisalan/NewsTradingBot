import feedparser
from datetime import datetime

# Livemint RSS feed (markets)
url = "https://www.livemint.com/rss/markets"

feed = feedparser.parse(url)

for entry in feed.entries:
    # Headline
    headline = entry.title.strip()
    
    # Content (summary from RSS)
    content = entry.description.strip()
    
    # Date and time (converted to standard format)
    pub_date = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d %H:%M:%S")
    
    print("Headline:", headline)
    print("Content:", content)
    print("Published:", pub_date)
    print("-" * 80)
