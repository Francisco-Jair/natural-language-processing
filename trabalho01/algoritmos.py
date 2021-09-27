import os
import nltk
from nltk.corpus import stopwords

nameDir = "./corpus"
textos = []


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


def TextosCorpus(diretorio=nameDir, opc=-1):
    """Retorna a lista de texto que contem no corpus"""
    
    listDiretorios = getDiretorios(diretorio)

    cont = 0
    if opc == -1:
        for name in listDiretorios:
            print(f"{cont} - {name}")
            cont += 1
        
        return ""
    elif opc >= 0:
        return montarString(listDiretorios[opc])


def diversidadeLexica(texto):
    """Retorna a diversidade lexical de um texto"""
    listaPalavras = []
    
    for word in texto.split(' '):
        listaPalavras.append(word.replace('\n', ''))

    return len(set(listaPalavras)) / len(listaPalavras)
    

def diversidadeLexicaCorpus(listadiretorios):

    listaPalavras = []

    for arquivo in listadiretorios:
        texto = montarString(arquivo)
        for word in texto.split(' '):
            listaPalavras.append(word.replace('\n', ''))    

    return len(set(listaPalavras)) / len(listaPalavras)


def palavrasFrequentes(text, n):
    """Retorna as n palavras mais frequentes"""

    fdist = nltk.FreqDist(text)
    return fdist.most_common(n)


def calculoDaPropocao(text, tupla):
    """
    Calcula a proporção de uma palavra em relação ao texto
    
    text -> Texto que vai ser analisado
    tupla -> tupla com a palavra e a quantidade de ocorrencia dela

    """
    # [(word[0], word[1]/len(text)) for word in words]

    return tupla[1]/len(text)


def removerStopWords(text):
    """Remove as stop words de textos em portugues"""

    stop_words = stopwords.words('portuguese')
    return [word for word in text if word not in stop_words]


def calcHepaxes(text):
    """Mostra os Hepaxes de um texto"""
    fdist = nltk.FreqDist(text)

    return fdist.hapaxes()


def bigramas(text):
    print(text)
    #print(text.collocations())


#https://www.nltk.org/book/ch01.html

"""
f = open(listName[0], 'r', encoding="utf-8")
listaPalavras = []
print(len(listaPalavras))
"""


"""

AQUI
i = 0
for dire in getDiretorios(nameDir):
    i += 1
    print(f"Diversidade Lexica do texto {i}: {diversidadeLexica(dire)}")


print(f"Diversidade Lexica do corpus: {diversidadeLexicaCorpus(getDiretorios(nameDir))}")
"""

"""
result = diversidadeLexica(listName[0])
print(result)
"""