import requests
from send_email import send_email

topic = "tesla"

api_key = "a97be4ff15da488fa33566e3706412d9"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

# Make request
request = requests.get(url)

# Get content in dictionary form
content = request.json()

raw_message = ""

# Access the article titles and descriptions
for article in content["articles"][:20]:
    title = article["title"]
    description = article["description"]
    link = article["url"]
    if title is not None and \
            description is not None and \
            link is not None:
        raw_message = raw_message + f"\nTitle: {title}" \
                                    f"\nDescription: {description}" \
                                    f"\nLink: {link}\n"

message = f"""\
Subject: Tesla News

{raw_message}
"""
message = message.encode("utf-8")

send_email(message)
