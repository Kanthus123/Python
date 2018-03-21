def hanoi (n, ini, fim, aux):
	if (n == 0):
		return

	hanoi (n-1, ini, aux, fim)
	pinos[fim][ndiscos[fim]] = pinos[ini][ndiscos[ini]-1]
	pinos[ini][ndiscos[ini]-1] = 0
	ndiscos[fim] += 1
	ndiscos[ini] -= 1
	desenha ()
	raw_input()
	hanoi (n-1, aux, fim, ini)

def desenha ():
	for j in range (discos-1, -1, -1):
		for i in range (3):
			print " "*(discos - pinos[i][j]),
			print "*"*(2 * pinos[i][j]),
			print " "*(discos - pinos[i][j]),
		print

discos = int(raw_input())

pinos = []
ndiscos = [discos, 0, 0]
for i in range (3):
	pinos.append ([0]*discos)

for i in range (discos):
	pinos[0][i] = discos - i



hanoi (discos, 0, 2, 1)
