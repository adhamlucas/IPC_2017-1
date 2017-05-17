#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IP
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Joelson Pereira Lima 			        1715310060
# Víctor Hugo de Oliveira Carreir      1715310063
#
#25) Criar um algoritmo que leia valores para uma matriz M2x2. Calcular e imprimir o
#determinante. Para cálculo do determinante de uma matriz de ordem 2, é simplesmente
#computar a diferença entre os produtos das diagonais principal e secundária,
#respectivamente.
#----------------------------------------------------------------------------------------------------------------------
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


