# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey         1715310059
# Edson de Lima Barros          1715310043
# Enrique Leão Barbosa Izel     1715310048
# Diego Reis figueira           1515070169
# Diogo Roberto Duarte da Costa 1715310056
# Iury da Silva Coelho          1715310069
#
# 10.Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
# intervalo compreendido por eles.
#-----------------------------------------------------------------------------------------------------------------------

number1 = int(input('Defina o inicio:'))
number2 = int(input('Defina o fim: '))

while number1 < number2:
    number1 = number2 + 1
    print(number1)


