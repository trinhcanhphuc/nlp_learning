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


"""
A function main of program
"""
def main():
  accessing_text_corpora()
  conditional_frequency_distributions()


if __name__=="__main__":
  main()