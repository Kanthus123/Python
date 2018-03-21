s = raw_input()
o,b,i = s.split()
o = float(o)
b = float(b)
i = float(i)

if (o < b and o < i):
    print "Otavio"
elif (b < o and b < i):
    print "Bruno"
elif (i < b and i < o):
    print "Ian"
else:
    print "Empate"
