#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Natália Cavalcante Xavier              1715310021
# Tiago Ferreira Aranha	                  1715310047
#
#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
#---------------------------------------------------------------------------

limit = 5
count = 0
list = []

while count < limit:
    number = int(input('Digite um número: '))
    list.append(number)
    count += 1

for element in list:
    print(element, end=" ")
