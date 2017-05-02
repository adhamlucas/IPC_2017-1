#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Natália Cavalcante Xavier               1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# Fazer um algoritmo em Python que:
# a) Leia o valor inteiro de n (n  1000) e os n valores de uma variável composta A de
# valores numéricos, ordenados de forma crescente;
# b) Determine e imprima, para cada número que se repete no conjunto, a quantidade de
# vezes em que ele aparece repetido;
# c) Elimine os elementos repetidos, formando um novo conjunto;
# d) Imprima o conjunto obtido no item c.
#---------------------------------------------------------------------------

n = int(input("digite a quantidade de números: "))
digitados = []
repete = 0

for i in range (0, n):
    
    numero = int(input("digite o número: "))
    digitados.append(numero)

i = 1
digitados.append(digitados[0]-1)

while i < n:
    
    while digitados[i] == digitados[i-1]:
        
        repete += 1
        digitados.remove(i)
        n -= 1
        
    else:
    
        if repete > 0:
        
            print ("número", digitados[i-1], "repete", repete, "vez(es)")
            repete = 0
       
    i += 1

digitados.remove(digitados[0]-1)    

for i in range (0, n):

    print (digitados[i])