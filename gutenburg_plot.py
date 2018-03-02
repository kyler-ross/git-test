import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup as bs
import nltk
from nltk.tokenize import RegexpTokenizer

def gutenburg_plot(url):
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    words = soup.get_text()
    lowered = []
    for word in words:
        lowered.append(word.lower())
    text = nltk.Text(lowered)
    FreqDist = nltk.FreqDist(text)
    FreqDist.plot(30)