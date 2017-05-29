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
# 43. Faça uma função que receba, por parâmetro, uma matriz A(12,12)
# e retorna a média aritmética dos elementos abaixo da diagonal
# principal e da diagonal secundária.


from lista08.ipc import matriz, vetor

matriz1 = matriz.cria_matriz(12, 12)

media_diagonal_pricipal = matriz.media_diagonal_principal(matriz1)
media_diagonal_secundaria = matriz.media_diagonal_secundaria(matriz1)

media = (media_diagonal_pricipal + media_diagonal_secundaria) / 2

print(media)
