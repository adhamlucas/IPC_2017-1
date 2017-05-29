# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros          1715310043
# Tiago Ferreira Aranha         1715310047
# Vitor Simôes Azevedo          1715310025
# Roberta de Oliveira da Cruz   0825070169
# Uriel Brito Barros            1515120558
#
# 42. Faça uma função que receba, por parâmetro, uma matriz A(8,8)
# e retorne o menor valor dos elementos acima da diagonal secundária.


from lista08.ipc import matriz, vetor

matriz1 = matriz.cria_matriz_quadrada(3)

diagonal_secundaria = matriz.diagonal_secundaria(matriz1)

menor_da_diagonal_secundaria = vetor.menor_valor_do_vetor(diagonal_secundaria)

print(menor_da_diagonal_secundaria)
