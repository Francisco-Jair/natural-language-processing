import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def getDiretorios(nomeDaPasta):
    """Pega o caminho para todos os arquivos de uma pasta"""
    listName = []
    for diretorio, subpastas, arquivos in os.walk(nomeDaPasta):
        for arquivo in arquivos:
            listName.append(os.path.join(diretorio, arquivo))

    return listName


def montarString(diretorio):
    """Ler o arquivo e retorna o texto"""
    f = open(diretorio, 'r', encoding="utf-8")
    texto = f.read()
    f.close()

    return texto


def TextosCorpus(diretorio="./corpus", opc=-1):
    """
    1. Retorna a lista de texto que contem no corpus
    2. Retorna um texto especificado
    """
    
    listDiretorios = getDiretorios(diretorio)

    cont = 0
    if opc == -1:
        for name in listDiretorios:
            print(f"{cont} - {name}")
            cont += 1
        
        return ""
    elif opc >= 0:
        return montarString(listDiretorios[opc])


def palavrasFrequentes(text):
    """Retorna as n palavras mais frequentes"""

    text1 = text.split(" ")

    fdist = nltk.FreqDist(w.lower() for w in text1)
    return fdist


def docFeatures(docs, lista=[]):
    """
    Representação binaria

    1. Lista e o vocabulario do corpus (todos os textos)
    2. 
    """
    docWords = set(docs) # Vocabulario do documento
    feats = {}

    for w in list(lista):
        feats['contains({})'.format(w)] = (w in docWords) # Binaria
    
    return feats
    

def classificar(docs):
    fsets = [(docFeatures(d), c) for (d, c) in docs]
    #fsets = docs
    #print(fs)
    traingset, traine = fsets[10:], fsets[:10]

    c1 = nltk.NaiveBayesClassifier.train(traingset)
    print(nltk.classify.accuracy(c1, traine))
    print(c1.show_most_informative_features(5))


def classificador(texto):
    pass


stopset = list(set(stopwords.words('portuguese')))

def tokenizacao(words):
    return dict([(word, True) for word in words.split() if word not in stopset])