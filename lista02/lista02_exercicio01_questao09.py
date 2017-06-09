#---------------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Prof. Jucimar Jr.
#Adham Lucas da Silva Oliveira       1715310001
#Erik Atilio Silva Rey               1715310059
#Enrique Leão Barbosa Izel           1715310048
#Ulisses Antonio  Antonino da Costa  1515090555
#Lukas Michel Souza Mota             1715310018
#Guilherme Silva de Oliveira         1715310034
#
#Faça um Programa que peça a temperatura em graus Farenheit,
#transforme e mostre a temperatura em graus Celsius.
#
#    C = (5 * (F-32) / 9).
#----------------------------------------------------------------------
print('-Conversão de Graus Farenheit para Celsius-')
farenheit = float(input('Digite o valor em Farenheit:'))
celsius = (5*(farenheit-32)/9)
print('O resultado é:',celsius,'°C')