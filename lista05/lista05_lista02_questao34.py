#----------------------------------------------------------------
# Introdu��o a Programa��o de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro De Mello         1315120052
# Silas castro de Mendon�a          1715310066
# Escreva um algoritmo em Python que calcule 
# o quociente da divis�o de A por B (n�mero inteiros
# e positivos), ou seja, A div B, atrav�s de subtra��es
# sucessivas. Esses dois valores s�o passados pelo usu�rio
# atrav�s do teclado. 

A = int(input("dividendo: "))
B = int(input("divisor: "))

while (A <= 0) or (B <= 0):

    print("valores inv�lidos, devem ser inteiros e positivos")
    A = int(input("dividendo: "))
    B = int(input("divisor: "))

c = 0
A -= B

while A >= 0:

    A -= B
    c += 1

print("Quociente da divis�o:", c)