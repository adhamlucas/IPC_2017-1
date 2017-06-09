#---------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Jandinne Duarte de Oliveira                   1015070265
# Wesley da Silva Rocha                         1715310026 
#
# Faça um procedimento que receba uma matriz A(10, 10), por parâmetro
# e realize as seguintes trocas:
#   a linha 2 com a linha 8;
#   a coluna 4 com a coluna 10;
#   a diagonal principal com a secundária;
#   a linha 5 com a coluna 10
# O procedimento deve retornar a matriz alterada
# 
#---------------------------------------------------------------------

from ipc import matriz

def swap(a, b):
    a, b = b, a

def troca_elementos(M):
    n = len(M)
    for j in range(n):
        M[1][j], M[7][j] = M[7][j], M[1][j]
    for i in range(n):
        M[i][4], M[i][9] = M[i][9], M[i][4]
    for i in range(n):
        j = n-(i+1)
        M[i][i], M[i][j] = M[i][j], M[i][i]
    for k in range(n):
        M[4][k], M[k][9] = M[k][9], M[4][k]
    return M

M = matriz.cria_matriz(10, 10)
M = troca_elementos(M)
matriz.imprime_matriz(M)
