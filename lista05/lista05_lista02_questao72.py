#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro De Mello         1315120052
# Silas castro de Mendonça          1715310066
# 72.Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e cresce 3
# centímetros por ano. Construir um algoritmo em PORTUGOL que calcule iterativamente
# e imprima quantos anos serão necessários para que Juca seja maior que Chico.

Chico = 1.5
Juca = 1.1
c = 0

while Juca < Chico:

    Chico += 0.02
    Juca += 0.03
    c += 1

print("Levará", c, "anos para Juca ultrapassar a estatura de Chico")
