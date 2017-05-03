# ---------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Antônio Diego Furtado da Silva        1715310004
# Aracille de Souza Barbosa             1315120206
# Marcus Vinicius Paes da Silva Santos  1515070060
# Silas Castro de Mendonça              1715310066
# Wesley da Silva Rocha                 1715310026
#
# Escreva um algoritmo em PORTUGOL que receba oito números do usuário
# e armazene em um vetor o logaritmo de cada um deles na base 10. Caso
# não seja possível calcular o valor para o número digitado, o número
# -1 deve ser atribuído ao elemento do vetor. Após isso, o algoritmo
# deve imprimir todos os valores armazenados.
#
# ---------------------------------------------------------------------

numeros = [float(x) for x in input().split()]

from math import log
logaritmos = [log(x) if x > 0 else -1 for x in numeros]

for logaritmo in logaritmos:
    print(round(logaritmo, 2))
