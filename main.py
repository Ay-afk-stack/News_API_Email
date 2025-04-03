import requests
import os
from send_mail import send_email
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"

# Make Request
request  = requests.get(url)

# Get a dictionary with data
news = request.json()

# Access the articel titles and description
articles = news['articles']

body = """Subject:Todays News\n"""

# Writing data from the API to a text file
for article in articles:
    if article['title'] is not None:
        body = body + article['title']+"\n"+article['description']+"\n"+ f"Read more at {article['url']} {2*"\n"}"

body = body.encode('UTF-8')
send_email(body)
print("Email sent successfully!")