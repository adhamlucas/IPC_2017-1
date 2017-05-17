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
#Criar um algoritmo que leia uma matriz ANxN (N < 10) e calcule a respectiva matriz transposta At

tam = int(input('Informe tamanho da matriz quadrática: '))
matr = [[0 for z in range(tam)] for x in range(tam)]

for i in range(tam):
    for j in range(tam):
        matr[i][j] = int(input("Informe matriz %i%i: " % (i+1, j+1)))
print('Transposta:')
for i in range(tam):
    for j in range(tam):
        print(matr[j][i], end=" ")
    print()
