#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058

# 25- Faça um programa que peça para n pessoas a sua idade, ao final o programa devera
#  verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
#  e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = float(input("Quantas pessoas irão informar a idade?\n"))
i = 0
soma = 0
while i<n:
    idade = int(input())
    soma+=idade
    i+=1
media = soma/n
if media >= 0 and media <= 25:
    print( "Turma jovem!")
elif media >= 26 and media <= 60:
    print ("Turma adulta")
else:
    print ("Turma idosa")
n = int(input("Quantas pessoas irão informar a idade?\n")) ## no lugar de float é int
i = 0
soma = 0
while i<n:
    idade = int(input())
    soma+=idade
    i+=1
media = soma/n
if media >= 0 and media <= 25:
    print ("Turma jovem!")
elif media >= 26 and media <=60:
    print ("Turma adulta")
else:
    print ("Turma idosa")