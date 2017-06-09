# -----------------------------------------------------------
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
# Faça um algoritmo em PORTUGOL para calcular o valor de S,
# dado por:
# 	S = 1/N + 2/(N-1) + 3/(N-2) + ... + (N-1)/2 + N/1
# sendo N fornecido pelo teclado.
# -----------------------------------------------------------
n = int(input())
h = 0
i = 1
while i <= n:
    h += 1/i
    i += 1
print(h)
