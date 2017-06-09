# --------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA  1515090555
# TIAGO FERREIRA ARANHA              1715310047
# VÍTOR SIMÕES AZEVEDO               1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA   1715310063
# REINALDO VARGAS                    1715310054
#
# 37) Escreva um algoritmo em PORTUGOL que determine todos os divisores de
# um dado número N.
# ---------------------------------------------------------------------------

number = int(input("Number: "))
c = 1  # aux

print("Dividers: ")

while c <= number:

    if number % c == 0:
        print(c)

    c = c + 1
