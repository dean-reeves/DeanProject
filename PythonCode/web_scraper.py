# web_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('h1')
    return [title.get_text() for title in titles]

def save_titles_to_file(titles, filename):
    with open(filename, 'w') as file:
        for title in titles:
            file.write(f"{title}\n")

if __name__ == "__main__":
    url = 'https://example.com'
    html = fetch_html(url)
    if html:
        titles = parse_html(html)
        save_titles_to_file(titles, 'titles.txt')
        print(f"Titles saved to 'titles.txt'")
    else:
        print("Failed to retrieve the webpage")
