#---------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Diego Reis Figueira      		      	1515070169
# André Luis Laborda Neves            		1515070006
# Gabriel Nascimento de Oliveira  	  	1715310052
# Diogo Roberto Duarte da Costa 	  	1715310056
# João Vitor de Cordeiro B. Gonçalves 		1515140036
#
#Dado um conjunto de 100 valores numéricos disponíveis num meio de entrada qualquer,
# fazer um algoritmo em PORTUGOL para armazená-los numa variável composta B, e calcular
# e imprimir o valor do somatório dado a seguir:
# S(b1 -b100 )3 (b2 -b99 )3 (b3 -b98 )3 ...(b50 -b51 )3
#-------------------------------------------------------------------------
list=[]
j=99
for i in range (100):
    x=int(input())
    list.append(x)
    soma=0
for i in range (50):
    a=list[i]
    b=list[j]
    soma+=(a-b)**3
    j-=1
print(soma)