#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Alexandre Marques Uchôa                   1715310028
# Carlos Eduardo Tapudima de Oliveira	    1715310030
# Gabriel de Queiroz Sousa                  1715310044
# Lucas Gabriel Silveira Duarte             1715310053
# Natália Cavalcantre Xavier                1715310021
#(a) (MAT 83) Imprimir as n primeiras linhas do triângulo de Pascal (2).

#1

#1    1

#1    2    1

#1    3    3    1

#1    4    6    4    1

#1    5   10   10    5    1

#:

#(b) Imprimir as n primeiras linhas do triângulo de Pascal usando apenas um vetor.


matriz = []

n = int(input())

for i in range(n):
    lista = []
    for j in range(n):
        lista.append(0)
    matriz.append(lista)
for i in range(n):
    for j in range(n):
        if(i>=j):
            if(i==0 or i==j):
                matriz[i][j] = 1
            else:
                matriz[i][j] = matriz[i-1][j-1] + matriz[i-1][j]
for i in range(n):
    print(matriz[i])