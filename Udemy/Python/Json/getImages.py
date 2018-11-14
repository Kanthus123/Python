import requests
from io import BytesIO
from PIL import Image


r = requests.get("https://www.comboinfinito.com.br/principal/wp-content/uploads/2018/07/jojo-vento-aureo.jpg")

print("Status code:", r.status_code)
imagem = Image.open(BytesIO(r.content))
print(imagem.size, imagem.format, imagem.mode)
path = "./imagem." + imagem.format

try:
    imagem.save(path, imagem.format)
except IOError:
    print("Cannot save image.")
