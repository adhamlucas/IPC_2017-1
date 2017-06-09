#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Diogo Roberto Duarte da Costa     1715310056
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro de Mello         1315120052
# Frederico Victor Alfaia Rodrigues 1515200030
# Gabriel Barroso da Silva Lima     1715310011
# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 
#---------------------------------------------------------------

numero = input("digite um numero menor que 1000 ---> ")
numero_str = str(numero)
qt_numero = len(numero_str)
 
if qt_numero == 3:
    centena = numero_str[0:1]
    dezena = numero_str[1:2]
    unidade = numero_str[2:3]
    print numero_str+" = "+centena+" centenas , "+dezena+" dezenas, "+unidade+ " unidades"
 
if qt_numero == 2:
    dezena = numero_str[0:1]
    unidade = numero_str[1:2]
    print numero_str+" = "+dezena+" dezenas, "+unidade+ " unidades"
 
if qt_numero == 1:
    unidade = numero_str[0:1]
    print numero_str+" = "+unidade+ " unidades"
