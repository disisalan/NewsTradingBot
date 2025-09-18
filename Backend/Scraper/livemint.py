import feedparser
from datetime import datetime, timezone, timedelta
# Livemint RSS feed (markets)
url = "https://www.livemint.com/rss/markets"
url2="https://www.livemint.com/rss/market"
feed = feedparser.parse(url)
feed2=feedparser.parse(url2)
def livemint_news():
    news_items=[]
    for entry in feed.entries:
        # Headline
        headline = entry.title.strip()
        
        # Content (summary from RSS)
        content = entry.description.strip()

    # entry.published_parsed is a time.struct_time in UTC
        pub_dt = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)

        # Define IST
        ist = timezone(timedelta(hours=5, minutes=30))

        # Convert UTC → IST
        pub_ist = pub_dt.astimezone(ist)
        date_str = pub_ist.strftime("%Y-%m-%d")
        time_str = pub_ist.strftime("%H:%M:%S")

        news_items.append({
                "date": date_str,
                "time": time_str,
                "headline": headline,
                "content": content,
                "source": "Livemint"
            })
        
    for entry in feed2.entries:
        # Headline
        headline = entry.title.strip()
        
        # Content (summary from RSS)
        content = entry.description.strip()

    # entry.published_parsed is a time.struct_time in UTC
        pub_dt = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)

        # Define IST
        ist = timezone(timedelta(hours=5, minutes=30))

        # Convert UTC → IST
        pub_ist = pub_dt.astimezone(ist)
        date_str = pub_ist.strftime("%Y-%m-%d")
        time_str = pub_ist.strftime("%H:%M:%S")

        news_items.append({
                "date": date_str,
                "time": time_str,
                "headline": headline,
                "content": content,
                "source": "Livemint"
            })
    return news_items