n = int(raw_input())
k = [0]*n
dici = ["do","do#","re","re#","mi","fa","fa#","sol","sol#","la","la#","si"]

escala = [[0,2,4,5,7,9,11,0],
          [1,3,5,6,8,10,0,1],
          [2,4,6,7,9,11,1,2],
          [3,5,7,8,10,0,2,3],
          [4,6,8,9,11,1,3,4],
          [5,7,9,10,0,2,4,5],
          [6,8,10,11,1,3,5,6],
          [7,9,11,0,2,4,6,7],
          [8,10,0,1,3,5,7,8],
          [9,11,1,2,4,6,8,9],
          [10,0,2,3,5,7,9,10],
          [11,1,3,4,6,8,10,11]]

for i in range(n):
    k[i] = (int(raw_input()) - 1) % 12

for p,o in enumerate(escala):
    damn = True
    for j in k:
        if not(j in o):
            damn = False
            break
    if(damn):
        break

if (damn):
    print dici[p]
else:
    print "desafinado"
