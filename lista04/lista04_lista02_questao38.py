# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
# Victor Hugo de Oliveira Carreira          1715310063
#
# URI Online Judge | 1038
# Lanche
#
# Com base na tabela abaixo, escreva um programa que leia o código de um item 
# e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
# 
#  Codigo           especificaçao        preço
#    1             Cachorro Quente      R$ 4,00
#    2                X-Salada          R$ 4,50
#    3                X-Bacon           R$ 5,00
#    4             Torrada Simples      R$ 2,00
#    5              Refrigerante        R$ 1,50
# 
#Entrada
#
# O arquivo de entrada contém dois valores inteiros correspondentes ao código 
# e à quantidade de um item conforme tabela acima.
#
# Saída
#
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor 
# a ser pago, com 2 casas após o ponto decimal.
# --------------------------------------------------------------------------------------

code = int(input())
amount = float(input())

if code == 1:
    price = 4.00
elif code == 2:
    price = 4.50
elif code == 3:
    price = 5.00
elif code == 4:
    price = 2.00
else:
    price = 1.50

print("Total: R$ %2.2f" % float(price * amount))
