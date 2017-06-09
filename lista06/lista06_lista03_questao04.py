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
# Dados dois vetores x e y, ambos com n elementos, determinar o produto
# escalar desses vetores.
#
# ---------------------------------------------------------------------

n = int(input())
x = [float(k) for k in input().split()]
y = [float(k) for k in input().split()]

z = sum([x[i]*y[i] for i in range(n)])

print(round(z, 2))
