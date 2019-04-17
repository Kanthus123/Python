casos = int(input())
tot = 0

for i in range(casos):
    s = input()

    presmax, pesomax = s.split()
    presmax = int(presmax)
    pesomax = int(pesomax)

    k = input()
    pesopres = map(int, k.split())

    for j in pesopres:
        tot = tot + j
    if(tot <= pesomax):
        print("1")
        tot = 0
    else:
        print (-(-tot//pesomax))
        tot = 0
