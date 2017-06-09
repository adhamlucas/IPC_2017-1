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
# 29. Faça um procedimento que receba, por parâmetro, duas matrizes A(4,6) e B(6,4)
# e retorna uma matriz C, também por parâmetro,
# que seja o produto matricial de M por N.


from lista08.ipc import matriz

matrizA = matriz.cria_matriz(4, 6)
matrizB = matriz.cria_matriz(6, 4)

matrizC = matriz.cria_matriz_zerada(len(matrizA),len(matrizB[0]))

matriz_final = matriz.produto_matriz(matrizA, matrizB)
matriz.imprime_matriz(matriz_final)
