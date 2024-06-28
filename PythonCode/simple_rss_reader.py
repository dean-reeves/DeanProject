# simple_rss_reader.py
import feedparser

def parse_rss_feed(url):
    feed = feedparser.parse(url)
    return feed.entries

if __name__ == "__main__":
    url = input("Enter RSS feed URL: ")
    entries = parse_rss_feed(url)
    for entry in entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print("=" * 40)
