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
#Faça um programa que receba uma temperatura em Celsius, celcule e mostre essa temperatura em Fahrenheit
#Sabe-se que F = 180(C + 32)/100

C = float(input("digite uma temperatura em Celsius"))
F = float(180*(C + 32)/100)
print("Temperatura em Fahreinheit: ", F)
