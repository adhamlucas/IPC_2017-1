# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
#
# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#   
#   a) Álcool:
#       até 20 litros, desconto de 3% por litro
#       acima de 20 litros, desconto de 5% por litro
#   b) Gasolina:
#       até 20 litros, desconto de 4% por litro
#       acima de 20 litros, desconto de 6% por litro
#
#   Escreva um algoritmo que:
#       - leia o número de litros vendidos, 
#       - o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
#       - calcule e imprima o valor a ser pago pelo cliente sabendo-se que:
#           - o preço do litro da gasolina é R$ 2,50 
#           - e o preço do litro do álcool é R$ 1,90
#
# -------------------------------------------------------------------------------------- 

liters = int(input("Informe o número de litros vendidos: "));
fuel_type = input("Selecione o tipo de combustível: \nA - Álcool \nG - Gasolina\n")

if fuel_type == "A":
    if liters <= 20:
        discount = 0.03
    else:
        discount = 0.05
    total = liters - liters * discount
elif fuel_type == "G":
    if liters <= 20:
        discount = 0.04
    else:
        discount = 0.06
    total = liters - liters * discount

print("O valor a ser pago pelo cliente é",total)
