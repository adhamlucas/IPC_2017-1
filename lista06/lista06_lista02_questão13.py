#---------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Diego Reis Figueira      		      	1515070169
# André Luis Laborda Neves            		1515070006
# Gabriel Nascimento de Oliveira  	  	1715310052
# Diogo Roberto Duarte da Costa 	  	1715310056
# João Vitor de Cordeiro B. Gonçalves 		1515140036
#Escreva um algoritmo em PORTUGOL que receba dez números do usuário e
#armazene em um vetor o cubo de cada número. Após isso, o algoritmo deve imprimir
# todos os valores armazenados
# ----------------------------------------------------------

list = []
for i in range (0,10):
    numbers = float(input())**3
    list.append(numbers)
print(list)
