import nltk, pylab, matplotlib, random
from nltk.book import text1
from decimal import *

def freq_rank(text):
    fdist = nltk.FreqDist([w.lower() for w in text])
    keys = fdist.keys()
    freq = []
    rank = []
    n = 1 # must start at 1 because log10(0) = infinity

    for w in keys:
        frequency = Decimal.logb(Decimal(fdist[w]))
        freq.append(frequency)

    for w in keys:
        rank.append(Decimal.logb(Decimal(n)))
        n = n + 1

    pylab.plot(rank, freq)
    return pylab.show()


freq_rank(text1)