# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# 
# Vitor Summer Oliveira Pantaleão  1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luis Evangelista Marins  1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
# Faça um programa que calcule o mostre a média aritmética de N notas.
#-----------------------------------------------------------
grades_count = int(input())

grades_sum = 0
i = 0
while i < grades_count:
    grade = float(input())
    grades_sum += grade
    i += 1
grades_media = grades_sum/grades_count

print('Média aritmética:', grades_media)
