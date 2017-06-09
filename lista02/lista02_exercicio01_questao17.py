# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Diego Reis Figueira                1515070169
# Gabriel Barroso da Silva Lima      1715310011
# Rodolfo gomes do nascimento        1515200550
# Victor Hugo de Oliveira Carreira   1715310063
# Wesley da Silva Rocha              1715310026
#Luis Gustavo Moura de Queiros       1715310037
#
# Faça um Programa para uma loja de tintas. O programa deverá pedir o
# tamanho em metros quadrados da área a ser pintada. Considere que a
# cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os
# respectivos preços em 3 situações:
#   a. comprar apenas latas de 18 litros;
#   b. comprar apenas galões de 3,6 litros;
#   c. misturar latas e galões, de forma que o preço seja o menor.
#   Acrescente 10% de folga e sempre arredonde os valores para cima,
#   isto é, considere latas cheias.
# ----------------------------------------------------------

# A função ceil(x) retorna o menor número inteiro maior que x.
# Ex: ceil(2.1) = 3, ceil(1) = 1
from math import ceil

area = float(input(
       'Insira o tamanho da área a ser pintada em metros quadrados: '))
necessary_liters = area/6
# Margem acrescentada (folga)
necessary_liters += 0.1*necessary_liters

# Uma lata contém 18 litros de tinta e custa R$ 80,00
necessary_cans = ceil(necessary_liters/18)
cans_total_price = 80*necessary_cans
print('Comprando apenas latas =', cans_total_price)

# Um galão contém 3,6 litros de tinta e custa R$ 25,00
necessary_gallons = ceil(necessary_liters/3.6)
gallons_total_price = 25*necessary_gallons
print('Comprando apenas galões =', gallons_total_price)

# Como a há mais litro por real na lata, é necessário ter no mínimo
# necessary_liters//18 de latas para atingir o lucro máximo.
# A quantidade restante de tinta pode ser completa por mais uma lata
# ou por mais alguns galões. Se for necessário 4 ou mais galões, é
# melhor escolhar a lata, pois:
#     2*80 + 0*25 < 1*80 + 4*25
#             160 < 180
if ceil((necessary_liters%18)/3.6) < 4:
    necessary_cans = necessary_liters//18
    necessary_gallons = ceil((necessary_liters%18)/3.6)
else:
    necessary_cans = necessary_liters//18 + 1
    necessary_gallons = 0

cans_total_price = 80*necessary_cans
gallons_total_price = 25*necessary_gallons
best_price = cans_total_price+gallons_total_price
print('Misturando latas e galões (preço ótimo) =', int(best_price))
