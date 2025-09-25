import requests
from bs4 import BeautifulSoup

# URL of the news site (example: BBC)
URL = "https://www.bbc.com/news"

def scrape_headlines(url):
    # Fetch HTML content
    response = requests.get(url)
    response.raise_for_status()  # raise error if request failed

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines (BBC uses <h2> for many headlines)
    headlines = []
    for h2 in soup.find_all("h2"):
        text = h2.get_text(strip=True)
        if text:  # avoid empty strings
            headlines.append(text)

    return headlines


def save_to_file(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for line in headlines:
            f.write(line + "\n")
    print(f"✅ Saved {len(headlines)} headlines to {filename}")


if __name__ == "__main__":
    headlines = scrape_headlines(URL)
    save_to_file(headlines)