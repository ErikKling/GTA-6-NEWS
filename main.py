import requests
from dotenv import load_dotenv
import os
from config.whitelist import WHITELIST
from datetime import datetime, timedelta

today = datetime.now()
days_since_monday = today.weekday()
last_monday = today - timedelta(days=days_since_monday)


load_dotenv()
NEWS_API = os.getenv("NEWS_API_KEY")
url = "https://newsapi.org/v2/everything"

params = {
    "q": "GTA 6",
    "language": "de",
    "apiKey": NEWS_API
}

response = requests.get(url, params=params)
data = response.json()

filtered_articles = []

for article in data["articles"]:
    published_at = datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
    if article["source"]["name"] in WHITELIST and published_at >= last_monday:
        filtered_articles.append(article)
