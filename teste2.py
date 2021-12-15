import urllib.parse
import tabula
from tabula.io import read_pdf
import csv
import pandas as pd

listaTabelas = tabula.read_pdf("componente_organizacional.pdf", pages = "114,115,120")
tabela1 = listaTabelas[0]
tabela2 = listaTabelas[1]
tabela3 = listaTabelas[2]

tabela1.columns = tabela1.iloc[0]
tabela2.columns = tabela2.iloc[0]
tabela3.columns = tabela3.iloc[0]

tabela1.to_csv("Tabela de Tipo de Demandante.csv", index = False)

tabela2.to_csv("Tabela de Categoria do Padrão TISS.csv", index = False)

tabela3.to_csv("Tabela de Tipo de Solicitação.csv", index = False)

