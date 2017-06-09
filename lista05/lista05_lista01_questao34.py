# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey         1715310059
# Edson de Lima Barros          1715310043
# Enrique Leão Barbosa Izel     1715310048
# Diego Reis figueira           1515070169
# Diogo Roberto Duarte da Costa 1715310056
# Iury da Silva Coelho          1715310069
#
#34.Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo
#é aquele que é divisível apenas por um e por ele mesmo.
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#-----------------------------------------------------------------------------------------------------------------------

number = int(input("Digite um número inteiro para verificar se ele é primo: "))

aux = number
cont = 0

while aux > 1 :
    if (number % aux) == 0 :
        cont += 1
    aux -= 1    

if cont == 1 :
    print("O valor eh primo !")
else :
    print("O valor nao eh primo !")
