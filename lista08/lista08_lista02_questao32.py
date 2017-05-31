#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Joelson Pereira Lima 			        1715310060
# Víctor Hugo de Oliveira Carreira      1715310063
#
#32.Faça um procedimento que recebe, por parâmetro, uma matriz M(6,6) e um valor A . O procedimento deve multiplicar cada
# elemento de M por A e armazenar em um vetor V(36). O vetor V deve retornar por parâmetro.
#-----------------------------------------------------------------------------------------------------------------------
import random
def matriz_mult(x,y):
    A = int(input())
    matriz = []
    for i in range(x):
        linha = []
        for j in range(y):
            linha.append(random.randint(1,1) * A)
        matriz.append(linha)

    return matriz

def matriz_no_vetor(matriz):
    vetor = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            vetor.append(matriz[i][j])
    return vetor




print(matriz_no_vetor(matriz_mult(6,6)))



