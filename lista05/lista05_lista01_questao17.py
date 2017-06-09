#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058
#
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
#   Ex.: 5!=5.4.3.2.1=120
#----------------------------------------------------------------------------

number = int(input("Informe um número: "))
cont = 1
factorial = 1 
while cont <= number:
    factorial = factorial*cont
    cont = cont+1
print(factorial)
