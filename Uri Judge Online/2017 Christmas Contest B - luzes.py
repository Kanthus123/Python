
def defeito(s):
    cont = 0
    trocar = 0
    for j in s:
      if(j == '1'):
        cont = cont + 1
        if(cont > trocar):
          trocar = cont
      if(j == '0'):
        cont = 0
    return trocar

grupos = int(input())

for i in range(grupos):
    lampadas = int(input())
    lampadas = bin(lampadas)
    print(defeito(lampadas))
