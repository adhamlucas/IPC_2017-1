# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros          1715310043
# Tiago Ferreira Aranha         1715310047
# Vitor Simôes Azevedo          1715310025
# Roberta de Oliveira da Cruz   0825070169
#
#
# 42. Faça uma função que receba, por parâmetro, uma matriz A(8,8)
# e retorne o menor valor dos elementos acima da diagonal secundária.


from lista08.ipc import matriz

matriz1 = matriz.cria_matriz(8, 8)

menor_da_diagonal = matriz.menor_da_diagonal_secundaria(matriz1)

print(menor_da_diagonal)