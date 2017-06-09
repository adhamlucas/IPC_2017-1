# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 10
# Walter Nobre da Silva Conceição 1715310057
#
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


first = input('write the price of the first product: R$ ')
first = int(first)
second = input('write de price of the second product: R$ ')
second = int(second)
third = input('write the price of the third product: R$ ')
third = int(third)

if first < second < third  or first < third < second and first:
    print('the first is the cheapest product, so buy it')
elif second < first < third or second < thrid < first:
    print('the second is the cheapest product, so buy it')
elif third < first < second or third < second < first:
    print('The third is the cheapest product, so buy it')
else:
    print('all products have the same price')


