#-----------------------------------------------------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Alexandre Marques Uchôa               1715310028
#Jandinne Duarte de Oliveira           1015070265
#Uriel Brito Barros                    1515120558
#Roberta de Oliveira da cruz           0825070169
#Evandro Padilha Barroso Filho         1715310009
#
##
#Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba um salário fixo
#de um funcionário e o valor de suas vendas, calcule e mostre a comissão e o salário final do funcionário
#-----------------------------------------------------------------------------------------------------------------------
fix_salary = float(input('Digite o seu salário fixo'))
commission = float(input('Quanto você vendeu esse mẽs?'))
max_com = (commission*0.04)
salary = (max_com + fix_salary)
print ('Sua comissão é', max_com)
print ('Seu salário é',salary)
