#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Alexandre Marques Uchôa           1715310028
# Carlos Eduardo T. de Oliveira     1715310030
# Hugo Thadeu Silva Cardoso         1715310013
# Judá Salazar Braga                1515200050
# Kethelen Tamara Braba Barbosa     1525212002
#Escreva um algoritmo em PORTUGOL que receba a altura de 10 atletas. Esse
#algoritmo deve imprimir a altura daqueles atletas que tem altura maior que a média.

lista = list()
i = 0
acimaalt = 0
somaalt = 0
while i < 10:
    altura = float(input())
    somaalt = somaalt + altura
    i += 1
    lista.append(altura)
mediaalt = somaalt/10
print("%.2f" %mediaalt)
acimadamed = list()
for altura in lista:
    if altura > mediaalt:
        acimadamed.append(altura)
print(*acimadamed)