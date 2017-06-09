#----------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Adham Lucas da Silva Oliveira         1715310059
# Alexandre Marques Uchôa               1715310028
# André Luís Laborda Neves              1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Diego Reis Figueira                   1515070169
# 

#Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R).
#A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.
#
#Entrada
# O arquivo de entrada contém um valor de ponto flutuante (dupla precisão), correspondente ao raio da esfera.
#
#Saída
# A saída deverá ser uma mensagem "VOLUME" conforme o exemplo fornecido abaixo, 
#com um espaço antes e um espaço depois da igualdade. 
#O valor deverá ser apresentado com 3 casas após o ponto.
#----------------------------------------------------------------------------------
radius = float(input())
pi = 3.14159
volume = 4/(3*pi*radius**3)

print('volume = %.3f' % volume)
