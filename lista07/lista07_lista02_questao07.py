linhas = int(input())
colunas = int(input())
matriz = []
somas = []
soma = 0
c = 0
verifications = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input()))
    matriz.append(linha)

while c < linhas:
    for j in range(colunas):
        soma += matriz[c][j]
    somas.append(soma)
    c += 1
    soma = 0
c = 0
while c < colunas:
    for j in range(linhas):
        soma += matriz[j][i]
    somas.append(soma)
    c += 1
    soma = 0

c = 0

for x in range(linhas):
    soma += matriz[x][x]
somas.append(soma)
soma = 0

c = linhas - 1
while c > -1:
    soma += matriz[c][c]
    c -= 1
    

somas.append(soma)


for x in range(len(somas)):
    if somas[x] == soma:
        verifications += 1


if verifications == len(somas):
    print('sim')

else:
    print('não')

