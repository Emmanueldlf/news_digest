import requests
from dotenv import load_dotenv
import os

load_dotenv()
id = os.getenv("newsapi_id")
url = os.getenv("newsapi_url")
key = os.getenv("newsapi_key")

request = requests.get(url+key)
content = request.text
print(content)
