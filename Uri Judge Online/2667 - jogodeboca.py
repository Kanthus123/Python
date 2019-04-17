n = raw_input()
tot = 0
for i in n:
    tot += ord(i)

if(tot%3==0):
    print(0)
elif(tot%3==1):
    print(1)
else:
    print(2)
