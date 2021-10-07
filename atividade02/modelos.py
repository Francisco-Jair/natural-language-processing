from algoritmos import TextosCorpus, TextosCorpus


listaDiretorios = TextosCorpus("../trabalho01/corpus", opc=1)
print(listaDiretorios)


stoplist = set(listaDiretorios.split(" "))
print(stoplist)