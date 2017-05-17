linhas = int(input())
colunas = int(input())
matriz = []
matriz_transposta = []
matriz_oposta = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input()))
    matriz.append(linha)
print(matriz)

for i in range(colunas):
    linha = []
    for j in range(linhas):
        linha.append(int(matriz[j][i]))
    matriz_transposta.append(linha)
print(matriz_transposta)

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(matriz[i][j]) * -1)
    matriz_oposta.append(linha)
print(matriz_oposta)

if matriz_oposta == matriz_transposta:
    print("Anti simetricas")
else:
    print("Não anti simetricas")


