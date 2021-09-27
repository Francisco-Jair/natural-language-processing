from nltk.book import text2, text3

def diversidade_lexica(text):
    return len(text)/len(set(text))

def contagem_de_palavras(text):
    return len(text)

def tamanho_vocabulario(text):
    return len(set(text))


print("------------------ TEXT2 ----------------------")

print(diversidade_lexica(text2))
print(contagem_de_palavras(text2))
print(tamanho_vocabulario(text2))
print("------------------ TEXT3 ----------------------")
print(diversidade_lexica(text3))
print(contagem_de_palavras(text3))
print(tamanho_vocabulario(text3))
