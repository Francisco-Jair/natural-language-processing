import nltk
#nltk.download()
from nltk.book import text2

print(f'Quantidade total de palavras: {len(text2)}')
print(f'Quantidade de palavras sem repetição: {len(set(text2))}')