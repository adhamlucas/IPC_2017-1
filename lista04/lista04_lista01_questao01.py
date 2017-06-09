#--------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Diogo Roberto Duarte da Costa     1715310056
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro de Mello         1315120052
# Frederico Victor Alfaia Rodrigues 1515200030
# Gabriel Barroso da Silva Lima     1715310011
#
# Faça um Programa que peça dois números e imprima o maior deles. 
#-------------------------------------------------------------------------------------

number1 = float(input("Digite um valor: "))
number2 = float(input("Digite outro valor: "))

if number1 > number2:
    print(number1, " é maior que ", number2)
else:
    if number2 > number1:    
        print(number2, " é maior que ", number1)  
    else:
        print(number2, " e ", number1, " são iguais.")
