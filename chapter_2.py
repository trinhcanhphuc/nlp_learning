import nltk


"""
This function obtains all bigrams from the text of the book of Genesis, then constructs a conditional frequency distribution to record which words are most likely to follow a given word
"""
def generate_model(cfdist, word, num=15):
  for i in range(num):
    print(word),
    word = cfdist[word].max()

def accessing_text_corpora():
  # Accessing text corpora
  ## Gutenberg Corpus. It contains 25000 free electronic books
  print("=====================================")
  print("Gutenberg Corpus")
  print("=====================================")
  print(nltk.corpus.gutenberg.fileids())
  emma = nltk.corpus.gutenberg.words('austen-emma.txt')
  print(len(emma))

  ## Web and Chat Text. It is a small collection of web text includes content from a Firefox discussion forum, conversations overheard in New York, the movie script of Pirates of the Carribean, personal adver- tisements, and wine reviews
  print("=====================================")
  print("Web and Chat Text")
  print("=====================================")
  from nltk.corpus import webtext
  for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65], '...')

  from nltk.corpus import nps_chat
  chatroom = nps_chat.posts('10-19-20s_706posts.xml')
  print(chatroom[123])

  ## Brown Corpus. It contains text from 500 sources, and the sources have been categorized by genre, such as news, editorial, and so on
  print("=====================================")
  print("Brown Corpus")
  print("=====================================")
  from nltk.corpus import brown
  print(brown.categories())
  print(brown.words(categories='news'))
  print(brown.words(fileids=['cg22']))
  print(brown.sents(categories=['news', 'editorial', 'reviews']))

  ## Reuters Corpus. It contains 10,788 news documents totaling 1.3 million words
  print("=====================================")
  print("Reuters Corpus")
  print("=====================================")
  from nltk.corpus import reuters
  print(reuters.fileids())
  print(reuters.categories())
  print(reuters.categories('training/9865'))
  print(reuters.categories(['training/9865', 'training/9880']))
  print(reuters.fileids('barley'))
  print(reuters.fileids(['barley', 'corn']))

  ## Inaugural Address Corpus. It contains Corpus Addresses
  print("=====================================")
  print("Inaugural Address Corpus")
  print("=====================================")
  from nltk.corpus import inaugural
  print(inaugural.fileids())
  print([fileid[:4] for fileid in inaugural.fileids()])
  cfd = nltk.ConditionalFreqDist((target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))
  cfd.plot()

  ## Annotated Text Corpora. It contains linguistic annotations, representing part-of-speech tags, named entities, syntactic structures, semantic roles, and so forth
  print("=====================================")
  print("Annotated Text Corpora")
  print("=====================================")

def conditional_frequency_distributions():
  counting_words_by_genre()
  plotting_and_tablutating()
  generating_random_text_with_bigrams()

