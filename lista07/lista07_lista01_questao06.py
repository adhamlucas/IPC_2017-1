#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Antonio Diego Furtado da Silva            1715310004
# Fangyao                                   1115180236
# Matheus de Oliveira Marques               1515310514
# Reinaldo da Silva Varas                   1715310054
# Silas Castro de Mendonça                  1715310066
#
# Lista1. Questão 6) Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e imprima o
# produto dos elementos que estão abaixo da diagonal principal.
#----------------------------------------------------------------------------------------------------------------------

linhas = 10
colunas = 10
matriz = []

for l in range(linhas):
    linha = []
    for c in range(colunas):
        valor = int(input('Insira o elemento da posição [%i,%i] da matriz: ' % (l,c) ))
        #valor = int(2)
        linha.append(valor)
    matriz.append(linha)

li_inicio = 1
co = 0
produto = 1

while co <= colunas-2:
    li = li_inicio
    while li <= linhas-1:
        produto *= (matriz[li][co])
        li += 1

    li_inicio += 1
    co += 1

print("Produto: ", produto)