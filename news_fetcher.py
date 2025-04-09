import requests
from config import NEWS_API_KEY

def fetch_top_headlines():
    url = f"https://newsapi.org/v2/top-headlines?language=en&pageSize=5&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("articles", [])