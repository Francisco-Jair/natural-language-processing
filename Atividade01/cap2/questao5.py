from nltk.corpus import wordnet as wn

lava = wn.synsets('lava')[0]
ice = wn.synsets('ice')[0]
print(lava.common_hypernyms(ice))
print(ice.substance_holonyms())
print(ice.substance_meronyms())