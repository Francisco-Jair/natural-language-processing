import nltk

files_names = ["female.txt", 'male.txt']
dates = [(file, word[0]) for file in files_names for word in nltk.corpus.names.words(file)]

distribution = nltk.ConditionalFreqDist(dates)
distribution.tabulate()   
#distribution.plot()