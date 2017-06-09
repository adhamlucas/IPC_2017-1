#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Joelson Pereira Lima 			        1715310060
# Víctor Hugo de Oliveira Carreira      1715310063
#
#2.  Um vetor real X com n elementos é apresentado como resultado de um sistema de equações lineares Ax = B cujos
#coeficientes são representados em uma matriz real Amxn e os lados direitos das equações em um vetor real B de m
#elementos. Verificar se o vetor X é realmente solução do sistema dado.
#
#-----------------------------------------------------------------------------------------------------------------------
linhas = int(input())
colunas = int(input())
vetor_x = input().split()
matriz = []
matriz_b = []
result = []
c = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input()))
    matriz.append(linha)

for i in range(linhas):
    linha = []
    for j in range(1):
        linha.append(int(input()))
    matriz_b.append(linha)

while c < len(vetor_x):
    for i in range(linhas):
        linha = []
        for j in range(1):
            linha.append(int(matriz[i][j]) * int(vetor_x[c]))
        result.append(linha)
    c += 1

if result == matriz_b:
    print("True")
else:
    print("False")

