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
# 28. Faça um procedimento que recebe, por parâmetro, uma matriz A(8,8)
# e calcula o maior elemento da sua diagonal principal.
# A seguir, o procedimento deve dividir todos os elementos de A pelo maior encontrado.
# O procedimento deve retornar a matriz alterada.


from lista08.ipc import matriz

matriz1 = matriz.cria_matriz(8, 8)

maior_da_diagonal = matriz.maior_da_diagonal_principal(matriz1)

matriz2 = matriz.multiplica_matriz_por_inteiro(matriz1, maior_da_diagonal)

print(matriz2)