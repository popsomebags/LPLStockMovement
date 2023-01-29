import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

url = "https://seekingalpha.com/article/4528986-lpl-financial-holdings-inc-lpla-ceo-dan-arnold-on-q2-2022-results-earnings-call-transcript"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

transcript = soup.find_all("p")

text = ""
for words in transcript:
    text += words.get_text() + " "

blob = TextBlob(text)
sentiment = blob.sentiment

if blob.sentiment.polarity > 0:
    print("The overall polarity is " + str(blob.sentiment.polarity) + " which means that the overall sentiment is positive.")
else: 
    print("The overall polarity is " + str(blob.sentiment.polarity) + " which means that the overall sentiment is negative.")
