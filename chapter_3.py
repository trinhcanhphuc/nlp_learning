import nltk
from nltk import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Learning
url = "http://www.gutenberg.org/files/2551/2551.txt"
raw = urlopen(url).read().decode('utf-8')
print(raw[:75])
tokens = nltk.word_tokenize(raw)
print(tokens[:10])
text = nltk.Text(tokens)
print(text[:10])
print('; '.join(text.collocation_list()))
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
print(html[:60])
raw = BeautifulSoup(html).get_text()
tokens = nltk.word_tokenize(raw)
print(tokens[:10])
tokens = tokens[96:399]
text = nltk.Text(tokens)
print(text.concordance('gene'))

