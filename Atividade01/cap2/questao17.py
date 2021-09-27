import nltk
from nltk.book import text5
from nltk.probability import FreqDist


def freq_non_stopwords(text):
	stopwords = nltk.corpus.stopwords.words('english')
	clean_list = [w for w in text if w.lower() not in stopwords]
	freqdist = FreqDist(clean_list)
	return list(freqdist.keys())

p = freq_non_stopwords(text5)[:50]
for word in p:
    print(word)