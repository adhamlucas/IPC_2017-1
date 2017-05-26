# Biblioteca de funções para os vetores

import random

# lista 1 questão 1
# Edson de Lima Barros   1715310043
# Tiago Ferreira Aranha  1715310047
# Vitor Simôes Azevedo   1715310025

def imprimir_questao1(n):
    res = ""
    c = 1

    for i in range(n):
        res += c * (str(i + 1) + " ") + "\n"
        c += 1

    return res

# função para retornar uma lista a partir de uma entrada em sequência
# Ex.: Em um input: 4 10 PM, retornará a lista: ['4', '10', 'PM']

def get_as_uri(valores):
    valores = valores.split()

    return valores


# função para retornar uma lista de inteiros a partir de uma entrada em sequência
# Ex.: Em um input: 4 5 6 3 2, retornará a lista: [4, 5, 6, 3, 2]

def get_as_uri_inteiros(valores):
    valores = valores.split()
    valores_int = []

    for i in valores:
        valores_int.append(int(i))

    return valores_int