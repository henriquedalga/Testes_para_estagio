import urllib.parse
import tabula
from tabula.io import read_pdf
import csv
import pandas as pd
import zipfile

listaTabelas = tabula.read_pdf("componente_organizacional.pdf", pages = "114,115")
tabela1 = listaTabelas[0]
tabela2 = listaTabelas[1]


tabela1.columns = tabela1.iloc[0]
tabela1 = tabela1['Código Descrição da categoria'].str.split(' ', expand=True, n=1)
tabela1.columns = tabela1.iloc[0]
tabela1 = tabela1.drop(tabela1.index[[0]])
tabela2.columns = tabela2.iloc[0]
tabela2 = tabela2.drop(tabela2.index[[0]])



tabela1.to_csv("Tabela de Tipo de Demandante.csv", index = False)

tabela2.to_csv("Tabela de Categoria do Padrão TISS.csv", index = False)


listaTabelas2 = tabula.read_pdf("componente_organizacional.pdf", pages = "120", lattice = True)

tabela3 = listaTabelas2[1]

## usei o loop a baixo para descobrir quais eram as colunas da tabela3
#for column in tabela3:
#   print(column)

tabela3 = tabela3[['Tabela de Tipo de Solicitação','Unnamed: 0']]

tabela3 = tabela3.loc[2:]
tabela3.columns = tabela3.iloc[0]
tabela3 = tabela3.loc[3:]


tabela3.to_csv("Tabela de Tipo de Solicitação.csv", index = False)

z = zipfile.ZipFile('Teste_{Henrique_Franco}.zip', 'w', zipfile.ZIP_DEFLATED)
z.write('Tabela de Tipo de Demandante.csv')
z.write('componente_organizacional.pdf')
z.write('Tabela de Tipo de Solicitação.csv')
z.write('Tabela de Categoria do padrão TISS.csv')
z.close()
