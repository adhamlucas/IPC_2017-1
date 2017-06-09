#----------------------------------------------------------------
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
#19.Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
#
#----------------------------------------------------------------
#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

number = 0
lowest = 0
biggest = 0
amount = 0
exi = 0

while ( exi == 0 ):

    number = input('Digite um número entre 0 e 1000 ou digite s para sair: ')

    if ( number != 's'):

        number = int(number)
        if ( number < 0) or ( number > 1000 ):

            print('Número %.2f inválido!' % number )

        elif( number < lowest ):

            lowest = number

        elif ( number > biggest ):

            biggest = number

    else:
        exi = 1

amount = lowest + biggest

print('O maior número é: %.2f' % biggest)
print('O menor número é: %.2f' % lowest)
print('A soma dos dois é: %.2f' % amount)