def counting_words_by_genre():
  ## Counting Words By Genre
  print("=====================================")
  print("Counting Words By Genre")
  print("=====================================")
  from nltk.corpus import brown
  cfd = nltk.ConditionalFreqDist((genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
  print(len(cfd))
  genre_word = [(genre, word)
                for genre in ['news', 'romance']
                for word in brown.words(categories=genre)]
  print(len(genre_word))
  print(genre_word[:4])
  print(genre_word[-4:])
  cfd = nltk.ConditionalFreqDist(genre_word)
  print(cfd.conditions())
  print(list(cfd['romance'])[:10])

def plotting_and_tablutating():
  print("=====================================")
  print("Plotting and Tabulating Distributions")
  print("=====================================")
  from nltk.corpus import inaugural
  cfd = nltk.ConditionalFreqDist((target, fileid[:4])
    for fileid in inaugural.fileids() for w in inaugural.words(fileid)
    for target in ['america', 'citizen'] if w.lower().startswith(target))
  print(list(cfd['america'])[:10])
  from nltk.corpus import udhr
  languages = ['Chickasaw', 'English', 'German_Deutsch',
  'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
  cfd = nltk.ConditionalFreqDist((lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1'))
  print(list(cfd['English'])[:10])
  print(cfd.tabulate(conditions=['English', 'German_Deutsch'], samples=range(20), cumulative=True))

def generating_random_text_with_bigrams():
  print("=====================================")
  print("Generating Random Text with Bigrams")
  print("=====================================")
  sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
  print(list(nltk.bigrams(sent)))
  text = nltk.corpus.genesis.words('english-kjv.txt')
  bigrams = nltk.bigrams(text)
  cfd = nltk.ConditionalFreqDist(bigrams)
  print(list(cfd['living']))
  generate_model(cfd, 'living')

def lexical_diversity(text):
  word_count = len(text)
  vocab_size = len(set(text))
  return word_count/vocab_size

def plural(word):
  if word.endswith('y'):
    return word[:-1] + 'ies'
  elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
    return word + 'es'
  elif word.endswith('an'):
    return word[:-2] + 'en'
  else:
    return word + 's'


def reusing_code():
  print("=====================================")
  print("Lexical Diversity")
  print("=====================================")
  print(lexical_diversity("Hi My name is Pluar. My dog is Zero"))
  print("=====================================")
  print("Plural")
  print("=====================================")
  print(plural('fairy'))
  print(plural('woman'))

def unusual_words(text):
  text_vocab = set(w.lower() for w in text if w.isalpha())
  english_vocab = set(w.lower() for w in nltk.corpus.words.words())
  unusual = text_vocab.difference(english_vocab)
  return sorted(unusual)

def lexical_resources():
  print("=====================================")
  print("Wordlist Corpora")
  print("=====================================")
  print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))[:10])
  print(unusual_words(nltk.corpus.nps_chat.words())[:10])
  from nltk.corpus import stopwords
  print(stopwords.words('english')[:10])
  print(content_fraction(nltk.corpus.reuters.words()))
  print(produce_word_from_chars('egivrvonl'))
  print(find_name_both_male_and_female()[:10])
  plot_names()
  print("=====================================")
  print("A Pronouncing Dictionary")
  print("=====================================")
  entries = nltk.corpus.cmudict.entries()
  print(len(entries))
  for entry in entries[39943:39951]:
    print(entry)
  print([w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']][:10])
  print("=====================================")
  print("Comparative Wordlists")
  print("=====================================")
  from nltk.corpus import swadesh
  print(swadesh.fileids())
  print(swadesh.words('en')[:10])
  translate()
  translate_mul_langs(['en', 'de', 'nl', 'es', 'fr', 'pt', 'la'])
  print("=====================================")
  print("Shoebox and Toolbox Lexicons")
  print("=====================================")
  from nltk.corpus import toolbox
  print(toolbox.entries('rotokas.dic')[:2])
  print("=====================================")
  print("WordNet")
  print("=====================================")
  from nltk.corpus import wordnet as wn
  wn.synsets('motorcar')
  print(wn.synset('car.n.01').lemma_names())
  print(wn.synset('car.n.01').definition())
  print(wn.synset('car.n.01').examples())
  print(wn.synsets('car'))
  motorcar = wn.synset('car.n.01')
  types_of_motorcar = motorcar.hyponyms()
  print(types_of_motorcar[26])

def stress(pron):
  return [char for phone in pron for char in phone if char.isdigit()]
def produce_word_from_chars(chars):
  puzzle_letters = nltk.FreqDist(chars)
  obligatory = 'r'
  wordlist = nltk.corpus.words.words()
  return [w for w in wordlist if len(w) >= 6
                          and obligatory in w
                          and nltk.FreqDist(w) <= puzzle_letters]

def find_name_both_male_and_female():
  names = nltk.corpus.names
  male_names = names.words('male.txt')
  female_names = names.words('female.txt')
  return [w for w in male_names if w in female_names]

def plot_names():
  names = nltk.corpus.names
  cfd = nltk.ConditionalFreqDist((fileid, name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid))
  cfd.plot()

def content_fraction(text):
  stopwords = nltk.corpus.stopwords.words('english')
  content = [w for w in text if w.lower() not in stopwords]
  return len(content)/len(text)

def translate():
  from nltk.corpus import swadesh
  fr2en = swadesh.entries(['fr', 'en'])
  translate = dict(fr2en)
  print(translate['chien'])

def translate_mul_langs(languages):
  from nltk.corpus import swadesh
  for i in [139, 140, 141, 142]:
    print(swadesh.entries(languages)[i])

def exercise():
  print("=====================================")
  print("Exercise 1")
  print("=====================================")
  # Create a variable phrase containing a list of words. Experiment with the operations described in this chapter, including addition, multiplication, indexing, slicing, and sorting.
  from nltk.corpus import webtext
  fileid = webtext.fileids()[0]
  phrase = webtext.words(fileid)
  print("addition: ", phrase[:10]+["aaaa"])
  print("multiplication: ", phrase[:10]*2)
  print("slicing: ", sorted(phrase[:10]))
  print("=====================================")
  print("Exercise 2")
  print("=====================================")
  # Use the corpus module to explore austen-persuasion.txt. How many word tokens does this book have? How many word types (vocabularies)?
  from nltk.corpus import gutenberg
  text = gutenberg.words('austen-persuasion.txt')
  tokens = len(text)
  print("tokens: ", tokens)
  word_types = len(set([w.lower() for w in text]))
  print("word_types: ", word_types)
  print("=====================================")
  print("Exercise 3")
  print("=====================================")
  # Use the Brown Corpus reader nltk.corpus.brown.words() or the Web Text Corpus reader nltk.corpus.webtext.words() to access some sample text in two different genres.
  from nltk.corpus import brown
  brown_text = brown.words(categories='news')
  print(brown_text[:10])
  from nltk.corpus import webtext
  webtext_text = webtext.words(webtext.fileids()[0])
  print(webtext_text[:10])
  print("=====================================")
  print("Exercise 4")
  print("=====================================")
  # Read in the texts of the State of the Union addresses, using the state_union corpus reader. Count occurrences of men, women, and people in each document. What has happened to the usage of these words over time?
  from nltk.corpus import state_union
  for fileid in state_union.fileids():
    print(len([w.lower() for w in state_union.words(fileid) if w=='men' or w=='women' ]))
  print("=====================================")
  print("Exercise 5")
  print("=====================================")
  # Investigate the holonym-meronym relations for some nouns. Remember that there are three kinds of holonym-meronym relation, so you need to use member_meronyms(), part_meronyms(), substance_meronyms(), member_holonyms(), part_holonyms(), and substance_holonyms().
  from nltk.corpus import wordnet as wn
  print([synset.name() + ': ' + synset.definition() for synset in wn.synsets('table')])
  synset = wn.synset('table.n.02')
  print(synset.name() + ': ' + synset.definition())
  print(synset.part_meronyms())
  print(synset.substance_meronyms())
  print(synset.member_holonyms())
  print(synset.part_holonyms())
  print(synset.substance_holonyms())
  print("=====================================")
  print("Exercise 6")
  print("=====================================")
  # In the discussion of comparative wordlists, we created an object called translate, which you could look up using words in both German and Italian in order to get corresponding words in English. What problem might arise with this approach? Can you suggest a way to avoid this problem?
  # Answer: It can't translate some words and uses too many resources
  from nltk.corpus import swadesh
  en2it = swadesh.entries(['en', 'it'])
  translate = dict(en2it)
  print(translate['we'])
  




"""
A function main of program
"""
def main():
  # accessing_text_corpora()
  # conditional_frequency_distributions()
  # reusing_code()
  # lexical_resources()
  exercise()


if __name__=="__main__":
  main()