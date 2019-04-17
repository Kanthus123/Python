s = input()
b, o , l, a, d, e, n, v, p = s.split()
b = int(b)
o = int(o)
l = int(l)
a = int(a)
d = int(d)
e = int(e)
n = int(n)
v = int(v)
p = int(p)
renas = ["Dasher",
        "Dancer",
        "Prancer",
        "Vixen",
        "Comet",
        "Cupid",
        "Donner",
        "Blitzen",
        "Rudolph"]
tot = b + o + l + a + d + e + n + v + p

for j in range(tot):
    tot = tot - 1
    ganhadora = renas[j%9]

print(ganhadora)
