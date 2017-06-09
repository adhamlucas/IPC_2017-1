#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# Vitor Summer Oliveira Pantaleão   1715310042
# Vítor Simões Azevedo              1715310025
# Wesley da Silva Rocha             1715310026
# Wilbert Luís Evangelista Marins   1715310055
# Yuri Leandro de Aquino Silva      1615100462
#
# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação
# de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem cor-
# respondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de
# numero negativo.
#------------------------------------------------------------------------------

from math import sqrt
a, b, c = map(float, input().split())
delta = b*b -4*a*c

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b + sqrt(delta)) / (2*a)
    r2 = (-b - sqrt(delta)) / (2*a)
    print('R1 = {0:.5f}'.format(r1))
    print('R2 = {0:.5f}'.format(r2))
