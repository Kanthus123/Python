import re

print("Calculadora")
print("Digite Sair para sair\n")

store = 0
run = True

def operacoesMatematicas():
    global run
    global store
    equacao = ""

    if store == 0:
        equacao = input("Equação Matematica: ")
    else:
        equacao = input(str(store))

    if equacao == 'Sair':
        run = False
    else:
        equacao = re.sub('[a-zA-Z,.:()" "]', '', equacao)

        if store == 0:
            store = eval(equacao)
        else:
            store = eval(str(store) + equacao)

        print("Resposta: \n",store)

while run:
    operacoesMatematicas()
