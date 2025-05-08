import requests
from dotenv import load_dotenv
import os

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
print(data["articles"][1]["title"])