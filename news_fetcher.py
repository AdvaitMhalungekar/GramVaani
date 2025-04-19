import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("NEWSDATA_API_KEY")

# API endpoint
url = "https://newsdata.io/api/1/news"

def health_news_fetcher():
    # Parameters for the API
    params = {
        "apikey": api_key,
        "country": "in",
        "language": "en",
        "category": "health"
    }

    # Send GET request
    response = requests.get(url, params=params)

    # Parse response
    if response.status_code == 200:
        data = response.json()
        articles = data.get("results", [])
        
        for i, article in enumerate(articles, 1):
            print(f"\n{i}. {article.get('title')}")
            print(f"   Source: {article.get('source_id')}")
            print(f"   Date: {article.get('pubDate')}")
            print(f"   Link: {article.get('link')}")
    else:
        print("Failed to fetch news:", response.status_code, response.text)
        
if __name__ == "__main__":
    health_news_fetcher()