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
# 27. Faça uma função que receba, por parâmetro, uma matriz A(6,6) e retorna o menor elemento
# da sua dagonal secundária.
#-----------------------------------------------------------------------------------------------------------------------
import ipc.matriz

matrix = ipc.matriz.cria_matriz_quadrada(6)
ipc.matriz.imprime_matriz(matrix)
minor = ipc.matriz.menor_item_secundaria(matrix)
print("O menor item da diagona secundária é: %d" %minor)