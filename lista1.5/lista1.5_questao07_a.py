# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Prof. Jucimar Jr
#
#Alexandre Marques Uchôa               1715310028
#Jandinne Duarte de Oliveira           1015070265
#Uriel Brito Barros                    1515120558
#Roberta de Oliveira da cruz           0825070169
#Evandro Padilha Barroso Filho         1715310009
#Marcus Vinícius Paes da Silva Santos  1515070060
#
# 7 - Faça um programa que receba o peso de uma pessoa, calcule e mostre:
#a)o novo peso se a pessoa engordar 15% sobre o peso digitado;
# ----------------------------------------------------------
weight = float(input('Digite seu peso em quilogramas'))
weightabove = (weight * 1.15)
print('se a pessoa engordar 15% o peso sera', round(weightabove, 2) )
