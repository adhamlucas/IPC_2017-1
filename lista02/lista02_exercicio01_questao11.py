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
#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo .
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo.
#-----------------------------------------------

a = int(input("Digite um número inteiro: ")) #primeiro número é imputado
b = int(input("Digite um número inteiro: ")) #segundo número é imputado
c = float(input("Digite um número real: ")) #terceiro número é imputado
print("o produto do dobro do primeiro com metade do segundo: ", (a*2)*(b/2)) #a primeira operação é feita e mostrada na tela
print("a soma do triplo do primeiro com o terceiro: ", a*3+c) #a segunda operação é feita e mostrada na tela
print("o terceiro elevado ao cubo: ", c**3) #a terceira operação é feita e mostrada na tela
