import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

url = "https://seekingalpha.com/article/4550191-lpl-financial-holdings-inc-lpla-q3-2022-earnings-call-transcript"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

transcript = soup.find_all("p")

text = ""
for words in transcript:
    text += words.get_text() + " "

blob = TextBlob(text)
sentiment = blob.sentiment

# Print the sentiment scores
print(sentiment)
