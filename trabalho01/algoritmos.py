import os

nameDir = "./corpus"

listName = []

for diretorio, subpastas, arquivos in os.walk(nameDir):
    for arquivo in arquivos:
        listName.append(os.path.join(diretorio, arquivo))


def diversidadeLexica(diretorio):
    listaPalavras = []

    f = open(diretorio, 'r', encoding="utf-8")

    for line in f:
        for word in line.split(' '):
            listaPalavras.append(word)
    

    return len(set(listaPalavras)) / len(listaPalavras)
    

def diversidadeLexicaCorpus(listadiretorios):

    listaPalavras = []

    for dire in listadiretorios:
        f = open(dire, 'r', encoding="utf-8")
        for line in f:
            for word in line.split(' '):
                listaPalavras.append(word)
        
        f.close()
    

    return len(set(listaPalavras)) / len(listaPalavras)


"""
f = open(listName[0], 'r', encoding="utf-8")
listaPalavras = []
print(len(listaPalavras))
"""
i = 0
for dire in listName:
    i += 1
    print(f"Diversidade Lexica do texto {i}: {diversidadeLexica(dire)}")


print(f"Diversidade Lexica do corpus: {diversidadeLexicaCorpus(listName)}")
"""
result = diversidadeLexica(listName[0])
print(result)
"""