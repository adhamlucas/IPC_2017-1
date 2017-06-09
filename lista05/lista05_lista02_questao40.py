# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey         1715310059
# Edson de Lima Barros          1715310043
# Enrique Leão Barbosa Izel     1715310048
# Diego Reis figueira           1515070169
# Iury da Silva Coelho          1715310069
#
#40.Escreva um algoritmo em PORTUGOL que calcule o m.d.c.(máximo divisor comum)entre A e B (número inteiros e positivos)
#Esses dois valores são passados pelo usuário através do teclado.
#-----------------------------------------------------------------------------------------------------------------------

n = int(input("Digite o valor de A: "))
m = int(input("Digite o valor de B: "))

mdc = n

while n % mdc != 0 or m % mdc != 0:
    mdc = mdc - 1

print("MDC de A e B: %d" % mdc)
