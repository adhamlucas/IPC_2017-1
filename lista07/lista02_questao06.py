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
#6.Dada uma matriz  Amxn, imprimir o número de linhas e o número de colunas nulas da matriz.
#
#Exemplo: m = 4 e n = 4
#tem 2 linhas nulas e 1 coluna nula.
#
#-----------------------------------------------------------------------------------------------------------------------

linhas = int(input())
colunas = int(input())
matriz = []
zeros = 0
colunas_nulas = 0
linhas_nulas = 0
c = 0
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input()))
    matriz.append(linha)

while c < (colunas):
    for j in range(colunas):
        if matriz[c][j] == 0:
            zeros += 1

    c += 1
    if zeros == linhas:
        linhas_nulas += 1
    zeros = 0
c = 0
while c < (linhas):
    for j in range(linhas):
        if matriz[j][c] == 0:
            zeros += 1

    c += 1
    if zeros == linhas:
        colunas_nulas += 1
    zeros = 0

print("Tem",linhas_nulas,"nulas e",colunas_nulas,"nulas")


