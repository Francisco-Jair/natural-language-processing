import algoritmos


listaDiretorios = algoritmos.getDiretorios("./corpus")


#a = algoritmos.calcHepaxes(listaDiretorios[0])

#b = algoritmos.montarString(listaDiretorios[0])
#fre = algoritmos.diversidadeLexica(b)
#dive = algoritmos.diversidadeLexicaCorpus(listaDiretorios)
switc = algoritmos.TextosCorpus(opc=1)
#freque = algoritmos.palavrasFrequentes(switc, 30)
listPalavras = algoritmos.removerStopWords(switc)
freque = algoritmos.palavrasFrequentes(listPalavras, 30)

"""
for t in freque:
    print(f"Palavra: {t[0]} - Porporção: {algoritmos.calculoDaPropocao(switc, t)}")
"""

if __name__ == '__main__':
    print(algoritmos.calCollocations(switc))