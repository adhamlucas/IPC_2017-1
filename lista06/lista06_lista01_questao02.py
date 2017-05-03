#---------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Diego Reis Figueira      		      	1515070169
# André Luis Laborda Neves            	1515070006
# Gabriel Nascimento de Oliveira  	  	1715310052
# Diogo Roberto Duarte da Costa 	  	1715310056
# João Vitor de Cordeiro B. Gonçalves 	1515140036
#
#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
#------------------------------------------------------------------------------

vet = []

for i in range (0,10):

    numbers = float(input())
    vet.append(numbers)

vet.reverse()
print(vet)


