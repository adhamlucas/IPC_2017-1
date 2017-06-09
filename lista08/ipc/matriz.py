# Biblioteca de funções para as matrizes

import random


# função para criar matriz de ordem n x m
def cria_matriz(n, m):
    matriz = []
    for i in range(n):
        list = []
        for j in range(m):
            # serão inseridos valores aleatórios na matriz (entre 1 e 4)
            value = random.randint(1, 4)
            list.append(value)
        matriz.append(list)
    return matriz


# função para criar matriz quadrada de ordem n
def cria_matriz_quadrada(n):
    matriz = []
    for i in range(n):
        list = []
        for j in range(n):
            # serão inseridos valores aleatórios na matriz (entre 1 e 4)
            value = random.randint(1, 4)
            list.append(value)
        matriz.append(list)
    return matriz


# função para imprimir uma matriz de qualquer ordem
def imprime_matriz(matriz):
    for i in matriz:
        print(i)

        
#função para multiplicar duas matrizes(matriz A e matriz B) e retornar a matriz resultante(matriz AxB)
def produto_matricial(matriz1, matriz2):

    matriz_result = []

    linhas = len(matriz1)
    colunas = len(matriz2[0])

    # verifica se o numero de colunas de A
    # é igual ao número de linhas de B
    if (len(matriz1[0])) == (len(matriz2)):

        for i in range(linhas):
            matriz_result.append([])
            for j in range(colunas):
                value = 0
                for aux in range(len(matriz2)):
                    value += matriz1[i][aux] * matriz2[aux][j]

                matriz_result[i].append(value)

        return matriz_result

    else:
        return 'O produto não é possível'

# função para imprimir os índices de uma matriz de qualquer ordem
def imprime_matriz_indices(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print("%d%d" % (i, j), end=" ")
        print()


# lista 1 questão 3
# função para imprimir retângulo com uma matriz
def imprime_retagulo_matriz(matriz):
    for i in range(len(matriz)):

        for j in range(len(matriz[0])):

            largura = len(matriz[i]) - 1
            altura = len(matriz) - 1

            if (j == 0 and i == altura) or (j == largura and i == 0) or (i == altura and i == 0) or (
                            i == 0 and j == 0) or (
                            i == altura and j == largura):
                caractere = "+"
            elif (j == largura):
                caractere = "|"
            elif (i == 0):
                caractere = "-"
            elif (j == 0):
                caractere = "|"
            elif (i == altura):
                caractere = "-"

            else:
                caractere = " "

            print("%s" % (caractere), end=" ")

        print()


# função que pultiplica cada elemento da matriz por um número n e retorna um vetor
def multiplica_matriz_por_inteiro(matriz, n):
    vetor = []

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            vetor.append(matriz[i][j] * n)

    return vetor


# lista 2 questão 28
# função que retorna o maior elemento da diagonal principal

def maior_da_diagonal_principal(matriz):
    maior = matriz[0][0]
    for i, n in enumerate(matriz):
        for j, m in enumerate(n):
            if i == j:
                if j > maior:
                    maior = j
    return maior


# função que retorna um vetor com os elementos da diagonal principal

def diagonal_principal(matriz):
    vetor = []
    for i, n in enumerate(matriz):
        for j, m in enumerate(n):
            if i == j:
                vetor.append(matriz[i][j])
    return vetor


# função que retorna um vetor com os elementos da diagonal secundária

def diagonal_secundaria(matriz):
    ordem = len(matriz)
    j = ordem - 1
    secundaria = []
    for i in range(ordem):
        secundaria.append(matriz[i][j])
        j -= 1
    return secundaria


# função que retorna a média dos elementos da diagonal principal

def media_diagonal_principal(matriz):
    vetor = []
    soma = 0
    c = 0

    for i, n in enumerate(matriz):
        for j, m in enumerate(n):
            if i == j:
                soma += matriz[i][j]
                c += 1
    return soma / c


# função que retorna a média dos elementos da diagonal secundária

def media_diagonal_secundaria(matriz):
    ordem = len(matriz)
    j = ordem - 1
    soma = 0
    c = 0
    for i in range(ordem):
        soma += matriz[i][j]
        j -= 1
        c += 1
    return soma / c

# lista02_questao37 função que retorna o minimax de uma matriz #
def funcao_minimax(mat):
   minimax = mat[0][0]
   maior = mat[0][0]
   for i in range(10):
       menor = mat[i][0]
       maior_aux = maior
       for j in range(10):
           if mat[i][j] > maior_aux:
               maior_aux = mat[i][j]
           if mat[i][j] < menor:
               menor = mat[i][j]
       if maior_aux > maior:
           minimax = menor
           maior = maior_aux
   return minimax

# lista02_questao36 função que retorna a soma da multiplica linha por diagonal #
def multiplica_linha(mat):
   for i in range(6):
       di = mat[i][i]
       for j in range(6):
           mat[i][j] *= di
   return mat

# Lista 2 questão 27 retorna o menor item da diagonal secundaria
def menor_item_secundaria(matriz):
    secundaria = diagonal_secundaria(matriz)
    menor = min(secundaria)

    return menor


def diferenca_m_por_n(A, B, C):

    C = 4*[6*[None]]

    for i in range(4):
        for j in range(6):
            C[i][j] = A[i][j] - B[j][i]

    return C

# lista 2 questão 26
def soma_matriz_parcial(matriz, linha, coluna):
    n = len(matriz)
    m = len(matriz[0])
    soma = 0
    for i in range(n):
        soma += matriz[i][coluna]
    for j in range(m):
        soma += matriz[linha][j]
    return soma - matriz[linha][coluna]

# lista 2 questão 39
def soma_abaixo_diagonal_principal(matriz):
    n = min(len(matriz), len(matriz[0]))
    soma = 0
    for i in range(n):
        for j in range(i):
            soma += matriz[i][j]
    return soma

def media_abaixo_diagonal_principal(matriz):
    n = min(len(matriz), len(matriz[0]))
    qtd = (n*(n-1))//2
    return soma_abaixo_diagonal_principal(matriz)/qtd

# lista 2 questão 40
def soma_acima_diagonal_principal(matriz):
    n = len(matriz)
    m = len(matriz[0])
    soma = 0
    for i in range(n):
        for j in range(i+1, m):
            soma += matriz[i][j]
    return soma

# funcao que retorna a soma dos elementos

def soma_elementos_matriz(matriz):
    acumulador = 0
    for i in matriz:
        for j in i:
            acumulador += j
    return acumulador


# lista 2 questão 26

def soma_linha5_coluna3(matriz):
    soma = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):

            if i == 4 or j == 2:
                soma += matriz[i][j]
    return soma


# função que cria matriz zerada
def cria_matriz_zerada(n, m):
    matriz = []
    linha = []
    for i in range(n):
        linha.append(0 * m)
        matriz.append(linha)
    return matriz



# função que soma as diagonais

def soma_diagonais(matriz):
    vetor = []
    soma = 0
    c = 0
    ordem = len(matriz)
    j = ordem - 1

    for i, n in enumerate(matriz):
        for j, m in enumerate(n):
            if i == j:
                soma += matriz[i][j]
    for i in range(ordem):
        soma += matriz[i][j]
        j -= 1

    return soma

# lista 2 questão 29
def produto_matriz(matriz1, matriz2):
    matrizvirgem = []
    for i in range(len(matriz1)):
        vetbranco = []
        for j in range(len(matriz2[0])):
            vetbranco.append((matriz1[i][0] * matriz2[0][j]) + (matriz1[i][1] * matriz2[1][j]))
        matrizvirgem.append(vetbranco)
    return matrizvirgem


