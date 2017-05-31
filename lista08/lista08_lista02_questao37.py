#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Natália Cavalcantre Xavier                1715310021
# Diogo Roberto Duarte da Costa             1715310056
# Carlos Eduardo Tapudima de Oliveira	    1715310030
# Walter Nobre                              1715310057
# Dayana Picanço Marquez                    1715310058
#
# 37. Na teoria dos sistemas, define-se como elemento minimax
# de uma matriz o menor elemento de uma linha onde se encontra
# o maior elemento da matriz. Faça uma função que recebe, por
# parâmetro, uma matriz A(10,10) e retorna o seu elemento minimax,
# juntamente com a sua posição.
#-----------------------------------------------------------------------------------------------------------------------
from ipc import matriz

mat = matriz.cria_matriz_quadrada(10)
mini = matriz.minimax(mat)
print(mini)
