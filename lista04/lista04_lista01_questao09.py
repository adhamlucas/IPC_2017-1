#-----------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Adham Lucas da Silva Oliveira         1715310059
# Alexandre Marques Uchôa               1715310028
# André Luís Laborda Neves              1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Diego Reis Figueira                   1515070169
#
# Faça um Programa que leia três números e mostre-os em ordem decrescente.
#-----------------------------------------------------------------------------
numb1 = float(input('Digite um número: '))
numb2 = float(input('Digite um número: '))
numb3 = float(input('Digite um número: '))

lower = numb1
if numb2 < lower:
    lower = numb2
if numb3 < lower:
    lower = numb3

higher = numb1
if numb2 > higher:
    higher = numb2
if numb3 > higher:
    higher = numb3

mid = numb1 + numb2 + numb3 - higher - lower

print(higher, mid, lower)
