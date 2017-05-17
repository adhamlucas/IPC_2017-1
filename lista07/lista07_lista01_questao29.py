
#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Antonio Diego Furtado da Silva            1715310004
# Fangyao                                   1115180236
# Matheus de Oliveira Marques               1515310514
# Reinaldo da Silva Varas                   1715310054
# Silas Castro de Mendonça                  1715310066
#
#29) Criar um algoritmo que leia uma matriz A2x2 e calcule a respectiva inversa A-1.
#-----------------------------------------------------------------------------------------------------------------------
import random

linhas = 2
colunas = 2
matriz = []

for g in range(linhas):
    linha = []
    for e in range(colunas):
        x = random.randint(1,100)
        linha.append(x)
    matriz.append(linha)
print("Matriz:")
for y in range(0,2):
    print(matriz[y])

inversa = []
for t in range(0,2):
    b = t
    linha_inversa = []
    for h in range(0,2):
        r = int(matriz[b][h])*(-1)
        linha_inversa.append(r)
    inversa.append(linha_inversa)
print("Inversa:")
for u in range(0,2):
    print(inversa[u])
