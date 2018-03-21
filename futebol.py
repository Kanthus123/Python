while True:
	try:
		s = raw_input ()

		n, g = map (int, s.split())
	except EOFError:
		break
	except ValueError:
		break

	vit = 0
	emp = 0
	derrotas = []
	for i in range (n):
		s = raw_input ()
		gp, gc = map (int, s.split())

		if (gp > gc):
			vit += 1
			continue

		if (gp == gc):
			emp += 1
			continue

		derrotas.append (gc - gp)

	if g >= emp:
		vit += emp
		g -= emp
		emp = 0
	else:
		vit += g
		emp -= g
		g = 0

	derrotas.sort ()

	for i in derrotas:
		if (g > i):
			vit += 1
			g -= i+1
		elif (g == i):
			emp += 1
			g -= i
			break

print vit*3+emp
