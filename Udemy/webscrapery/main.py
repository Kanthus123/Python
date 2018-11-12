from bs4 import BeautifulSoup
import requests

search = input("Procurar por:") #pergunta ao usuario o que ele quer pesquisar
params = {"q": search} #diz a URL que ela precisa incluir a variavel inserida na URL para fazer a pesquisa
r = requests.get("http://www.bing.com/search", params = params)

soup = BeautifulSoup(r.text, "html.parser") #pega o conteudo da request e nos permite fazer o "parse" disso
results = soup.find("ol", {"id": "b_results"}) #pega a lista de resultados
links = results.findAll("li", {"class": "b_algo"}) #lista todos os items da pesquisa

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"] #attrs pega o tipo especifico do elemento

    if item_text and item_href:
        print(item_text)
        print(item_href)
