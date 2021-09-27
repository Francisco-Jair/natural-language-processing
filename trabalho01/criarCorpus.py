import PyPDF2
import os
import re

nameDir = "./corpus"

listNamePDF = []

for diretorio, subpastas, arquivos in os.walk(nameDir):
    for arquivo in arquivos:
        listNamePDF.append(os.path.join(diretorio, arquivo))

# print(listNamePDF)

pdf_file = open('./corpus\\01092021  Nº 940.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

numPages = read_pdf.getNumPages()

research = ". PROMOTORIAS DE JUSTIÇA"

for i in range(0, numPages):
    PageObj = read_pdf.getPage(i)
    print("this is page " + str(i)) 
    Text = PageObj.extractText() 
    # print(Text)
    ResSearch = re.search(research, Text)
    print(ResSearch)
