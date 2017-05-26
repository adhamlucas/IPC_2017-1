# Biblioteca de funções para as matrizes

import random

def cria_matriz(n, m):
    matriz = []
    for i in range(n):
        list = []
        for j in range(m):
            value = random.randint(1, 4)
            list.append(value)
        matriz.append(list)
    return matriz