import nltk
#nltk.download()
from nltk.book import text5

list_word = sorted([w for w in text5 if w.startswith('b')])

for word in list_word:
    print(word)
