import nltk
#nltk.download()
from nltk.book import text1

print(len(sorted(set(w.lower() for w in text1))))
print(len(sorted(w.lower() for w in set(text1))))