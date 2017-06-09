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
#
# 24  Faça uma função que recebe, por parâmetro, uma matriz A(5,5)
# e retorna a soma dos seus elementos.


from lista08.ipc import matriz

matriz1 = matriz.cria_matriz(5, 5)

valor = matriz.soma_elementos_matriz(matriz1)
print(valor)
