# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
# Ulisses Antonio Antonino da Costa         1515090555
# Rodrigo Duarte de Souza                   1115140049
# Victor Hugo de Oliveira Carreira          1715310063
#
# 06. Faça um Programa que leia três números 
# e mostre o maior deles.
# ---------------------------------------------------------- 

number1 = int(input("Digite o primeiro número: "));
number2 = int(input("Digite o segundo número: "));
number3 = int(input("Digite o terceiro número: "));

if number1 > number2 and number1 > number3:
    higher = number1
elif number2 > number1 and number2 > number3:
    higher = number2
elif number3 > number1 and number3 > number2:
    higher = number3
else:
    higher = "Impossível informar. Dois ou mais são iguais."

print("Maior número: ",higher)
