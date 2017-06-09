# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
# Ulisses Antonio Antonino da Costa         1515090555
# Rodrigo Duarte de Souza                   1115140049
# Victor Hugo de Oliveira Carreira          1715310063
#
# 16. Faça um programa que calcule as raízes de uma equação do segundo grau, 
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e 
# fazer as consistências, informando ao usuário nas seguintes situações:
# 
#   a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo 
#       grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# 
#   b) Se o delta calculado for negativo, a equação não possui raizes reais. 
#       Informe ao usuário e encerre o programa;
#       
#   c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
#       informe-a ao usuário;
#   
#   d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
# -------------------------------------------------------------------------------------- 

a = int(input("Digite o valor de a: "));

if a == 0:
    print("A equação não é do segundo grau. Programa encerrado.")
else:
    b = int(input("Digite o valor de b: "));
    c = int(input("Digite o valor de c: "));
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Delta é um valor negativo. A equação não possui raízes reais. Programa encerrado.")
    elif delta == 0:
        result = -b / 2 * a
        print("A equação possui apenas uma raiz e seu valor é: %2.1f" % result)
    else:
        result_1 = (-b + delta ** (1/2) ) / 2 * a
        result_2 = (-b - delta ** (1/2) ) / 2 * a  
        print("A equação possui duas raízes reais. São elas: %2.1f e %2.1f" % (result_1, result_2))
