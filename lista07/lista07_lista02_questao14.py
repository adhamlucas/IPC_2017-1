colunas = int(input())
linhas = int(input())
matriz = []
custo = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input()))
    matriz.append(linha)
print(matriz)

locais = input().split()

for i in range(len(locais)-1):
    custo += matriz[int(locais[i])] [int(locais[i+1])]

print(custo)




