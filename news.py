import requests
from bs4 import BeautifulSoup
import html

def getNewsHeadline(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        headline = soup.find("h1")
        print(headline)
        headline = html.unescape(headline.text)
        return headline
    except Exception as e:
        print("news=>", e)