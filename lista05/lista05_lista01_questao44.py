# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Gabriel Nascimento de Oliveira    1715310052
# Gabriel de Queiroz Souza          1715310044
# Guilherme Silva de Oliveira       1715310034
# Hugo Thadeu Silva Cardoso         1715310013
# Jandinne Duarte de Oliveira       1015070265
# Joelson Pereira Lima              1715310060
#
#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#1 , 2, 3, 4  - Votos para os respectivos candidatos
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
#
eleitores = int(input("Digite o número total de eleitores: "))

var1 = 0

Matheus = 0
Cesar = 0
Camila = 0
Fernanda = 0
Branco = 0
Nulo = 0

from random import randint

while var1 < eleitores:
    voto = randint(0, 5)
    if voto == 1:
        Matheus = Matheus + 1
    if voto == 2:
        Cesar = Cesar + 1
    if voto == 3:
        Camila = Camila + 1
    if voto == 4:
        Fernanda = Fernanda + 1
    if voto == 0:
        Branco = Branco + 1
    if voto == 5:
        Nulo = Nulo + 1
    var1 = var1 + 1

print(("Matheus obteve: "), Matheus, ("votos"))
print(("Cesar obteve: "), Cesar, ("votos"))
print(("Camila obteve: "), Camila, ("votos"))
print(("Fernanda obteve:"), Fernanda, ("votos"))
print(("Votos Brancos:"), Branco, ("votos"))
print(("Votos Nulos:"), Nulo,), ("votos")
print(("Porcentagem de votos nulos é de"), Nulo/var1, ("%"))
print(("Porcentagem de votos brancos é de"), Branco/var1, ("%"))