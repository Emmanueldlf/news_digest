import requests
from dotenv import load_dotenv
import os

#Load environment variables
load_dotenv()

#Assigne environment variables
id = os.getenv("newsapi_id")
url = os.getenv("newsapi_url")
key = os.getenv("newsapi_key")
api_url = url+key

#Make a request
request = requests.get(api_url)

#Get the data within dictionary format
content = request.json()

#Iterate over articles data
for article in content["articles"]:
    print(article["title"])
