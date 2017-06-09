#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros   1715310043
# Tiago Ferreira Aranha  1715310047
# Vitor Simôes Azevedo   1715310025
# Lista1. Questão 8: Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
# todos os elementos exceto os elementos da diagonal secundária.

import random

matrix = []
row = 10
column = 10
var = row + 1

# gerando matriz
for i in range (row):
    list=[]
    for j in range(column):
        value = random.randint(0,100)
        list.append(value)
    matrix.append(list)
print(matrix)
for i,n in enumerate(matrix):
    for j,m in enumerate(n):
        # ajuste do índice da matriz, que começa em 1 e não em 0
        if j+i+2 != var:
            print(m,end=' ')
