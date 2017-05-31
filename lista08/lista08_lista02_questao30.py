#----------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira             1715310001
# Frederico Victor Alfaia Rodrigues         1515200030
# Gabriel Barroso da Silva Lima             1715310011
# Nayara da Silva Cerdeira da Costa         1715310038
# Yuri Leandro de Aquino Silva              1615100462
#
# 30.Faça um procedimento que receba, por parâmetro,
# duas matrizes A(4,6) e B(6,4) e retorna uma matriz C,
# também por parâmetro, que seja a soma de M com N.
#

from ipc import matriz

def cria_matriz_quadrada(n):
    matriz = []
    for i in range(n-6):
        list = []
        for j in range(n-4):
            list.append(A[i][j])
    for i in range(n-4):
        list = []
        for j in range (n-6):
            list.append(B[i][j])
        matriz.append(list)
    return matriz

A = cria_matriz(4, 6)
B = cria_matriz(6, 4)
C = cria_matriz_quadrada(10)