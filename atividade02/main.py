import bibliotecas

texto = bibliotecas.TextosCorpus(opc=0)
fr = bibliotecas.palavrasFrequentes(texto)

binario = bibliotecas.docFeatures(texto, fr)
a = bibliotecas.tokenizacao(texto)

if __name__ == "__main__":
    print(bibliotecas.classificar(a))
    
    #list(fr)
    #print()