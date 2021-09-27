import nltk
from nltk.book import text5
from nltk.util import bigrams
from nltk.probability import FreqDist

stopwords = nltk.corpus.stopwords.words('english')
words = set()

for w in text5:
    if w.lower() not in stopwords:
        words.add(w)

freqdist = FreqDist(words)

bigramas = list(bigrams(list(freqdist)))

print(bigramas[:50])