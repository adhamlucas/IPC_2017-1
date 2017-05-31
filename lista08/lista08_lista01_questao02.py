#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Fang Yao                           1115180236
# Enrique leão Barbosa Izel          1715310048
# Hugo Thadeu Silva Cardoso          1715310013
# Victor Summer Oliveira             1715310042
# Wilbert Luis Evangelista Marins    1715310055
# Guilherme Silva de Oliveira        1715310034

# Faça um programa para imprimir:
# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n
# para um n informado pelo usuário.
# Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
#---------------------------------------------------------------------------

from lista08.ipc import vetor

quantidade = int(input("Digite a quantidade: "))
resultado = vetor.SequencialAbaixoDiagonalPrincipal(quantidade)
print(resultado)
