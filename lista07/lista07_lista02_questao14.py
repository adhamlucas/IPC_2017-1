#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Joelson Pereira Lima 			        1715310060
# Víctor Hugo de Oliveira Carreira      1715310063
#
#14.  (POLI 94) Os elementos aij de uma matriz inteira Anxn representam os custos de transporte da cidade i para a cidade j. Dados n itinerários, cada um com k cidades, calcular o custo total para cada itinerário.
#
#    Exemplo:
#
#    O custo do itinerário 0 3 1 3 3 2 1 0 é
#
#    a03 + a31 + a13 + a33 + a32 + a21 + a10 = 3 + 1 + 400 + 5 + 2 + 1 + 5 = 417
#
#-----------------------------------------------------------------------------------------------------------------------
colunas = int(input())
linhas = int(input())
matriz = []
custo = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input()))
    matriz.append(linha)
print(matriz)

locais = input().split()

for i in range(len(locais)-1):
    custo += matriz[int(locais[i])] [int(locais[i+1])]

print(custo)




