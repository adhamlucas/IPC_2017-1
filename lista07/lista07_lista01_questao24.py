#------------------------------------------------------------------------------
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
#Criar um algoritmo que leia e armazene os elementos de uma matriz inteira M10x10 e
#imprimi-la. Troque, na ordem a seguir:
#- a segunda linha pela oitava linha;
#- a quarta coluna pela décima coluna;
#- a diagonal principal pela diagonal secundária.
#---------------------------------------------------------------------------------------
matriz = []
ordem = 10

for m in range(ordem):
    linha = []
    for n in range(ordem):
        linha.append(int(input('Digite o valor(%d,%d): ' %(m,n))))
    matriz.append(linha)

for x in (matriz):
    print(*x)

linha = matriz[1]
matriz[1] = matriz[7]
matriz[7] = linha
linha = [[] for x in range(10)]

for i in range(ordem):
    linha[i] = matriz[i][3]
    matriz[i][3] = matriz[i][9]
    matriz[i][9] = linha[i]

for i in range(ordem):
    linha[i] = matriz[i][i]
    matriz[i][i] = matriz[i][9-i]
    matriz[i][9-i] = linha[i]

for x in (matriz):
    print(*x)
