##------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Adham Lucas da Silva Oliveira                 1715310001
# Jandinne Duarte de Oliveira                   1015070265
# Roberta de Oliveira da Cruz                   0825070169
# Nayara da Silva Cerdeira da Costa             1715310038
# Wesley da Silva Rocha                         1715310026 
#
#
#3) Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
#somente os elementos acima da diagonal principal.
#-----------------------------------------------------------------------------------------------------------------------
m = 10
n = 10
matriz = []
linha = []

for i in range(m):
    for j in range(n):
        x = int(input("Digite um valor:"))
        linha.append(x)
    matriz.append(linha)

for i in range(m):
    for j in range(n):
        if i<j:
            print(matriz[i][j])
