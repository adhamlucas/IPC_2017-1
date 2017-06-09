#-----------------------------------------------------------------------------------------------------------------------
#introdução a Programação de Computadores
#Prof. Jucimar Jr.
#Adham Lucas da Silva Oliveira       1715310001
#Erik Atilio Silva Rey               1715310059
#Enrique Leão Barbosa Izel           1715310048
#Guilherme Silva de Oliveira         1715310034
#Lukas Michel Souza Mota             1715310018
#Ulisses Antonio  Antonino da Costa  1515090555
#
#Faça um programa que receba dois números, calcule e mostre a divisão 
#do primeiro número pelo segundo. Sabe-se que o segundo número não pode
#ser zero, portanto não é necessário se preocupar com validações
#----------------------------------------------------------------------
number_1 = float(input("numerador: "))                       #receber o primeiro número (n=number)
number_2 = float(input("denominador (Não pode ser 0!!): "))  #receber o segundo número
division = (number_1/number_2)                                     #dividir o primeiro pelo segundo
print(division)                                        #resultado da divisão
