#---------------------------------------------------------------------------------
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
# É um quebra‐cabeça, cujo objetivo do jogo é preencher os números de 1 a
# 9 em cada uma   das   células   vazias numa  grade  de 9×9,  constituída   por   3×3  
# subgrades chamadas   regiões.  Cada  coluna,   linha  e  região só pode  ter   um número 
# de cada um dos números de 1  a  9.
# Faça  um  programa    em  Java    que,    dado    um  jogo    Sudoku, representado 
# por uma classe que contem  uma matriz  9x9,    verifica    se  o   jogo    está    ou  não correto.
#---------------------------------------------------------------------------------

casos = int(input())
for indice in range(casos):
    condicao = set(range(1, 10))
    n = 9
    matriz = []
    for i in range(n):
        linha = [int(x) for x in input().split()]
        matriz.append(linha)

    correto = True
    for linha in matriz:
        if not set(linha) == condicao:
            correto = False

    for j in range(n):
        coluna = []
        for i in range(n):
            coluna.append(matriz[i][j])
        if not set(coluna) == condicao:
            correto = False

    for a in range(3):
        for b in range(3):
            valores = []
            for i in range(3):
                for j in range(3):
                    valores.append(matriz[3*a+i][3*b+j])
            if not set(valores) == condicao:
                correto = False

    
    print("Instancia {}".format(indice+1))
    print("SIM" if correto else "NAO")
    print()
