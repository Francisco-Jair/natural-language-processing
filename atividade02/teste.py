from nltk.corpus import movie_reviews
import nltk

docs = [(list(movie_reviews.words(fid)), cat)
for cat in movie_reviews.categories() 
for fid in movie_reviews.fileids(cat)
]
    
#print(docs)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())

wFeats = list(all_words)[:2000]

def docFeatures(doc):
    
    docWords = set(doc) # Vocabulario do documento
    feats = {}

    for w in wFeats:
        feats['contains({})'.format(w)] = (w in docWords) # Binaria
    
    return feats

feats = [(docFeatures(d), c) for (d, c) in docs]
print(feats[0])