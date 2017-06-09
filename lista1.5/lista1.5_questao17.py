#-----------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Gabriel Barroso da Silva Lima     -|- 1715310011
#Wesley da Silva Rocha             -|- 1715310026
#Rodolfo gomes do nascimento       -|- 1515200550
#Victor Hugo de Oliveira Carreira  -|- 1715310063
#Diego Reis Figueira               -|- 1515070169
#Luis Gustavo Moura de Queiros     -|- 1715310037
#
#Faça um programa que receba o raio, calcule e mostre
# a) o comprimento de uma eefera, sabe-se que C = 2rR;
# b) a área de uma esfera, sabe-se que A = rR²;
# c) o volume de uma esfera, sabe-se que V = 3/4rR³
# ----------------------------------------------------------

import math

r = math.pi

raio = float(input("digite o valor do raio: "))
C = 2*raio*r
A = r*(raio**2)
V = (3*r*(raio**3))/4

print("Comprimento da esfera: ", C)
print("Área da esfera: ", A)
print("Volume da esfera: ", V)
