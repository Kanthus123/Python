import requests

params = {"#q": "pizza"}
r = requests.get("https://google.com", params = params)
print("Status:", r.status_code) # variavel.status_code = acessa a request

print(r.url)

f = open("./page.html", "w+")
f.write(r.text)
