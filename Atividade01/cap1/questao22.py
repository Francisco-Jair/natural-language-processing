from nltk.book import text5
from nltk.probability import FreqDist

list_word_len_four = [w for w in text5 if len(w) == 4]

freq = FreqDist(list_word_len_four)
freq.plot(50)
