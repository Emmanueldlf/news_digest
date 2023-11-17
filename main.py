import requests
from send_email import send_email
from dotenv import load_dotenv
import os

topic = "tesla"

#Load environment variables
load_dotenv()

#Assign environment variables
id = os.getenv("newsapi_id")
url = os.getenv("newsapi_url")
key = os.getenv("newsapi_key")

topic_filter = f"q={topic}&"
sort_by= f"sortBy=publishedAt&"
api_url = url+topic_filter+sort_by+"apiKey="+key+"&language=en"

#Make a request
request = requests.get(api_url)

#Get the data within dictionary format
content = request.json()

#Iterate over articles data, title and description

email_body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        email_body += "Subject: Today's news" + "\n" +article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

email_body = email_body.encode("utf-8")
send_email(message=email_body)
