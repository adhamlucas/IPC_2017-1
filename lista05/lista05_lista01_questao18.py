#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Evandro Padilha Barroso Filho     1715310009 
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030 
# Felipe Eduardo Silva de Almeida   1715310031 
# Felipe Guerreiro De Mello         1315120052 
# Silas castro de Mendonça          1715310066
#
# 18. Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dos valores.
#
#----------------------------------------------------------------

bigger = 0
summation = 0
set_numbers = int(input("Digite quantos numeros farão parte do conjunto: "))
c = 1
while c <= set_numbers:
    number = int(input("Digite o %dº número: " % c))
    if c == 1:
        smaller = number
    if number < smaller:
        smaller = number
    if number > bigger:
        bigger = number
    summation = summation + number
    c = c + 1
print("menor = ", smaller)
print("maior = ", bigger)
print("soma = ", summation)
