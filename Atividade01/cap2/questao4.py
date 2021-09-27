import nltk

cfd = nltk.ConditionalFreqDist(
  (target, fileid[:4])
  for fileid in nltk.corpus.state_union.fileids()
  for w in nltk.corpus.state_union.words(fileid)
  for target in ['men', 'women', 'people']
  if w.lower().startswith(target))

cfd.plot()

"""
O texto sugere que antes de 1970 o termo mulher quase não era usado, mas desde então tem sido usado mais ou menos como o termo homem.
Pessoas é o termo preferido, principalmente nas últimas décadas.
"""


