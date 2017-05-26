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

