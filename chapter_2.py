import nltk


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

"""
A function main of program
"""
def main():
  accessing_text_corpora()


if __name__=="__main__":
  main()