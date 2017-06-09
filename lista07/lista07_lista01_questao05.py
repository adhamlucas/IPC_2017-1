#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Alexandre Marques Uchôa                   1715310028
# Carlos Eduardo Tapudima de Oliveira	    1715310030
# Gabriel de Queiroz Sousa                  1715310044
# Lucas Gabriel Silveira Duarte             1715310053
# Natália Cavalcantre Xavier                1715310021
#
# Lista1. Questão 5) Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
# somente os elementos abaixo da diagonal principal.

matriz = []
lista = []

for i in range(0,10):

    for j in range(0,10):
        lista.append(int( input('Digite o elemento da posição (%i,%i) da matriz: ' % ((i + 1),(j + 1)))))

    matriz.append(lista)
    lista = []

for line in matriz:
    print(line)

for i in range(0,10):

    for j in range(0,10):

        if (i == j) :
            aux = i + 1

            while aux <= 9:
                print(matriz[aux][j])
                aux += 1