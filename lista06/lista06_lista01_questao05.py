#---------------------------------------------------------------------------

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
#---------------------------------------------------------------------------

limit = 20
vet = []
vet_pair = []
vet_odd = []

for element in range(limit):
    number = int(input('Digite o número %d: ' % (element+1)))
    vet.append(number)
    if number % 2 == 0:
        vet_pair.append(number)
    else:
        vet_odd.append(number)

print(vet)
print(vet_pair)
print(vet_odd)
