#pesquisa as imagens e coloca na pasta destinada

from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
    search = input("Porcurar por:")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params = params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            title = item.attrs["href"].split("/")[-1] #-1 pega o ultimo elemento de um array
            try:
                img = Image.open(BytesIO(img_obj.content)) #permite ao python utilizar a image
                img.save("./" + dir_name + "/" + title, img.format) #coloca as imgens na pasta indicada
            except:
                print("Could not save image.")
        except:
            print("Could not request Image")
    StartSearch()

StartSearch()
