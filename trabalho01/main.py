import algoritmos


listaDiretorios = algoritmos.getDiretorios("./corpus")


#a = algoritmos.calcHepaxes(listaDiretorios[0])

b = algoritmos.montarString(listaDiretorios[0])
fre = algoritmos.diversidadeLexica(b)
switc = algoritmos.TextosCorpus(opc=0)


if __name__ == '__main__':
    print(switc)