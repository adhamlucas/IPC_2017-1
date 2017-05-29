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
