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
# Implementar um algoritmo para calcular o valor de e^x.
# O valor de X deverá ser digitado. O valor será calculado
# pela soma dos 15 primeiros termos da série a seguir:
#	e^x = 1 + x + (x^2)/2! + (x^3)/3! + (x^4)/4! + ...
#
# -----------------------------------------------------------
x = int(input())

e = 0
numerator = 1
denominator = 1
i = 1
while i <= 15:
    e += numerator/denominator
    numerator *= x
    denominator *= i
    i += 1
print(e)
