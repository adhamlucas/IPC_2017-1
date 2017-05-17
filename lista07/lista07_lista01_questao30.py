##----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Aracille de Souza Barbosa                 1315120206
# kethelen Tamara Braga Barbosa      	    1525212002
# Marcus Vinicius Paes da Silva Santos      1515070060
# Ulisses Antonio Antonino da Costa         1515090555
# Uriel Brito Barros                        1515120558
#
#
#
#Criar um algoritmo que receba duas matrizes A(CxD) e B(ExF) (C, D, E, F <=6). Esse
#algoritmo deve verificar se o produto matricial de A por B é possível (D=E). Caso
#seja possível, calcular o tal produto, imprimindo a matriz G(CxF) resultado.

linhas_A = int(input("Quantidade de linhas para A "))
colunas_A = int(input("Quantidade de colunas para A "))
linhas_B = int(input("Quantidade de linhas para B "))
colunas_B = int(input("Quantidade de colunas para B "))
matriz_A = []
matriz_B = []
matriz_G = []

for i in range(linhas_A):
    linha = []
    for j in range(colunas_A):
        linha.append(int(input()))
    matriz_A.append(linha)

for i in range(linhas_B):
    linha = []
    for j in range(colunas_B):
        linha.append(int(input()))
    matriz_B.append(linha)


if colunas_A == linhas_B:
    print("Produto matricial possível")
else:
    print("Produto matricial impossível")

for i in range(linhas_A):
    linha = []
    for j in range(colunas_A):
        elemento = 0
        for k in range(colunas_A):
            elemento += matriz_A[i][k] * matriz_B[k][j]
        linha.append(elemento)
    matriz_G.append(linha)

print(matriz_G)