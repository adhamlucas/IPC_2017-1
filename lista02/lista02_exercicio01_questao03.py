# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Carlos Eduardo Tapudima de Oliveira       1715310030
# Frederico Victor Alfaia Rodrigues         1515200030
# Joelson Pereira Lima	                    1715310060
# Lucas Gabriel Silveira Duarte             1715310053
# Reinaldo da Silva Vargas	            1715310054
# Walter Nobre da Silva Conceição           1715310057
#
# 3 - Faça um Programa que peça dois números e imprima a soma.
# ----------------------------------------------------------
print ('---------------------Soma de 2 números---------------------')
try:
    a = input ('Digite o primeiro número: ')# a váriável A recebe o primeiro numero da soma via teclado
    a = int(a) #Convertendo o valor de A de String para Inteiro
    b = input ('Digite o segundo número: ')# a variábel B recebe o segundo número da soma via teclado
    b = int(b) #Convertendo o valor de b de String para Inteiro
    c = a + b # a variável C recebe a soma dos dois números
    print ('A soma: ',a,'  + ',b,' é igual a : ',c) #imprime o resultado da soma
except ValueError:
    print('Somente números são aceitos, tente novamente!')
