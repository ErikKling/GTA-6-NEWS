import requests
from dotenv import load_dotenv
import os

load_dotenv()
NEWS_API = os.getenv("NEWS_API_KEY")

print(NEWS_API)