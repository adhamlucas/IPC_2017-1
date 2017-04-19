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
# 33.Escreva um algoritmo que calcule o resto da divisão de A por B (número
# inteiros e positivos), ou seja, A mod B, através de subtrações sucessivas.
# Esses dois valores são passados pelo usuário através do teclado.

A = int(input("dividendo: "))
B = int(input("divisor: "))

while (A <= 0) or (B <= 0):
    print("valores inválidos, devem ser inteiros e positivos")
    A = int(input("dividendo: "))
    B = int(input("divisor: "))

C = B

while B <= A:
    B += C

rest = A - (B - C)

print("resto da divisão:", rest)
