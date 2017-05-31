# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros   1715310043
# Tiago Ferreira Aranha  1715310047
# Vitor Simôes Azevedo   1715310025
# Roberta de Oliveira da Cruz   0825070169
# Uriel Brito Barros            1515120558
#
# 25. Faça uma função que recebe, por parâmetro, uma matriz A(6,6)
# e retorna a soma dos elementos da sua diagonal principal e
# da sua diagonal secundária.


from lista08.ipc import matriz

matriz1 = matriz.cria_matriz(6, 6)

soma1=matriz.media_diagonal_principal(matriz1)

valor = matriz.soma_diagonais(matriz1)
print(matriz1)
print(valor)
