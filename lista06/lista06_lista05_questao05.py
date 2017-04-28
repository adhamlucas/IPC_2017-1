#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Alexandre Marques Uchôa           1715310028
# Carlos Eduardo T. de Oliveira     1715310030
# Hugo Tadeu Silva Cardoso          1715310013
# Judá Salazar Braga                1515200050
# Kethelen Tamara Braba Barbosa     1525212002
#
# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

count = 1
number = 0
numbers = []
par = []
impares = []

while count <= 20 :
    number = int(input('Digite o %i número: ' % count))
    numbers.append(number)

    if (number % 2 == 0):
        par.append(number)

    else:
        impares.append(number)

    count += 1

print('Todos os números: ', numbers)
print('Números pares: ', par)
print('Números ímpares: ', impares)