#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# Vitor Summer Oliveira Pantaleão 	1715310042
# Vítor Simões Azevedo 			1715310025
# Wesley da Silva Rocha			1715310026
# Wilbert Luís Evangelista Marins 	1715310055
# Yuri Leandro de Aquino Silva 		1615100462
#
# Faça um Programa que leia três números
# e mostre o maior e o menor deles.
#------------------------------------------------------------------------------

numb1 = float(input('Digite um numero: '))
numb2 = float(input('Digite um numero: '))
numb3 = float(input('Digite um numero: '))

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

print('O menor é: %d' %lower)
print('O maior é: %d' %higher)
