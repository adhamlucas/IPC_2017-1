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
#Ler valores inteiros para a matriz A3x5. Gerar e imprimir a matriz (vetor) SL (soma das
#3 linhas), onde cada elemento é a soma dos elementos de uma linha da matriz A. Faça
#o trecho que gera a matriz SL separado (laços de repetição) da entrada e da saída de
#dados..
#-----------------------------------------------------------------------------------------------------------------------

A = []
linhas = 3
SL = []
sum = 0

for x in range(linhas):
    lista = input('Digite os 5 valores da linha %d' %(x+1)).split()
    A.append(lista)

for i, element in enumerate(A):
    for j, number in enumerate(element):
        number = int(number)
        sum += number
    SL.append(sum)
    sum = 0

print(SL)
