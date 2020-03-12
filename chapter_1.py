from nltk.book import *

"""
A function has a single parameter for the text, and which returns the vocabulary size of the text.
"""
def vocab_size(text):
  fdist = FreqDist(text)
  vocabulary = fdist.keys()
  return len(vocabulary)

"""
A function calculates how often a given word occurs in a text and expresses the result as a percentage.
"""
def percent(word, text):
  return text.count(word) / float(len(text))

"""
A function main of program
"""
def main():
  print("Exercise 10")
  my_sent = ["My", "sent"]
  my_sent = ' '.join(my_sent)
  print(my_sent)
  my_sent = my_sent.split(' ')
  print(my_sent)

  print("Exercise 22")
  print([w for w in FreqDist(text5).keys() if len(w)==4])

  print("Exercise 25")
  text_exe_25 = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
  print([w for w in sorted(set(text_exe_25)) if w.startswith('sh')])
  
  print("Exercise 27")
  print(vocab_size(text1))

  print("Exercise 28")
  print(percent("you", text1))
  

if __name__=="__main__":
  main()