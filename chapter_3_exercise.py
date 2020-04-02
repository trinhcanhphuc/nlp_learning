# -*- coding: utf-8 -*-

import nltk
from nltk import *
from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import feedparser
import os
from command_history import history
from random import randint
from nltk.corpus import gutenberg
import unicodedata


print("=====================================")
print("Exercise 6")
print("=====================================")
raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
well without--Maybe it's always pepper that makes people hot-tempered,'..."""
patterns = [r'[a-zA-Z]+', r'[A-Z][a-z]*', r'p[aeiou]{,2}t', r'\d+(\.\d+)?', r'([^aeiou][aeiou][^aeiou])*]', r'\w+|[^\w\s]+']

for pattern in patterns:
  nltk.re_show(pattern, raw)

print("=====================================")
print("Exercise 8")
print("=====================================")
def getUrlContent(url):
  return request.urlopen(url).read().decode('utf8')
print(getUrlContent('http://nltk.org/'))

print("=====================================")
print("Exercise 16")
print("=====================================")
from prog import monty
print(monty)

print("=====================================")
print("Exercise 18")
print("=====================================")
raw = gutenberg.raw('melville-moby_dick.txt')
wh_words = set(re.findall(r'\b[wh][Wh]\w+', raw))
print(sorted(wh_words))

print("=====================================")
print("Exercise 19")
print("=====================================")
lines = open('word_freq.txt', encoding='latin2').readlines()
result = [[line.split(' ')[0], int(line.split(' ')[1])] for line in lines]
print(result)

print("=====================================")
print("Exercise 20")
print("=====================================")
weather_url = 'https://weather.com/weather/today/l/10.80,106.62?par=google&temp=c'
req = Request(weather_url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('utf-8')
raw = BeautifulSoup(html, 'html.parser').find('div', id='LookingAhead').get_text()
tokens = word_tokenize(raw)
print(tokens)
pattern = r'\w+\d+[°%F]*\d*'
r = re.compile(pattern)
print(list(filter(r.match, tokens)))
