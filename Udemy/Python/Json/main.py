import json #não é necessario mais usar simplejson apenas json na chamada do import
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read()) #json.loads = Converte o conteudo em  do arquivo para um formato que pode ser usado pelo python
    print("Current age is", data["age"], "--- adding a year.")
    data["age"] = data["age"] + 1
    print("Now age is", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "Nick", "age": 27}
    print("No file found, setting default age to", data["age"])

old_file.seek(0) #Começa a ler o arquivo do inicio
old_file.write(json.dumps(data)) #json.dumps = converte de volta para json

#newfile = open("newfile.txt", "w+") # 1- caminho do arquivo, 2- o que fazer com ele

#string = "This is the content that will be written to the text file"

#newfile.write(string) #Escreve no arquivo, se ele não existir, cria ele no diretorio
