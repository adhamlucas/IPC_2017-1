#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# Erik Atlio Silva Rey                  1715310059
# Edson de Lima Barros                  1715310043
# Enrique Leão Barbosa Izel             1715310048
# Evandro Padilha Barroso Filho         1715310009
# Fang Yao                              1115180236
#
#12.Escreva um programa que leia três valores com ponto flutuante de dupla precisão:
# A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.
#Entrada:
#O arquivo de entrada contém três valores com um dígito após o ponto decimal.
#Saída:
#O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima,
#sempre com mensagem correspondente e um espaço entre os dois pontos e o valor.
#O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
#-----------------------------------------------------------------------------------------------------------------------

value = input().split()
a = value
b = value
c = value
pi = 3.14159

triangle = (float(a) * float(c)) / 2
circle = pi*(float(c) * float(c))
trapezius = float(c) * (float(a) + float(b)) / 2
square = float(b) * float(b)
rectangle = float(a) * float(b)

print("TRIANGULO: %0.3f" % triangle)
print("CIRCULO: %0.3f" % circle)
print("TRAPEZIO: %0.3f" % trapezius)
print("QUADRADO: %0.3f" % square)
print("RETANGULO: %0.3f" % rectangle)
