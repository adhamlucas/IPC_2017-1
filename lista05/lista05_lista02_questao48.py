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
#48) Faça um algoritmo em PORTUGOL para calcular o valor de S, dado por:
# s = (1/n)+(2/(n-1)...(n/1)
# sendo N fornecido pelo teclado. 
#
#----------------------------------------------------------------
number_n = int(input("Digite um número: "))
count = 1
number_s = 0
final = number_n
while count <= final:
    number_s = number_s + (count/number_n)
    count += 1
    number_n -= 1
print (number_s)
