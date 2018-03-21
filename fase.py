n = int(raw_input())
k = int(raw_input())
vet = [0]*n


def passaram(x,k):
    c = 0
    cont = 0

    for i in x:
        if (c < i):
            c = i

    while(cont < k):
        for i in x:
            if(c == i):
                cont += 1
        c = c - 1

    return cont

for i in range(n):
    vet[i] = int(raw_input())

z = passaram(vet,k)
print(z)
