# -*- coding: utf-8 -*-

import nltk
from nltk import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import feedparser
import os
from command_history import history
from random import randint

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

path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = open(path, encoding='latin2')
for line in f:
  print(line.strip())

def flip(segs, pos):
  return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

def flip_n(segs, n):
  for i in range(n):
    segs = flip(segs, randint(0, len(segs)-1))
  return segs
def segment(text, segs):
  words = []
  last = 0
  for i in range(len(segs)):
    if segs[i] == '1':
      words.append(text[last:i+1])
      last = i+1
  words.append(text[last:])
  return words

def evaluate(text, segs):
  words = segment(text, segs)
  text_size = len(words)
  lexicon_size = sum(len(word) + 1 for word in set(words))
  return text_size + lexicon_size

def anneal(text, segs, iterations, cooling_rate):
  temperature = float(len(segs))
  while temperature > 0.5:
    best_segs, best = segs, evaluate(text, segs)
    for i in range(iterations):
      guess = flip_n(segs, round(temperature))
      score = evaluate(text, guess)
      if score < best:
        best, best_segs = score, guess
    score, segs = best, best_segs
    temperature = temperature / cooling_rate
    print(evaluate(text, segs), segment(text, segs))
  print()
  return segs



text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
anneal(text, seg1, 5000, 1.2)
