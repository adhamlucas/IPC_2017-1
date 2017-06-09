# -*- coding: utf8 -*-
# ---------------------------------------------------------------------------
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
# Dada uma seqüência de n números, imprimi-la na ordem inversa à da leitura. 
#---------------------------------------------------------------------------

n = int(input("digite a quantidade de números: "))
lista = []

for i in range (0, n):
    
    numero = int(input("digite um número: "))
    lista.append(numero)
    
print(lista[::-1])