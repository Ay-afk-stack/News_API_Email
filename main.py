import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-03-03&sortBy=publishedAt&apiKey={api_key}"

# Make Request
request  = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articel titles and description
articles = content['articles']
for article in articles:
    print(article['author'])

