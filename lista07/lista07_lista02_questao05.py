# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros   1715310043
# Tiago Ferreira Aranha  1715310047
# Vitor Simôes Azevedo   1715310025
#
# 5.  Dizemos que uma matriz inteira Anxn  é uma matriz de permutação se em cada linha e em cada coluna houver n-1 elementos nulos e um único elemento igual a 1.

import random

matriz = []
linhas = 3
colunas = 3

# gerando matriz
for i in range(linhas):
    lista = []
    for j in range(colunas):
        lista.append(random.randint(0, 1))
    matriz.append(lista)

print(matriz,"\n")

verifica = 0

for i, n in enumerate(matriz):
    zeros = 0
    uns = 0
    for j, m in enumerate(n):
        if matriz[i][j] == 0:
            zeros += 1
        elif matriz[i][j] == 1:
            uns += 1

    if zeros == linhas - 1 and uns == linhas - (linhas - 1):
        verifica += 1

if verifica == linhas:
    print("A matriz é de permutação")
else:
    print("A matriz NÃO é de permutação")
