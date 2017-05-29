# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros   1715310043
# Tiago Ferreira Aranha  1715310047
# Vitor Simôes Azevedo   1715310025
# Uriel Brito Barros     1515120558

# 32. Faça um procedimento que recebe, por parâmetro, uma matriz M(6,6) e um valor A .
#
# O procedimento deve multiplicar cada elemento de M por A e armazenar em um vetor V(36).
#
# O vetor V deve retornar por parâmetro.


from lista08.ipc import matriz

matriz1 = matriz.cria_matriz_quadrada(6)

print(matriz1)

A = int(input("Informe o valor que multiplicará os elementos da matriz: "))

vetor = matriz.multiplica_matriz_por_inteiro(matriz1, 2)

print(vetor)
