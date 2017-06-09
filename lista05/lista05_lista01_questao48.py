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
# Faça um programa que peça um numero inteiro positivo e em
# seguida mostre este numero invertido.
# ----------------------------------------------------------
number = int(input())
new_number = 0

while number:
    new_number = 10*new_number + number%10
    number //= 10

print('=>', new_number)
