import requests

api_key = "a97be4ff15da488fa33566e3706412d9"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-07-31&sortBy=" \
      "publishedAt&apiKey=a97be4ff15da488fa33566e3706412d9"

# Make request
request = requests.get(url)

# Get content in dictionary form
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
