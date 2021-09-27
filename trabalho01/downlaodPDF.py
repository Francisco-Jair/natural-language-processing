from selenium import webdriver
import requests
import os

# Driver
PATH = 'C:\\Users\\fjair\\.wdm\\drivers\\chromedriver\\win32\\93.0.4577.63\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("http://aplicativos3.mppi.mp.br/consultadiariomp/publico/index.xhtml")

tabelaDiarios = driver.find_element_by_id("formularioConsultaDiarios:diarioSolrTabela_data")
colecaoDiarios = tabelaDiarios.find_elements_by_tag_name('a')

link = []

for pdf in colecaoDiarios:
    nome = pdf.text.replace('-', '')
    nome = nome.replace('/', '')
    tup = (nome, pdf.get_attribute('href'))
    link.append(tup)
    
driver.quit()

diretorio = os.path.abspath("corpus")

for p in link:
    response = requests.get(p[1])
    salvar = f"{diretorio}\{p[0]}.pdf"
    with open(salvar, 'wb') as f:
        f.write(response.content)
        f.close()


