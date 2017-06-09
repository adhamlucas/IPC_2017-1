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
#28)Criar  um  algoritmo  que  leia  uma  matriz  ANxN(N10)e  verifique  (informe)  se  tal matriz é ou 
#não anti-simétrica
#(At=-A).
#
#-----------------------------------------------------------------------------------------------------------------------

linhas = int(input())
colunas = int(input())
matriz = []
matriz_transposta = []
matriz_oposta = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input()))
    matriz.append(linha)

for i in range(colunas):
    linha = []
    for j in range(linhas):
        linha.append(int(matriz[j][i]))
    matriz_transposta.append(linha)

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(matriz[i][j]) * -1)
    matriz_oposta.append(linha)

if matriz_oposta == matriz_transposta:
    print("Anti simetricas")
else:
    print("Não anti simetricas")


