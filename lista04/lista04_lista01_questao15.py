#-----------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

#Reinaldo da Silva Vargas 1715310054
#Natalia Cavalcante Xavier 1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Vinicius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
#-------------------------------------------------------------------------------------
side1=float(input("Digite o valor do lado"))
side2=float(input("Digite outro valor do lado"))
side3=float(input("Digite mais um valor do lado"))

if side1+side2>side3:
    print(" É possivel formar um triangulo ")
else:
    print("nao é possivel formar um triangulo")
if side1==side2==side3:
    print("Triangulo equilatero")
if side1==side2!=side3 or side1==side3!=side2:
    print("Triangulo isosceles")
if side1!=side2!=side3!=side1:
    print("Triangulo Escaleno")
