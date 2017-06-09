# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 08
# Victor Summer Oliveira Pantaleao 1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luís Evangelista Marins  1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
# Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano, e
# um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano,
# escrever um algoritmo em PORTUGOL que seja capaz de calcular e iterativamente e
# no fim imprimir o tempo necessário para que a população do país A ultrapasse a
# população do país B.
# ----------------------------------------------------------
population_count_a = 5*10**6
birth_rate_a = 0.03

population_count_b = 7*10**6
birth_rate_b = 0.02

year_count = 0
while population_count_a < population_count_b:
    population_count_a *= 1+birth_rate_a
    population_count_b *= 1+birth_rate_b
    year_count += 1

print('Tempo necessário:', year_count)
