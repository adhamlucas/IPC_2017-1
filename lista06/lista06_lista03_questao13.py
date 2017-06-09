pp = []
pq = []
np = int(input("o grau de p:"))
nq = int(input("o grau de q:"))
for i in range (np) :
    x = int(input("Coeficiente a:"))
    pp.append(x)
for i in range (nq) :
     x = int(input("Coeficiente b:"))
     pq.append(x)
xp = int(input("O x de p:"))
xq = int(input("O x de q:"))
somap = 0
somaq = 0
for i in range (np):
    somap += pp[i] * (xp ** i)
for i in range (nq):
    somaq += pq[i] * (xq ** i)
produto = somap * somaq
print(produto)