# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Luiz Paulo Machado                        1515200542
# Luiz Daniel Raposo 	                    1715310049
# Judá Salazar Braga                        1515200050
# Lukas Michel Souza Mota                   1715310018
# Ian Gabriel Costa                         1215010276
#
# Lista1. Questão 7)Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva os
# elementos da diagonal secundária

mat = []
for i in range(10):
    vet = []
    for j in range(10):
        x = int(input())
        vet.append(x)
    mat.append(vet)

for i in range (10):
    for j in range(10):
        if i == 10-1-j:
            print(mat[i][j])




