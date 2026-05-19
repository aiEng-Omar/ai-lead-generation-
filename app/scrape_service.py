import requests
from bs4 import BeautifulSoup

def scrape_website(url: str):
    try:
        response = requests.get(url, timeout=10, headers={
            "User-Agent": "Mozilla/5.0"
        })
        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator=" ", strip=True)
        clean_text = text[:3000]

        return clean_text
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"