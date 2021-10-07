import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split

diret ="./corpus"

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


def convertTexInList(dir, lista=[]):
    listaPalavras = []
    f = open(dir, 'r', encoding="utf-8")
    for line in f:
        listaPalavras.append(line.replace('\n', ''))

    return listaPalavras


def transformarCorpus(docs):
    listDiretorios = getDiretorios(diret)

    #print(listDiretorios[0]) #Generalizar depois
    lista = convertTexInList(listDiretorios[0])
    return lista

def tf_idf_vectorizer(data, n_range):
       
    vectorizer = TfidfVectorizer(strip_accents='ascii', analyzer='word', ngram_range=(1, n_range))
    X_tfidf =  vectorizer.fit_transform(data)
    
    return X_tfidf,vectorizer

def split_data_set(X, y, size):
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,stratify = y, test_size = size, random_state = 42)

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    #print(transformarCorpus(0))
    corpus = transformarCorpus(0)
    X, vec_tf_idf = tf_idf_vectorizer(corpus,1)
    X_train, X_test, y_train, y_test = split_data_set(X,y,0.3)
    #print(vec_tf_idf.get_feature_names())
    #print(X.toarray())