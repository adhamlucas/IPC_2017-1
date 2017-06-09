#---------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Jandinne Duarte de Oliveira                   1015070265
# Wesley da Silva Rocha                         1715310026 
#
# Faça uma função que receba, por parâmetro, uma matriz B(9,9) de
# reais e retorna a soma dos elementos das linhas pares de B.
# 
#---------------------------------------------------------------------

from ipc import matriz

def soma_linha_par(M):
    n = len(M)
    return sum([sum(linha) for linha in M[::2]])

M = matriz.cria_matriz(9, 9)
print(soma_linha_par(M))
