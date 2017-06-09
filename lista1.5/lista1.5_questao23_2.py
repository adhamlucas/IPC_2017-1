#---------------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Dayana Picanço Marquez         1715310058
#Felipe Guerreiro de Mello      1315120052
#Faça um programa que receba a medida de dois ângulos de um triângulo, calcule e
#mostre a medida do terceiro ângulo.Sabe-se que a soma dos ângulos de um triângulo é 180
#---------------------------------------------------------------------
angle1 = int(input())
angle2 = int(input())

final_angle = 180 - (angle1 + angle2)

print(final_angle)
