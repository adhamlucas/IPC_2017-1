#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Natália Cavalcantre Xavier                1715310021
# Diogo Roberto Duarte da Costa             1715310056
# Carlos Eduardo Tapudima de Oliveira	      1715310030
# Walter Nobre                              1715310057
# Dayana Picanço Marquez                    1715310058
#
# 36. Faça um procedimento que receba, por parâmetro, uma matriz A(6,6) e multiplica cada linha
# pelo elemento da diagonal principal daquela linha. O procedimento deve retornar a matriz alterada.
#-----------------------------------------------------------------------------------------------------------------------
from ipc import matriz

mat = matriz.cria_matriz_quadrada(6)
mat = matriz.multiplica_linha(mat)

matriz.imprime_matriz(mat)
