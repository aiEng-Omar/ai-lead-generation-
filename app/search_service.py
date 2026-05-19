import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def search_businesses(niche: str, location: str, num_leads: int = 5):
    query = f"{niche} in {location}"

    url = "https://google.serper.dev/search"
    payload = {"q": query}
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    businesses = []

    if "organic" in data:
        for item in data["organic"][:num_leads]:
            businesses.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet")
            })

    return businesses