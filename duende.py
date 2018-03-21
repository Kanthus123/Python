expediente = int(raw_input())
tempo = raw_input()
brinq1, brinq2 = tempo.split()
brinq1 = int(brinq1)
brinq2 = int(brinq2)

if(brinq1 + brinq2 > expediente):
    print ("Deixa para amanha!")
else:
    print ("Farei hoje!")
