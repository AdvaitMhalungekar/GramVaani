import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("NEWSDATA_API_KEY")

# API endpoint
url = "https://newsdata.io/api/1/news"

def health_news_fetcher(category=None,q=None):
    # Parameters for the API
    if q is not None:
        params = {
            "apikey": api_key,
            "country": "in",
            "language": "en",
            "q": q,
            "category": category
        }
    if category is None and q:
        params = {
            "apikey": api_key,
            "country": "in",
            "language": "en",
            "q": q,
        }
    else:
        params = {
            "apikey": api_key,
            "country": "in",
            "language": "en",
            "category": category
        }
    # Send GET request
    response = requests.get(url, params=params)

    # Parse response
    if response.status_code == 200:
        data = response.json()
        articles = data.get("results", [])
        data = []
        
        for i, article in enumerate(articles, 1):
            data.append({
                "title": article.get("title"),
                "descripion": article.get("description"),
                "pubDate": article.get("pubDate"),
                "link": article.get("link")
            })
        # print(data)
        return data
    else:
        print("Failed to fetch news:", response.status_code, response.text)
        
# if __name__ == "__main__":
# #     health_news_fetcher(category="health",q="health OR disease OR medicine OR doctor OR hospital OR patient OR treatment OR care OR health-care OR virus OR mental-health") # Example category
#     health_news_fetcher(q="farming OR agriculture OR (health OR nutrition) OR fertilizer OR pesticide OR crop OR soil OR irrigation") # Example category
# #     