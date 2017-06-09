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
# Escreva um algoritmo em PORTUGOL que determine se dois valores inteiros e
# positivos A e B são primos entre si. (dois números inteiros são ditos primos entre si,
# caso não exista divisor comum aos dois números). 
#----------------------------------------------------------------

number_a = float(input("Digite um numero: "))
number_b = float(input("Digite outro numero: "))
c = 1
summation = 0
while c <= number_a and c <= number_b:
    if (number_a % c == 0) and (number_b % c == 0):
        summation = summation + 1
    c += 1
if summation <= 1:
    print("São primos entre si")
else:
    print("Não são primos entre si")
