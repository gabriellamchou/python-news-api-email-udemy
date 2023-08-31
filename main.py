import requests
from send_email import send_email

api_key = "a97be4ff15da488fa33566e3706412d9"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-07-31&sortBy=" \
      "publishedAt&apiKey=a97be4ff15da488fa33566e3706412d9"

# Make request
request = requests.get(url)

# Get content in dictionary form
content = request.json()

raw_message = ""

# Access the article titles and descriptions
for article in content["articles"]:
    title = article["title"]
    description = article["description"]
    source = article["source"]["name"]
    author = article["author"]
    raw_message = raw_message + f"\nTitle: {title}\nDescription: {description}" \
                                f"\nSource: {source}\nAuthor: {author}\n"

message = f"""\
Subject: Tesla News

{raw_message}
"""
message = message.encode("utf-8")

send_email(message)
