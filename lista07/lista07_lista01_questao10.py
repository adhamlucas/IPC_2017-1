# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Enrique Leão Barbosa Izel         1715310048
# Hugo Thadeu Silva Cardoso         1715310013
# Victor Summer Oliveira Pantaleao  1715310042
# Wilbert Luís Evangelista Marins   1715310055
# Yuri Leandro de Aquino Silva      1615100462
#
# 10)Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
# somente os elementos abaixo da diagonal secundária.
#---------------------------------------------------------------------------------
matriz = []

for i in range(10):

    matriz.append([0] * 10)

    for j in range(10):
        matriz[i][j] = int(input())

for i in range(10):

    for j in range(10):

        if i + j > 9:
            print(matriz[i][j])
