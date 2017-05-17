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
#23) Criar um algoritmo que entre com valores inteiros para uma matriz m 3 x 3 e imprima
#a matriz final, conforme mostrado a seguir:
#-----------------------------------------------------------------------------------------------------------------------

import random

linhas = 3
colunas = 3
matriz = []
for g in range(linhas):
    linha = []
    for x in range(colunas):
        valor = random.randint(1,20)
        linha.append(valor)
    matriz.append(linha)
print("Matriz:")
for v in range(0,3):
    print(matriz[v])
matriz_nova = []
linha1 = []
linha1.append(matriz[0][2])
linha1.append(matriz[1][2])
linha1.append(matriz[2][2])
matriz_nova.append(linha1)
linha2 = []
linha2.append(matriz[0][1])
linha2.append(matriz[1][1])
linha2.append(matriz[2][1])
matriz_nova.append(linha2)
linha3 = []
linha3.append(matriz[0][0])
linha3.append(matriz[1][0])
linha3.append(matriz[2][0])
matriz_nova.append(linha3)
print("Matriz com giro 270:")
for b in range(0,3):
    print(matriz_nova[b])
