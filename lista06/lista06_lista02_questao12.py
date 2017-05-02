#---------------------------------------------------------------------------
# Introdu��o a Programa��o de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Nat�lia Cavalcante Xavier               1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# Escreva um algoritmo em Python o de cada
# n�mero. Ap�s isso, o algoritmo deve
# imprimir todos os valores armazenados.
#---------------------------------------------------------------------------

tamanho = 10
quadrado = []

for i in range (0, tamanho):

    numero = int(input("digite um valor: "))
    quadrado.append(numero**2)

print ("quadrado dos valores apresentados:")

print(quadrado)