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
# Faça um Programa que peça um número correspondente a um determinado 
# ano e em seguida informe se este ano é ou não bissexto.
#------------------------------------------------------------------------------

year = int(input('Insira um ano: '))

isLeapYear = False
if year%400 == 0 or (year%4 == 0 and year%100 != 0):
	isLeapYear = True

if isLeapYear == True:
	print('%d é um ano bissexto!' %year)
else:
	print('%d não é um ano bissexto.' %year)
