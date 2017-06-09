# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 08
# Victor Summer Oliveira Pantaleao 1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luís Evangelista Marins  1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
#Faça um programa que leia 5 números e informe a soma e a mé-
#dia dos números.
#-----------------------------------------------------------
values_sum = 0
values_count = 0
while values_count < 5:
    current_value = float(input())
    values_sum += current_value
    values_count += 1
values_media = values_sum/values_count

print('Soma =', values_sum)
print('Media =', values_media)
