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
#Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada m², deve-se usar 18 W de potência, FAça um programa que receba as duas dimensões de um cômodo (em metros), calcule e mostre a sua área (em m²) e a potência de iluminação que deverá ser utilizada

m1 = float(input("digite a largura do cômodo: "))
m2 = float(input("digite o comprimento do cômodo: "))
W = m1*m2
print("Seu cômodo terá: ", m1*m2, " m² e usará: ", W*18, " W de potência de iluminação")
