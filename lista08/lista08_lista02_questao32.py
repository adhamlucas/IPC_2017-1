# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros   1715310043
# Tiago Ferreira Aranha  1715310047
# Vitor Simôes Azevedo   1715310025
#
# 32. Faça um procedimento que recebe, por parâmetro, uma matriz M(6,6) e um valor A .
#
# O procedimento deve multiplicar cada elemento de M por A e armazenar em um vetor V(36).
#
# O vetor V deve retornar por parâmetro.


from lista08.ipc import vetor, matriz

matriz1 = matriz.cria_matriz(6, 6)


# função que pultiplica cada elemento da matriz por um número n e retorna um vetor
def multiplica_matriz_por_inteiro(matriz, n):
    for i in range(len(matriz)):
        print(i)
        for j in range(len(matriz)):
            print(j)

print(matriz1)
multiplica_matriz_por_inteiro(matriz1,0)
