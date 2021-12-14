import requests
from bs4 import BeautifulSoup

# acessando o link:
response = requests.get("https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss")
status = response.status_code
if(status == 200):
    print("Requisicao ok")

else:
    print("Erro na requisicao")

#procurando o local da pagina que contem o arquivo:
soup = BeautifulSoup(response.text, 'html.parser')
lastversionlink = soup.find(attrs = {'class' : 'callout'})
for link in lastversionlink:
    response2 = requests.get(link.get('href'))
    soup2 = BeautifulSoup(response2.text, "html.parser")
componente = soup2.find(class_='table-responsive')
componenteA = componente.find('a')
Url = componenteA.get('href')

#funcao para baixar arquivo:
def baixar_arquivo(url, enderecoLocal):
    resposta = requests.get(url, stream=True) 
    if resposta.status_code == requests.codes.OK:
        with open(enderecoLocal, 'wb') as novo_arquivo: 
                novo_arquivo.write(resposta.content)
        print("Download finalizado. Arquivo salvo em: {}".format(enderecoLocal))
    else:
        print("Erro ao realizar o download")
        resposta.raise_for_status()

#utilizando a funcao para baixar
baixar_arquivo(Url, 'componente_organizacional.pdf')