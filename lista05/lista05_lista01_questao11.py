# --------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009 
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030 
# Felipe Eduardo Silva de Almeida   1715310031 
# Felipe Guerreiro De Mello         1315120052 
# Silas castro de Mendonça          1715310066
#
# 11.Altere o programa anterior para mostrar no final a soma dos números.
# ----------------------------------------------------------------------

amount = 0
number1 = int(input('Digite um numero inteiro: '))
number2 = int(input('Digite outro numero inteiro: '))

if number1 < number2:
    while number1 < number2:
        number1 = number1 + 1
        if number1 < number2:
            print(number1)
            amount += number1

elif number2 < number1:
    while number2 < number1:
        number2 = number2 + 1
        if number2 < number1:
            print(number2)
            amount += number2

print('Soma dos numeros dentro do intervalo = %i' % amount)
