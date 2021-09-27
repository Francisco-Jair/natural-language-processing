from nltk.book import text1

def percent(word, text):
    return 100*(text.count(word)/len(text))


print(f'A porcentagem e {percent("is", text1)}%')