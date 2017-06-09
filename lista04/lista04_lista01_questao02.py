# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Guilherme Silva de Oliveira       1715310034
# Gabriel Nascimento de Oliveira    1715310052
# Gabriel de Queiroz Souza          1715310044
# Hugo Thadeu Silva Cardoso         1715310013
# Ian Gabriel Costa Machado         1215120276
#
# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# ----------------------------------------------------------------------------------------------------------------------
A = float(input('digite um valor'))

if A > 0:
    print('O valor é positivo')
else:
    if A < 0:
        print('O valor é negativo')
    else:
        print('O valor é neutro')
